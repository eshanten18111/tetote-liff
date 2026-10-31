/**
 * パッチ後の fetchReadyAnswer / findConversationId を、**本物の Dify API** に当てる。
 * KV だけ偽物。HTTP は本物（api.dify.ai）。
 * 認証はこの環境のプロキシが入れるので、Authorization ヘッダだけ外して投げる。
 */
import fs from 'fs';
const SRC = process.argv[2], USER = process.argv[3], CONV = process.argv[4], WANT = process.argv[5];
let src = fs.readFileSync(SRC,'utf8');
src = src.slice(src.indexOf('/**'), src.lastIndexOf('--56407')).replace('export default {','const _worker = {');
const W = new Function(src+'\nreturn {fetchReadyAnswer,findConversationId};')();
function makeKV(i={}){const s=new Map(Object.entries(i));return{store:s,
 async get(k){return s.has(k)?s.get(k):null},async put(k,v){s.set(k,v)},async delete(k){s.delete(k)}}}
// この環境の node の fetch はプロキシを通らないので、curl で出す。
// Worker 側のコード（URLの組み立て・戻り値の解釈）はそのまま動かす。
import { execFileSync } from 'child_process';
let seen = [];
const real = async (u, o={}) => {
  const args = ['-sS','--max-time','120','-w','\n<<<%{http_code}>>>', String(u)];
  if (o.method && o.method !== 'GET') args.push('-X', o.method);
  for (const [k,v] of Object.entries(o.headers||{})) if (k.toLowerCase()!=='authorization') args.push('-H', `${k}: ${v}`);
  if (o.body) args.push('-d', String(o.body));
  const out = execFileSync('curl', args, {encoding:'utf8', maxBuffer:1<<24});
  const i = out.lastIndexOf('\n<<<');
  const status = Number(out.slice(i+4, out.indexOf('>>>', i)));
  return new Response(out.slice(0,i), {status, headers:{'Content-Type':'application/json'}});
};
globalThis.fetch = async (u,o={}) => { seen.push(String(u)); return real(u,o); };
const ENV = (kv={}) => ({ SESSIONS: makeKV(kv), DIFY_API_KEY: '(proxy)' });
const ok = (n,c)=>console.log((c?'  OK  ':'  NG  ')+n);

console.log("対象の会話:",CONV,"／ 探す文面:",JSON.stringify(WANT));

// 本物の一覧から、その文面の行の created_at を取る
const raw = await real(`https://api.dify.ai/v1/messages?conversation_id=${CONV}&user=${USER}&limit=3`);
const rows = (await raw.json()).data || [];
console.log("  窓(limit=3):", rows.map(r=>`${String(r.query).slice(0,10)}@${r.created_at}`).join(" / "));
const hit = [...rows].reverse().find(r=>String(r.query).trim()===WANT);
console.log("  一致する最新の行 created_at =", hit && hit.created_at);

console.log("\n【1】KVに会話IDがある・sinceMs は受け取り時刻相当");
let env = ENV({[`conv:${USER}`]: CONV});
let a = await W.fetchReadyAnswer(env, USER, WANT, hit.created_at*1000);
ok("できている返事を返した", typeof a==='string' && a.length>0);
console.log("     先頭:", String(a).slice(0,40).replace(/\n/g,'/'));

console.log("\n【2】KVが空 → 本物の /conversations から会話IDを拾えるか");
seen=[]; env = ENV();
a = await W.fetchReadyAnswer(env, USER, WANT, hit.created_at*1000);
ok("会話IDを復元してKVに入れた", env.SESSIONS.store.get(`conv:${USER}`) === CONV);
ok("返事も取れた", typeof a==='string' && a.length>0);
console.log("     叩いたURL:", seen.map(u=>u.replace('https://api.dify.ai/v1','')).join("\n                "));

console.log("\n【3】門：受け取り時刻がその行よりずっと後なら、配らない");
env = ENV({[`conv:${USER}`]: CONV});
a = await W.fetchReadyAnswer(env, USER, WANT, Date.now()+3600000);
ok("古い行として弾いた（null）", a === null);

console.log("\n【4】門：60秒の余裕の内側なら、配る");
env = ENV({[`conv:${USER}`]: CONV});
a = await W.fetchReadyAnswer(env, USER, WANT, hit.created_at*1000 + 55000);
ok("55秒ずれていても配った", typeof a==='string' && a.length>0);

console.log("\n【5】findConversationId 単体（本物の一覧・sort_by 明示）");
const id = await W.findConversationId(ENV(), USER);
ok("いま動いている会話を返した", typeof id==='string' && id.length===36);
console.log("     返り値:", id, id===CONV ? "（対象と一致）" : "（対象とは別＝より新しく動いた会話）");
