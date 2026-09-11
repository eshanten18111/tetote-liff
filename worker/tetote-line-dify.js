--56407dacb0c65e64e475d6edbeefa934bb11dea87c3883d273e8a71933ab
Content-Disposition: form-data; name="worker.js"

/**
 * LINE ⇄ Dify 中継 (Cloudflare Workers)
 *
 * 役割は4つです。
 *   1. LINEからのWebhookを受け、署名を検証する            → POST /
 *   2. Difyのチャットフローを呼ぶ（会話IDを保持して、続きとして話す）
 *   3. 返ってきた本文をLINEに返信する
 *   4. 入力フォーム（LIFF）の中身を、トークを通さずに直接受け取る → POST /form
 *   5. 届かなかった返事を拾い直す（Apps Scriptが1分ごとに叩く）  → POST /retry
 *
 * 【設計上の要点】
 * ・LINEには先に200を返し、Difyの呼び出しは waitUntil で裏に回す。
 *   Difyの応答は20〜40秒かかることがあり、待たせるとLINEが再送して
 *   同じ返信が二重に届くため。
 * ・ただし waitUntil は約30秒で打ち切られる。ここに間に合わなかった回は
 *   「未返信」としてKVに残り、/retry が拾い直す。
 *   /retry を外（Apps Script）から叩く形にしたのは、返事を待っている相手が
 *   いるあいだは打ち切られないため。裏の仕事には、その30秒しかない。
 * ・会話IDをKVに保存する。これがないとDifyの会話変数（支援必要度・フェーズ）が
 *   毎回リセットされ、設計した積み上げが一切効かなくなる。
 * ・Difyが落ちているときも、24時間窓口だけは必ず返す。
 *   相談者を手ぶらで放置しないため。
 *
 * 【/form について（C案）】
 * ・従来は liff.sendMessages() でフォームの中身を「相談者本人の発言」として
 *   トークに流していた。そのため
 *     - 電話番号・氏名がトーク画面に残り、同居者に見られうる
 *     - 同じ内容がDify（AI）にも渡る
 *   という2つの結果が同時に起きていた。
 * ・/form は、フォームの中身をトークに出さず、ここで受け取って
 *   記録（GAS）と通知（Slack）だけを行う。
 *   トークに出るのは「詳細確認フォーム回答：受付しました」という短い合図だけ。
 * ・本人確認は LINEのIDトークン検証で行う。フォームのURLを知っただけの
 *   第三者が他人の記録に書き込めないようにするため。
 *
 * 【扱わないもの】
 * ・相談内容はログに出しません（要配慮個人情報のため）。
 */
 
const CONV_TTL = 60 * 60 * 24 * 30; // 会話IDの保持期間：30日
 
// フォームを置いている場所。ここ以外からの /form は受け付けない。
const ALLOWED_ORIGIN = 'https://eshanten18111.github.io';
 
// LIFFアプリのチャネルID（公開値。秘密ではない）
const LIFF_CHANNEL_ID = '2010836980';
 
// Difyが応答しないときの最終手段。ここは生成に頼らず定型で返す。
const FALLBACK =
  'うまくお返事できませんでした。申し訳ありません。\n' +
  'もう一度お送りいただくか、お急ぎの場合は下記の窓口もご利用いただけます。\n\n' +
  '・#いのちSOS　0120-061-338（24時間365日）\n' +
  '・よりそいホットライン　0120-279-338（24時間）\n\n' +
  'いのちに関わる緊急のときは119番、事件や事故のときは110番にお電話ください。';
 
// --- 無返信を防ぐための時間の設定 ---
//
// 【ここは推測で決めてはいけない場所です】
// Cloudflareは、LINEに200を返したあとの裏の仕事（waitUntil）を
// 「受け取りから約30秒」で強制終了する。ログにこう残っていた：
//   waitUntil() tasks did not complete within the allowed time ... have been canceled
// つまり何秒待つと書いても、実際に使えるのは30秒だけ。
// 以前ここに100秒と書いていたが、それは効いていなかった。
// Difyの返事は書けていたのに、届ける係が先に消されていた。
//
// 24秒 … ここで見切りをつけ、あとは1分ごとの見張りに渡す。
//        「お待たせしています」を送るのは、この見切りに達したときだけ。
//        待っているあいだは、LINEの「…」表示（60秒もつ）で足りる。
const ANSWER_TIMEOUT_MS = 24000;
 
