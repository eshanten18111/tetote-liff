import fs from 'fs';
const SRC = process.argv[2];
let src = fs.readFileSync(SRC,'utf8');
src = src.slice(src.indexOf('/**'), src.lastIndexOf('--56407'));
src = src.replace('export default {','const _worker = {');
function makeKV(i={}){const s=new Map(Object.entries(i));return{store:s,
 async get(k){return s.has(k)?s.get(k):null},async put(k,v){s.set(k,v)},async delete(k){s.delete(k)},
 async list({prefix}){return{keys:[...s.keys()].filter(k=>k.startsWith(prefix)).map(name=>({name}))}}}}
function makeFetch(script){const calls=[];const fn=async(u,o={})=>{u=String(u);calls.push({u,body:o.body});
 for(const[p,h]of script){if(u.includes(p))return h(calls,o)}
 return new Response('{}',{status:200,headers:{'Content-Type':'application/json'}})};fn.calls=calls;return fn}
const json=(o,s=200)=>new Response(JSON.stringify(o),{status:s,headers:{'Content-Type':'application/json'}});
const names=['retryPending','fetchReadyAnswer'];
const W=new Function(src+'\nreturn {'+names.join(',')+'};')();
const ENV=()=>({SESSIONS:makeKV(),DIFY_API_KEY:'d',LINE_CHANNEL_ACCESS_TOKEN:'d',
 GAS_URL:'https://example.invalid/exec',GAS_TOKEN:'d',SLACK_WEBHOOK_URL:''});

console.log("シナリオ：1通目が遅く、最初の聞き直しが失敗した回");
console.log(" t=0     相談者が「はい」を送る（Difyには行が出来て、返事も書けている）");
console.log(" t=180s  3回覗いても間に合わず、聞き直した → それも失敗（tries=1, p.at=180s に更新）");
console.log(" t=300s  次の拾い直し。できている返事は配られるか？\n");
const env=ENV(); const now=Date.now();
env.SESSIONS.store.set('conv:UZ','conv-z');
// p.at は「聞き直した時刻」に書き換わっている（120秒前 = LOCK_MS を過ぎている）
env.SESSIONS.store.set('pending:UZ',JSON.stringify({text:'はい',at:now-130000,recv:now-430000,tries:1,peeks:3}));
let regenerated=0;
globalThis.fetch=makeFetch([
 ['/messages',()=>json({data:[{query:'はい',answer:'本当の返事（t=0に書けている）',
    created_at:Math.floor((now-430000)/1000)}]})],
 ['/chat-messages',()=>{regenerated++;return json({conversation_id:'conv-z',answer:'聞き直して作り直した返事'})}],
]);
const stat=await W.retryPending(env);
const pushed=globalThis.fetch.calls.filter(c=>c.u.includes('/message/push'));
const delivered=pushed.length?JSON.parse(String(pushed[0].body)).messages[0].text:'(なし)';
console.log(" 配られたもの      :",delivered);
console.log(" AIに聞き直した回数:",regenerated);
console.log(" 判定:",delivered.startsWith('本当の返事')?'OK できている返事を配った':'NG できている返事を捨てて作り直した');

console.log("\n対照：p.at が受け取り時刻のままなら（＝聞き直しが1度も無い回）");
const e2=ENV(); e2.SESSIONS.store.set('conv:UY','conv-y');
e2.SESSIONS.store.set('pending:UY',JSON.stringify({text:'はい',at:now-430000,tries:0,peeks:2}));
let r2=0;
globalThis.fetch=makeFetch([
 ['/messages',()=>json({data:[{query:'はい',answer:'本当の返事（t=0に書けている）',
    created_at:Math.floor((now-430000)/1000)}]})],
 ['/chat-messages',()=>{r2++;return json({conversation_id:'conv-y',answer:'作り直し'})}],
]);
await W.retryPending(e2);
const p2=globalThis.fetch.calls.filter(c=>c.u.includes('/message/push'));
console.log(" 配られたもの      :",p2.length?JSON.parse(String(p2[0].body)).messages[0].text:'(なし)');
console.log(" AIに聞き直した回数:",r2);
