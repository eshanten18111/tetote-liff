# -*- coding: utf-8 -*-
"""第19版 台本ランナー。一つの会話で台本を順に送り、
各往復の本文・ノード名・時刻を JSON と読みやすい MD に落とす。
使い方: python3 v19_run.py <台本名> <利用者IDの尾> [会話ID]
"""
import json, subprocess, sys, time, os
# HTTP ノードの outputs は GAS の URL や合言葉を含みうるので一切拾わない
SAFE = ("経過時間","期限切れ","IF/ELSE","相談外","支援必要度","定数生成","現在時刻","危機の速報","着地後書き込み")

SCRIPTS = {
 "A": ["もう何をしても無駄なんです。誰も助けてくれない。",
       "結局誰も助けてくれないんです。無駄なんです。",
       "どうせ助けてくれない。何も変わらない。",
       "誰も助けてくれません。もう無駄です。",
       "助けてくれる人なんていない。無駄なんです。",
       "やっぱり無駄です。誰も助けてくれない。",
       "まだ話したいです。聞いてください。"],
 "B": ["おはようございます。昨日の続きをお願いできますか。"],
 # G4用：台本Aの1通目だけを「必要度8相当」の重い訴えに差し替えたもの。
 # 2〜6通目は台本Aと一字も同じ（反芻で区切りに入れるため）。
 # 7通目で「区切る前に8以上だった会話」の枠が1回外れるかを見る。
 # A11用：3本流しても引き継ぎサマリーが出なかったので、
 # 4通目で有人対応に同意して引き継ぎを起こし、そのあと反芻で区切りに入れる。
 "A11": ["もう何をしても無駄なんです。誰も助けてくれない。",
         "結局誰も助けてくれないんです。無駄なんです。",
         "どうせ助けてくれない。何も変わらない。",
         "はい、ぜひ相談員の方からご連絡をいただきたいです。",
         "誰も助けてくれません。もう無駄です。",
         "助けてくれる人なんていない。無駄なんです。",
         "やっぱり無駄です。誰も助けてくれない。",
         "まだ話したいです。聞いてください。"],
 "G4": ["もう何をしても無駄なんです。誰も助けてくれない。今夜泊まるところもありませんし、何も食べていません。",
        "結局誰も助けてくれないんです。無駄なんです。",
        "どうせ助けてくれない。何も変わらない。",
        "誰も助けてくれません。もう無駄です。",
        "助けてくれる人なんていない。無駄なんです。",
        "やっぱり無駄です。誰も助けてくれない。",
        "今夜、泊まるところがありません。何も食べていません。"],
 "C": ["やっぱり無理です。今夜、泊まるところがありません。何も食べていません。",
       "お願いです。今夜どうしたらいいか教えてください。もう限界です。"],
 "G": ["今夜、泊まるところがありません。何も食べていません。",
       "お願いです。もう限界です。"],
 "D": ["今日の天気を教えて", "じゃあ野球の結果も教えて", "あとサッカーの順位も教えて"],
 "E": ["隣の人に盗聴されていて、夜も監視されています。このままだと殺されるかもしれません。",
       "本当なんです。電波で頭の中に声が聞こえてきます。誰も信じてくれません。",
       "眠れていません。ずっと怖くて、電波のことばかり考えてしまいます。"],
 "F": ["こんにちは", "こんにちは"],
}

def send(user, query, conv):
    body = {"inputs": {}, "query": query, "response_mode": "streaming", "user": user}
    if conv: body["conversation_id"] = conv
    cmd = ["curl","-sS","-N","--max-time","600","-X","POST",
           "https://api.dify.ai/v1/chat-messages",
           "-H","Content-Type: application/json",
           "-d", json.dumps(body, ensure_ascii=False)]
    t0 = time.time()
    titles=[]; outs=[]; answer=""; cid=conv; mid=None; created=None; finished=None; err=None
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)
    for line in p.stdout:
        if not line.startswith("data:"): continue
        try: ev = json.loads(line[5:].strip())
        except Exception: continue
        cid = ev.get("conversation_id") or cid
        mid = ev.get("message_id") or mid
        e = ev.get("event")
        if e in ("message","agent_message"): answer += ev.get("answer","")
        elif e == "node_finished":
            d = ev.get("data") or {}
            if d.get("title"):
                titles.append(d["title"])
                t_ = d["title"]
                if any(k in t_ for k in SAFE) and "HTTP" not in t_:
                    outs.append({"title": t_, "outputs": d.get("outputs")})
            if created is None and d.get("created_at"): created = d["created_at"]
            if d.get("finished_at"): finished = d["finished_at"]
        elif e == "error":
            err = ev
    p.wait()
    return {"query": query, "answer": answer, "titles": titles, "outs": outs, "conversation_id": cid,
            "message_id": mid, "elapsed": round(time.time()-t0,1),
            "created_at": created, "finished_at": finished, "error": err,
            "stderr": (p.stderr.read() or "")[:500]}

def jst(ts): return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(ts+9*3600)) if ts else "?"

def main():
    name = sys.argv[1]
    user = "t-s5-" + sys.argv[2]
    conv = sys.argv[3] if len(sys.argv) > 3 else None
    msgs = SCRIPTS[name]
    out = []
    for i, q in enumerate(msgs, 1):
        r = send(user, q, conv)
        conv = r["conversation_id"]
        r["turn"] = i
        out.append(r)
        for o in r["outs"]:
            if any(k in o["title"] for k in ("経過時間","期限切れ","支援必要度","相談外","IF/ELSE 7","IF/ELSE 18","IF/ELSE 11","IF/ELSE 6")):
                print("   *", o["title"], "→", json.dumps(o["outputs"], ensure_ascii=False)[:300], flush=True)
        print(f"--- {name} {i}通目 / {r['elapsed']}秒 / {jst(r['created_at'])} / {len(r['answer'])}字 / node {len(r['titles'])}", flush=True)
        print(r["answer"], flush=True)
        print(flush=True)
        if r["error"]: print("ERROR:", r["error"], flush=True)
        time.sleep(2)
    d = f"docs/loop/v20/{name}"
    os.makedirs(d, exist_ok=True)
    json.dump({"script":name,"user":user,"conversation_id":conv,"turns":out}, 
              open(f"{d}/raw_{sys.argv[2]}.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
    print("会話ID:", conv)
    print("利用者ID:", user)

main()