// 24秒で答えが出なかったとき、その相談は「未返信」としてKVに残る。
// 1分ごとの定期実行が拾い直し、あらためてAIに聞いて、プッシュで届ける。
// 打ち切って定型文を返すのは、2回やり直しても駄目だったときだけ。
//
// 時間は2つある。混ぜると二重送信になるので、分けてある。
//   FIRST_PICKUP_MS … 受け取ってから、拾い直しが手をつけてよくなるまで
//   LOCK_MS        … 拾い直しが手をつけたあと、次に触ってよくなるまで
//                    （AIの生成中に次の定期実行が重ねて呼ぶと、同じ返事が2通届く）
//
// FIRST_PICKUP_MS は、必ず ANSWER_TIMEOUT_MS より長くしてください。
// 短いと、本線がまだ待っている最中に拾い直しが手をつけ、
// 同じ質問にAIが2回答えることになります（1回それをやりました）。
const FIRST_PICKUP_MS = 30000;
const LOCK_MS = 120000;
const MAX_TRIES = 2;          // やり直しの上限
const PENDING_TTL = 60 * 60;  // 1時間で自動的に消える（取りこぼしを溜めない）
 
const WAIT_NOTICE =
  'お待たせしています。いま、いただいた内容を読んでいます。\n' +
  'もう少しだけお時間をください。このまま開いたままで大丈夫です。';
 
export default {
  // Cloudflare側の定期実行。
  //
  // いまスケジュールは登録していない（拾い直しの係を2つ持つと、
  // 同じ返事が2通届く事故につながる）。拾い直しは Apps Script が
  // 1分ごとに /retry を叩く形に一本化した。
  // この受け口だけ残してあるのは、Apps Script が止まったときに
  // Cloudflare側だけで動かせるようにするため（Cron を1本足せば動く）。
  async scheduled(event, env, ctx) {
    await retryPending(env);
  },
 
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
 
    // --- 未返信の拾い直し（外から1分ごとに叩いてもらう） ---
    //
    // なぜ外から叩く形にしたか。
    // Cloudflareは「返事を返したあとの裏の仕事」を約30秒で打ち切る。
    // AIの生成に25秒かかると、そこに間に合わない回が必ず出る。
    // ところが、こうして誰かが返事を待っている最中は打ち切られない。
    // だから拾い直しは「待ってくれる相手」に呼んでもらう。
    // 呼ぶのは Apps Script の1分ごとの定期実行（GASは5分待てる）。
    if (url.pathname === '/retry') {
      if (request.method !== 'POST') return new Response('ok');
      let tok = '';
      try { tok = String((await request.json()).token || ''); } catch (_) {}
      if (!env.GAS_TOKEN || tok !== env.GAS_TOKEN) {
        return new Response('unauthorized', { status: 401 });
      }
      const result = await retryPending(env);
      return new Response(JSON.stringify({ ok: true, ...result }), {
        headers: { 'Content-Type': 'application/json' },
      });
    }
 
    if (url.pathname === '/form') {
      return handleForm(request, env, ctx);
    }
 
    if (url.pathname === '/prefill') {
      return handlePrefill(request, env);
    }
 
    if (request.method !== 'POST') {
      return new Response('ok'); // 疎通確認用
    }
 
    const raw = await request.text();
    const signature = request.headers.get('x-line-signature') || '';
 
    if (!(await verifySignature(raw, signature, env.LINE_CHANNEL_SECRET))) {
      return new Response('invalid signature', { status: 401 });
    }
 
    let body;
    try {
      body = JSON.parse(raw);
    } catch {
      return new Response('bad request', { status: 400 });
    }
 
    // 先に200を返し、処理は裏で続ける
    ctx.waitUntil(handleEvents(body.events || [], env, ctx));
    return new Response('ok');
  },
};
 
/* ============================================================ フォーム受け口 */
 
function corsHeaders() {
  return {
    'Access-Control-Allow-Origin': ALLOWED_ORIGIN,
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '86400',
  };
}
 
function jsonResponse(obj, status = 200) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { 'Content-Type': 'application/json', ...corsHeaders() },
  });
}
 
/**
 * フォーム送信の受け口。
 *
 * 期待するリクエスト（フォーム側から fetch で送る）:
 *   POST /form
 *   { "idToken": "...", "mode": "detail" | "addendum",
 *     "fields": { "name": "...", "phoneNumber": "...", ... } }
 *
 * 返すもの: { ok: true }
 *
 * 応答は速く返す。記録と通知は waitUntil で裏に回す。
 * 相談者の画面を、GASやSlackの遅さで待たせないため。
 */
async function handleForm(request, env, ctx) {
  if (request.method === 'OPTIONS') {
    return new Response(null, { status: 204, headers: corsHeaders() });
  }
  if (request.method !== 'POST') {
    return jsonResponse({ ok: false, error: 'method' }, 405);
  }
 
  let body;
  try {
    body = await request.json();
  } catch {
    return jsonResponse({ ok: false, error: 'bad json' }, 400);
  }
 
  // --- 本人確認 ---
  const userId = await verifyIdToken(body.idToken);
  if (!userId) {
    return jsonResponse({ ok: false, error: 'unauthorized' }, 401);
  }
 
  // --- 会話IDの引き当て ---
  // トークで一度でも話していればKVにある。無い場合も記録は落とさず、
  // LINEのユーザーIDを鍵にして1行作る（後で人が突き合わせられるように）。
  const conversationId = (await env.SESSIONS.get(`conv:${userId}`)) || `line:${userId}`;
 
  const f = body.fields || {};
  const mode = String(body.mode || 'detail');
 
  ctx.waitUntil(recordForm(env, conversationId, mode, f, userId));
 
  return jsonResponse({ ok: true });
}
 
/**
 * 先にお聞きした内容を返す（引き継ぎフォームの再確認用）。
 *
 * 入口フォームで都道府県をうかがっている。引き継ぎフォームでは、
 * それを選択済みで見せて「相違ないか」を確かめてもらう。
 * 空欄の状態で聞き直すと、確認ではなく二度目の質問になる。
 *
 * 返すのは都道府県と呼び名だけ。電話番号など、
 * 見られて困るものはここから返さない。
 */
async function handlePrefill(request, env) {
  if (request.method === 'OPTIONS') {
    return new Response(null, { status: 204, headers: corsHeaders() });
  }
  if (request.method !== 'POST') {
    return jsonResponse({ ok: false, error: 'method' }, 405);
  }
  let body;
  try { body = await request.json(); } catch { return jsonResponse({ ok: false }, 400); }
 
  const userId = await verifyIdToken(body.idToken);
  if (!userId) return jsonResponse({ ok: false, error: 'unauthorized' }, 401);
  if (!env.GAS_URL || !env.GAS_TOKEN) return jsonResponse({ ok: true, found: false });
 
  const conversationId = (await env.SESSIONS.get(`conv:${userId}`)) || `line:${userId}`;
  try {
    const res = await fetch(env.GAS_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        token: env.GAS_TOKEN,
        conversationId,
        lineUserId: userId,
        op: 'read',
      }),
    });
    if (!res.ok) return jsonResponse({ ok: true, found: false, visits: 0 });
    const d = await res.json();
    return jsonResponse({
      ok: true,
      found: !!d.found,
      visits: Number(d.visits || 0),
      name: d.name || '',
      ageGroup: d.ageGroup || '',
      gender: d.gender || '',
      prefecture: d.prefecture || '',
      mainIssue: d.mainIssue || '',
    });
  } catch (err) {
    console.log('prefill failed:', String(err && err.message));
    return jsonResponse({ ok: true, found: false, visits: 0 });
  }
}
 
/**
 * LINEのIDトークンを検証して、ユーザーID（sub）を取り出す。
 *
 * 署名・有効期限・宛先（aud）をLINE側で確かめてもらう。
 * 自前で解析しないのは、期限切れや偽造を見落とさないため。
 */
async function verifyIdToken(idToken) {
  if (!idToken) return null;
  try {
    const res = await fetch('https://api.line.me/oauth2/v2.1/verify', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({ id_token: idToken, client_id: LIFF_CHANNEL_ID }),
    });
    if (!res.ok) {
      console.log('id token verify failed:', res.status);
      return null;
    }
    const data = await res.json();
    return data.sub || null;
  } catch (err) {
    console.log('id token verify error:', String(err && err.message));
    return null;
  }
}
 
/**
 * フォームの中身を記録し、必要なら通知する。
 *
 * ここが、これまでDify側の「パラメータ抽出（詳細確認フォーム回答）」と
 * 「IF/ELSE 5（危険判定）」がやっていた仕事を引き取る場所。
 * AIの読み取り精度に頼らず、フォームの選択値をそのまま使う。
 */
async function recordForm(env, conversationId, mode, f, userId) {
  const payload = { token: env.GAS_TOKEN, conversationId };
  // 会話IDは30日で切れる。切れると同じ方でも別人の行になるので、
  // LINEが発行する記号もいっしょに置いておき、後から同じ方だと分かるようにする。
  if (userId) payload.lineUserId = userId;
  const lines = [];
 
  if (mode === 'note') {
    payload.addendumText = f.noteText || '';
  } else if (mode === 'close') {
    payload.closeAnswer = f.closeAnswer || '';
    payload.addendumText =
      `【終了確認】${f.closeAnswer || ''}` + (f.noteText ? `\n${f.noteText}` : '');
  } else if (mode === 'rebook') {
    payload.appointmentAt = joinAppointment(f);
    payload.callStatus = '再予約';
    if (f.situation) payload.addendumText = `【再予約の事情】${f.situation}`;
  } else {
    // general / safety
    payload.name = f.name || '';
    payload.prefecture = f.prefecture || '';
    payload.city = f.city || '';
    payload.contactMethod = f.contactMethod || '';
    payload.phoneNumber = f.phoneNumber || '';
    payload.timeSlots = f.timeSlots || '';
    payload.safetyQ3 = f.safetyQ3 || '';
    payload.consent = f.consent || '';
    // ルートと状態は、どのフォームから来たかで決まる。
    //   call   … LINE通話。ご本人からかけていただく（いまの既定）
    //   safety … 同じくLINE通話。安全配慮の説明つき（緊急時用に温存）
    //   general… こちらから電話をかける（緊急時対応が決まるまで使わない）
    // 「着電待ち」にしておかないと、未着電の自動チェックが拾わない。
    payload.route =
      mode === 'general' ? '折り返し（こちらから架電）'
      : mode === 'safety' ? '安全配慮（LINE通話）'
      : 'LINE通話（ご本人から）';
    payload.appointmentAt = joinAppointment(f);
    payload.callStatus = mode === 'general' ? '架電待ち' : '着電待ち';
    if (f.urgentDetail) lines.push(`【いますぐ危険・本人記入】${f.urgentDetail}`);
    if (f.situation) lines.push(`【状況】${f.situation}`);
    if (f.note) lines.push(`【備考】${f.note}`);
    if (lines.length) payload.addendumText = lines.join('\n');
  }
 
  await postToGas(env, payload);
  await notifySlackForForm(env, conversationId, mode, f, payload);
}
 
/**
 * 予約日時を1つの文字列にまとめる。
 * シート側で日付として扱えるよう、"YYYY-MM-DD HH:MM" の形にする。
 */
function joinAppointment(f) {
  if (!f.appointmentDate || !f.appointmentTime) return '';
  return `${f.appointmentDate} ${f.appointmentTime}`;
}
 
/**
 * 予約を「1時間の枠」として人に見せる。
 * 担当者はこの1時間を待機し、過ぎたら未着電として扱う。
 */
function appointmentBand(at) {
  if (!at) return '（未記入）';
  const m = at.match(/^(\S+)\s+(\d{1,2}):(\d{2})$/);
  if (!m) return at;
  const h = Number(m[2]);
  return `${m[1]} ${h}時〜${h + 1}時`;
}
 
async function postToGas(env, payload) {
  if (!env.GAS_URL || !env.GAS_TOKEN) {
    console.log('GAS not configured');
    return;
  }
  try {
    const res = await fetch(env.GAS_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });
    if (!res.ok) {
      console.log('gas write failed:', res.status);
      await postNotice(
        env,
        '⚠️ 記録シートに書き込めませんでした（' + res.status + '）\n' +
          '会話ID：' + (payload.conversationId || '不明') + '\n' +
          'この方の内容はシートに残っていません。相談者には受付できた旨が出ています。' +
          'Cloudflareのログを確認してください。'
      );
      return;
    }
 
    // ここが要点。
    // Apps Script は、合言葉が違っても「HTTP 200」を返す。
    // 中身に {"ok": false} と書いて返してくるだけなので、
    // res.ok だけを見ていると、書けていないことに誰も気づけない。
    // 実際、これで3日間ぶんの記録が黙って落ちた。中身まで確かめる。
    let reason = '';
    try {
      const d = await res.json();
      if (d && d.ok === false) reason = String(d.error || 'unknown');
    } catch (_) {
      // JSONでない応答＝ログイン画面などが返っている。URLかアクセス権を疑う。
      reason = 'JSON以外の応答（デプロイURLかアクセス権を確認）';
    }
    if (reason) {
      console.log('gas rejected:', reason);
      await postNotice(
        env,
        '⚠️ 記録シートに拒否されました（' + reason + '）\n' +
          '会話ID：' + (payload.conversationId || '不明') + '\n' +
          'この方の内容はシートに残っていません。相談者には受付できた旨が出ています。\n' +
          '合言葉（GAS_TOKEN）とウェブアプリURL（GAS_URL）が合っているかご確認ください。'
      );
    }
  } catch (err) {
    console.log('gas write error:', String(err && err.message));
    await postNotice(
      env,
      '⚠️ 記録シートに届きませんでした\n' +
        '会話ID：' + (payload.conversationId || '不明') + '\n' +
        'この方の内容はシートに残っていません。Cloudflareのログを確認してください。'
    );
  }
}
 
/**
 * フォームが届いたことをSlackへ知らせる。
 *
 * 「今すぐ危険」に はい が入っているときは、文面を変えて必ず目立たせる。
 * ここは相談者が自分で申告した内容なので、AIの判定より確度が高い。
 * 電話番号そのものはSlackに流さない（記録シートを見てもらう）。
 */
async function notifySlackForForm(env, conversationId, mode, f, payload) {
  const danger = String(f.safetyQ3 || '').includes('はい');
 
  let head;
  if (mode === 'close') head = '🔚 終了確認の回答が届きました';
  else if (mode === 'note') head = '📝 備考・特記事項が届きました';
  else if (mode === 'rebook') head = '📅 あらためてのご希望日時が届きました';
  else if (mode === 'safety') head = '📞 安全配慮ルートのご予約が届きました（LINE通話・着電待ち）';
  else head = '📥 折り返しのご予約が届きました（こちらから架電）';
 
  // 危険ありでも通知の形は変えない。分け隔てなく同じ通知にしたうえで、
  // 見出しに印だけ足して、一覧で拾えるようにする。
  if (danger) head += '　【いますぐの危険：はい】';
 
  const lines = [head, `会話ID：${conversationId}`];
 
  if (mode === 'note') {
    lines.push(`内容：${f.noteText || ''}`);
  } else if (mode === 'close') {
    lines.push(`回答：${f.closeAnswer || ''}`);
    if (f.noteText) lines.push(`内容：${f.noteText}`);
  } else if (mode === 'rebook') {
    lines.push(`ご希望の時間帯：${appointmentBand(payload.appointmentAt)}（この1時間、待機してください）`);
    if (f.situation) lines.push(`ご事情：${f.situation}`);
  } else {
    lines.push(`呼び名：${f.name || '（未記入）'}`);
    lines.push(`地域：${f.prefecture || ''}${f.city || ''}`);
    if (mode === 'safety') {
      lines.push(`お約束の時間帯：${appointmentBand(payload.appointmentAt)}（この1時間、待機してください）`);
      lines.push(`状況：${f.situation || ''}`);
    } else {
      lines.push(`希望時間帯：${f.timeSlots || '（未記入）'}`);
    }
    lines.push(`いますぐ危険：${f.safetyQ3 || '－'}`);
    if (f.urgentDetail) lines.push(`本人記入の状況：${f.urgentDetail}`);
    if (f.note) lines.push(`備考：${f.note}`);
    if (mode === 'safety') {
      lines.push('※ 画面や着信を他の方に見られる可能性があります。こちらから電話をかけないでください。');
    }
    lines.push('※ 電話番号は記録シートをご確認ください（ここには載せていません）。');
  }
 
  await postNotice(env, lines.join('\n'));
}
 
/**
 * 通知の送り先。
 * Slack と Google Chat の両方に対応する。片方だけ設定しても動く。
 * Google Chat の Webhook は { text: "..." } を受け取るので、形は同じでよい。
 */
async function postNotice(env, text) {
  const targets = [env.SLACK_WEBHOOK, env.CHAT_WEBHOOK].filter(Boolean);
  if (!targets.length) {
    console.log('no notification webhook configured');
    return;
  }
  for (const url of targets) {
    try {
      const res = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text }),
      });
      // 通知先が拒否しても黙って消えないようにする。
      // 通知は「届かなかったこと」に誰も気づけないのが一番こわい。
      if (!res.ok) {
        console.log('notify rejected:', res.status, (await res.text()).slice(0, 120));
      } else {
        console.log('notify ok');
      }
    } catch (err) {
      console.log('notify error:', String(err && err.message));
    }
  }
}
 
/* ------------------------------------------------------------------ 署名検証 */
async function verifySignature(raw, signature, secret) {
  if (!signature || !secret) return false;
  const key = await crypto.subtle.importKey(
    'raw',
    new TextEncoder().encode(secret),
    { name: 'HMAC', hash: 'SHA-256' },
    false,
    ['sign']
  );
  const mac = await crypto.subtle.sign('HMAC', key, new TextEncoder().encode(raw));
  const expected = btoa(String.fromCharCode(...new Uint8Array(mac)));
  return timingSafeEqual(expected, signature);
}
 
function timingSafeEqual(a, b) {
  if (a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}
 
/* ------------------------------------------------------------------ 本処理 */
async function handleEvents(events, env, ctx) {
  for (const event of events) {
    try {
      if (event.type === 'follow') {
        // 「はじめまして」の一言はLINE側のあいさつメッセージが引き受ける。
        // ここはその続きとして、待ち時間のことと緊急時の窓口だけを伝える。
        await replyToLine(env, event.replyToken, [
          'この相談チャット機能では、いまお困りのことをお聞きして、いっしょに整理します。\n' +
            'どんなことでも、書ける範囲で構いません。\n' +
            'お返事まで、30秒ほどお時間をいただくことがあります。\n' +
            '画面に「…」が出ているあいだは、こちらで受け取って考えています。少しだけお待ちください。\n' +
            'いのちに関わる緊急のときは119番、事件や事故のときは110番へお願いします。',
        ]);
        continue;
      }
      if (event.type !== 'message' || event.message?.type !== 'text') continue;
 
      const userId = event.source?.userId;
      const text = event.message.text;
      if (!userId || !text) continue;
 
      // 先に「入力中」を出してから考える。無言の20〜40秒を作らないため。
      await startLoading(env, userId);
 
      // --- 無返信を絶対に起こさないための備え ---
      //
      // 相談者は、こちらの事情を知らない。返事が来なければ「無視された」だけが残る。
      // だから、何があっても必ず何かを返す。
      //
      //  1) 待っているあいだは「…」を出しておく（上の startLoading。60秒もつ）
      //  2) 24秒で見切りをつけ、そのときだけ「お待たせしています」を送る
      //     （ここで定型文にはしない。まだAIの返事が間に合う見込みがある）
      //  3) 「未返信」として置いたまま、1分ごとの見張りに渡す
      //  4) 送信そのものが失敗したら、相談員に知らせる（人が拾えるように）
      //
      // 以前は8秒で「お待たせしています」を送っていた。
      // 1往復が19秒なので、毎回それが挟まり、トークが読みづらくなっていた。
      // 普通に返せる回に、待たせている旨を伝える必要はない。
 
      // 先に「未返信」として置いておく。届けられたら消す。
      // 消えないまま残ったものを、1分ごとの定期実行が拾い直す。
      const pendingKey = `pending:${userId}`;
      await env.SESSIONS.put(
        pendingKey,
        JSON.stringify({ text, at: Date.now(), tries: 0 }),
        { expirationTtl: PENDING_TTL }
      );
 
      const answer = await Promise.race([
        askDify(env, userId, text),
        sleep(ANSWER_TIMEOUT_MS).then(() => null),
      ]);
 
      if (answer === null || answer === FALLBACK) {
        // ここでは打ち切らない。定型文も送らない。
        // 待っていてほしい旨だけ伝えて、あとは見張りに渡す。
        try { await pushToLine(env, userId, [WAIT_NOTICE]); } catch (_) {}
        console.log('answer pending, will retry:', userId);
        continue;
      }
 
      await replyToLine(env, event.replyToken, splitMessages(answer), userId);
      await env.SESSIONS.delete(pendingKey);
 
      // 返事を出したあとに、記録の行へLINEの記号を書き添える。
      // 返事より先にやると、そのぶん相談者を待たせることになる。
      // 会話ごとに一度だけでよいので、済んだ印をKVに置く。
      await stampUserId(env, userId);
    } catch (err) {
      console.log('event handling failed:', String(err && err.message));
      if (event.replyToken) {
        try {
          await replyToLine(env, event.replyToken, [FALLBACK], event.source?.userId);
        } catch (_) {}
      }
      // 相談者には「うまくお返事できませんでした」と出ている。
      // それを相談員が知らないままだと、黙って人が離れていく。
      try {
        await postNotice(
          env,
          '⚠️ お返事を返せませんでした\n' +
            'この方には、うまく返事ができなかった旨のご案内が出ています。\n' +
            'チャットからの声かけをご検討ください。'
        );
      } catch (_) {}
    }
  }
}
 
/**
 * 記録の行に、LINEが発行する記号を書き添える。
 *
 * 会話IDは30日で切れる。切れたあとに同じ方が来ると別の行になり、
 * 何度目のご相談かが分からなくなる。それを繋ぐための印。
 * 名前でも電話番号でもなく、このアカウント内でだけ意味を持つ記号。
 */
async function stampUserId(env, userId) {
  try {
    const conversationId = await env.SESSIONS.get(`conv:${userId}`);
    if (!conversationId) return;
    const mark = `uid:${conversationId}`;
    if (await env.SESSIONS.get(mark)) return;
    await postToGas(env, { token: env.GAS_TOKEN, conversationId, lineUserId: userId });
    await env.SESSIONS.put(mark, '1', { expirationTtl: 60 * 60 * 24 * 40 });
  } catch (err) {
    console.log('stamp failed:', String(err && err.message));
  }
}
 
/* ------------------------------------------------------------------ Dify */
async function askDify(env, userId, query) {
  const key = `conv:${userId}`;
  let conversationId = (await env.SESSIONS.get(key)) || '';
 
  let data = await callDify(env, query, conversationId, userId);
 
  // 会話IDが無効になっていたら新しい会話としてやり直す。
  //
  // 会話が無効になる理由は複数ある：30日経過、Difyでの削除、
  // ワークフローを作り直したことで前の会話とつながらなくなった、など。
  // Difyはそれを 404 で返すことも 400 で返すこともあるので、両方拾う。
  // ここで諦めると、相談者は「うまくお返事できませんでした」しか見られない。
  if (!data.ok && conversationId && (data.status === 404 || data.status === 400)) {
    console.log('conversation may be stale, retrying as new:', data.status);
    await env.SESSIONS.delete(key);
    conversationId = '';
    data = await callDify(env, query, '', userId);
  }
  if (!data.ok) {
    // 本文も出す。番号だけでは原因が分からず、毎回ここで止まるため。
    // Difyが返すのはエラーの説明で、相談内容は含まれない。
    console.log('dify error status:', data.status, data.body || '');
    return FALLBACK;
  }
 
  if (data.json.conversation_id && data.json.conversation_id !== conversationId) {
    await env.SESSIONS.put(key, data.json.conversation_id, { expirationTtl: CONV_TTL });
  }
  const answer = (data.json.answer || '').trim();
  return answer || FALLBACK;
}
 
/**
 * 「その質問への答え、もう書けていますか」とDifyに聞く。
 *
 * 【なぜこれが必要か】
 * 24秒に間に合わなかった回を、拾い直しが「もう一度AIに聞き直す」形にしていた。
 * その結果、同じ質問にAIが2回答え、Difyの履歴には
 * 相談者が見ていない返事が1通残った。AIは「自分は言った」と思っている文章が
 * 相手には届いていない状態で、次の往復から話が食い違う。
 *
 * 実際には、間に合わなかっただけで返事は完成している。
 * だから聞き直すのではなく、できているものを取ってきて届ける。
 * 生成も1回で済むので、そのぶん速い。
 *
 * 返り値：届けられる本文。まだ無ければ null。
 */
async function fetchReadyAnswer(env, userId, query) {
  const conversationId = await env.SESSIONS.get(`conv:${userId}`);
  if (!conversationId) return null;
 
  const base = env.DIFY_BASE_URL || 'https://api.dify.ai/v1';
  const url = `${base}/messages?conversation_id=${encodeURIComponent(conversationId)}` +
    `&user=${encodeURIComponent(userId)}&limit=3`;
 
  let json;
  try {
    const res = await fetch(url, {
      headers: { Authorization: `Bearer ${env.DIFY_API_KEY}` },
    });
    if (!res.ok) {
      console.log('fetch ready answer failed:', res.status);
      return null;
    }
    json = await res.json();
  } catch (err) {
    console.log('fetch ready answer error:', String(err && err.message));
    return null;
  }
 
  const list = Array.isArray(json && json.data) ? json.data : [];
  const want = String(query || '').trim();
 
  // 新しいものから見る。同じ質問への、中身のある答えを探す。
  for (let i = list.length - 1; i >= 0; i--) {
    const m = list[i] || {};
    if (String(m.query || '').trim() !== want) continue;
    const answer = String(m.answer || '').trim();
    if (!answer || answer === FALLBACK) return null; // まだ書けていない
    return answer;
  }
  return null;
}
 
async function callDify(env, query, conversationId, userId) {
  const res = await fetch(`${env.DIFY_BASE_URL || 'https://api.dify.ai/v1'}/chat-messages`, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${env.DIFY_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      inputs: {},
      query,
      response_mode: 'blocking',
      conversation_id: conversationId || undefined,
      user: userId,
    }),
  });
  if (!res.ok) {
    let body = '';
    try { body = (await res.text()).slice(0, 300); } catch (_) {}
    return { ok: false, status: res.status, body };
  }
  return { ok: true, json: await res.json() };
}
 
/* ------------------------------------------------------------------ LINE */
/**
 * LINEの「入力中」表示（ローディングアニメーション）を出す。
 *
 * Difyの応答は20〜40秒かかる。その間、相談者の画面には何も起きない。
 * 「助けて」と書いた直後の無言は、無視されたと受け取られる。
 *
 * これはメッセージとして数えられないので、LINEの無料枠を消費しない。
 * 失敗しても本筋は止めない（表示が出ないだけ）。
 */
async function startLoading(env, userId) {
  if (!userId) return;
  try {
    await fetch('https://api.line.me/v2/bot/chat/loading/start', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${env.LINE_CHANNEL_ACCESS_TOKEN}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ chatId: userId, loadingSeconds: 60 }),
    });
  } catch (err) {
    console.log('loading indicator failed:', String(err && err.message));
  }
}
 
/**
 * Difyの本文を、LINEの複数バブルに分ける。
 * プロンプト側で「---」だけの行を区切りとして出力させている。
 * フェーズ2の①②③を別々のメッセージで届けるために必要。
 */
function splitMessages(text) {
  const parts = String(text)
    .split(/\n\s*---+\s*\n/)
    .map((s) => s.trim())
    .filter(Boolean);
  const chunks = [];
  for (const p of parts.length ? parts : [String(text)]) {
    // LINEの1メッセージ上限は5000字。念のため分割する。
    for (let i = 0; i < p.length; i += 4800) chunks.push(p.slice(i, i + 4800));
  }
  // 1回の返信で送れるのは5通まで。6通目以降は捨てずに5通目へまとめる。
  // 相談者にとっては、途中で切れた文章がいちばん不安になる。
  if (chunks.length > 5) {
    const tail = chunks.slice(4).join('\n\n');
    return chunks.slice(0, 4).concat([tail.slice(0, 4800)]);
  }
  return chunks;
}
 
async function replyToLine(env, replyToken, texts, userIdForPush) {
  const messages = texts.map((t) => ({ type: 'text', text: t }));
  const res = await fetch('https://api.line.me/v2/bot/message/reply', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${env.LINE_CHANNEL_ACCESS_TOKEN}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ replyToken, messages }),
  });
  if (res.ok) return;
 
  // 返信トークンが期限切れの場合はプッシュで送る（処理に時間がかかったとき）
  console.log('reply failed:', res.status);
  if (!userIdForPush) return;
  const push = await fetch('https://api.line.me/v2/bot/message/push', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${env.LINE_CHANNEL_ACCESS_TOKEN}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ to: userIdForPush, messages }),
  });
  if (push.ok) return;
 
  // ここまで来たら、相談者には何も届いていない。いちばん起きてはいけない状態。
  // 黙って終わらせず、必ず相談員に知らせる。
  console.log('push failed:', push.status);
  try {
    await postNotice(
      env,
      '🚨 相談者にお返事が届いていません（' + push.status + '）\n' +
        'LINEユーザーID：' + userIdForPush + '\n' +
        'この方の画面には何も表示されていません。' +
        'チャット画面から直接お声がけしてください。'
    );
  } catch (_) {}
}
 
function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}
 
async function pushToLine(env, userId, texts) {
  const res = await fetch('https://api.line.me/v2/bot/message/push', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${env.LINE_CHANNEL_ACCESS_TOKEN}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ to: userId, messages: texts.map((t) => ({ type: 'text', text: t })) }),
  });
  if (!res.ok) console.log('nudge push failed:', res.status);
}
 
/* ============================================================ 未返信の拾い直し */
/**
 * 1分ごとに呼ばれる。
 *
 * 相談者は、こちらの事情を知らない。返事が来なければ「無視された」だけが残る。
 * だから、届けられなかった相談をここで拾い直す。
 * AIにもう一度聞いて、プッシュで届ける。2回やっても駄目なときだけ、
 * 定型文に切り替えて、相談員に知らせる。
 */
async function retryPending(env) {
  const stat = { seen: 0, skipped: 0, recovered: 0, gaveUp: 0, failed: 0 };
 
  let list;
  try {
    list = await env.SESSIONS.list({ prefix: 'pending:' });
  } catch (err) {
    console.log('pending list failed:', String(err && err.message));
    return { ...stat, error: 'list failed' };
  }
  stat.seen = (list.keys || []).length;
 
  for (const k of list.keys || []) {
    try {
      const raw = await env.SESSIONS.get(k.name);
      if (!raw) continue;
 
      let p;
      try {
        p = JSON.parse(raw);
      } catch {
        await env.SESSIONS.delete(k.name);
        continue;
      }
 
      // まだ本線が送っている最中かもしれないので、少し置いてから拾う。
      // 一度手をつけたものは、生成が終わるまで触らない（二重送信を防ぐ）。
      const waitMs = Number(p.tries || 0) === 0 ? FIRST_PICKUP_MS : LOCK_MS;
      if (Date.now() - Number(p.at || 0) < waitMs) { stat.skipped++; continue; }
 
      const userId = k.name.slice('pending:'.length);
 
      if (Number(p.tries || 0) >= MAX_TRIES) {
        // ここが最後。何も届いていない状態で終わらせない。
        await pushToLine(env, userId, [FALLBACK]);
        await env.SESSIONS.delete(k.name);
        stat.gaveUp++;
        await postNotice(
          env,
          '⚠️ AIが' + MAX_TRIES + '回とも返せませんでした\n' +
            'LINEユーザーID：' + userId + '\n' +
            'この方には定型のご案内をお送りしました。内容は届いていません。\n' +
            'チャット画面からお声がけしてください。'
        );
        continue;
      }
 
      p.tries = Number(p.tries || 0) + 1;
      p.at = Date.now();
      await env.SESSIONS.put(k.name, JSON.stringify(p), { expirationTtl: PENDING_TTL });
 
      // まず、すでに書けている返事を取りにいく。
      // 間に合わなかっただけで、AIはもう書き終えていることが多い。
      // 聞き直すと、履歴に「相談者が見ていない返事」が増えてしまう。
      let answer = await fetchReadyAnswer(env, userId, p.text || '');
      let reused = true;
      if (!answer) {
        reused = false;
        answer = await askDify(env, userId, p.text || '');
      }
      if (!answer || answer === FALLBACK) continue; // 次の回でもう一度
      console.log('pending answer source:', reused ? 'ready' : 'regenerated');
 
      await pushToLine(env, userId, splitMessages(answer));
      await env.SESSIONS.delete(k.name);
      stat.recovered++;
      console.log('pending recovered:', userId, 'tries=', p.tries);
    } catch (err) {
      stat.failed++;
      console.log('pending retry failed:', k.name, String(err && err.message));
    }
  }
 
  return stat;
}
 


--56407dacb0c65e64e475d6edbeefa934bb11dea87c3883d273e8a71933ab--
