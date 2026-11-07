# -*- coding: utf-8 -*-
"""第39版 台本C：同意のあとの流れ。最大16往復。
1〜6通目は決まった文。7通目以降はAIの返事を見て返す。
IF/ELSE 6 が true になった回（同意の回）のあと、C-a／C-b／C-c を送って終わり。"""
import json, subprocess, time, os, re
SAFE = ("経過時間","期限切れ","IF/ELSE","相談外","支援必要度","定数生成","現在時刻","危機の速報",
        "着地後書き込み","採点","パラメータ抽出","返信整形","サマリー")
FIXED = ["母の介護をひとりでしています。最近、母に強く当たってしまいます。",
         "手が出そうになることもあって、自分が怖いです。",
         "誰にも相談したことはありません。兄弟もいませんし、ケアマネさんもいません。",
         "母は要介護の認定も受けていないと思います。",
         "夜も何度も起こされて、眠れていません。",
         "どこに言えばいいのかも分からなくて。"]
SHORT = ["つらいです。","母は83歳です。","昼間も家にいます。","仕事は今はしていません。",
         "自分の食事も作れていません。","助けてほしいです。","どうしたらいいか分かりません。"]
AFTER = ["ありがとうございます。いつごろ連絡をもらえますか。","夜はやっぱり眠れません。","母のことが心配です。"]

def send(user, query, conv):
    body={"inputs":{},"query":query,"response_mode":"streaming","user":user}
    if conv: body["conversation_id"]=conv
    cmd=["curl","-sS","-N","--max-time","600","-X","POST","https://api.dify.ai/v1/chat-messages",
         "-H","Content-Type: application/json","-d",json.dumps(body,ensure_ascii=False)]
    t0=time.time(); titles=[]; outs=[]; ans=""; cid=conv; created=None
    p=subprocess.Popen(cmd,stdout=subprocess.PIPE,text=True,bufsize=1)
    for line in p.stdout:
        if not line.startswith("data:"): continue
        try: ev=json.loads(line[5:].strip())
        except Exception: continue
        cid=ev.get("conversation_id") or cid
        if ev.get("event") in ("message","agent_message"): ans+=ev.get("answer","")
        elif ev.get("event")=="node_finished":
            d=ev.get("data") or {}; t=d.get("title")
            if t:
                titles.append(t)
                if created is None and d.get("created_at"): created=d["created_at"]
                if any(k in t for k in SAFE) and "HTTP" not in t:
                    outs.append({"title":t,"outputs":d.get("outputs")})
    p.wait()
    return {"query":query,"answer":ans,"titles":titles,"outs":outs,
            "elapsed":round(time.time()-t0,1),"created_at":created,"conversation_id":cid}

def grab(r,sub,key,exact=False):
    for o in r["outs"]:
        if not o["outputs"]: continue
        if (o["title"]==sub) if exact else (sub in o["title"]):
            if key in o["outputs"]: return o["outputs"][key]
    return None

user="t-39-C"; conv=None; rows=[]; prev=""; si=0; stop=""
consent_turn=None; after_i=0
for turn in range(1,17):
    if turn<=6:
        q=FIXED[turn-1]
    elif consent_turn is not None:
        if after_i>=len(AFTER): stop="C-a〜C-c を送り終えました"; break
        q=AFTER[after_i]; after_i+=1
    elif any(k in prev for k in ("この内容で","内容でよろしい","下記の内容","以下の内容","お間違いない","この内容をお伝え")):
        q="この内容で大丈夫です。"
    elif ("相談員" in prev) and any(k in prev for k in ("いかがでしょうか","よろしいでしょうか","おつなぎ","つなぐ","おつなぎしても","ご連絡")):
        q="はい、お願いします。"
    elif "ずれ" in prev:
        q="ずれていません。"
    else:
        q=SHORT[si%len(SHORT)]; si+=1
    r=send(user,q,conv); conv=r["conversation_id"]; r["turn"]=turn; rows.append(r); prev=r["answer"]
    pa=[o["outputs"] for o in r["outs"] if o["title"]=="パラメータ抽出" and o["outputs"]]
    i6=grab(r,"IF/ELSE 6","result")
    fc=grab(r,"返信整形","forced_close"); ph=grab(r,"返信整形","phone_removed")
    mark=[t for t in r["titles"] if "定数生成" in t]
    http=[t for t in r["titles"] if "HTTP" in t]
    print(f"--- {turn}通目 送={q} / {r['elapsed']}秒 / {len(r['answer'])}字 / node{len(r['titles'])} / 版={mark} / IF6={i6} / forced_close={fc!r} / phone_removed={ph!r} / need={(pa[0].get('support_need') if pa else '-')} / HTTP={http}",flush=True)
    print(r["answer"],flush=True); print(flush=True)
    if turn==1:
        em=(pa[0].get("error_message") if pa else "取れず")
        print(f"[1往復目の確認] error_message={em!r} / 版の目印={mark}",flush=True)
        if em: stop="429/エラー"; print("★ error_message が空ではありません。止めます。",flush=True); break
        if not any("2026-09-20e" in t for t in mark):
            stop="版ちがい"; print("★ 版の目印が 2026-09-20e ではありません。止めます。",flush=True); break
    if i6 is True and consent_turn is None:
        consent_turn=turn
        print(f"★ {turn}通目で IF/ELSE 6 が true になりました（同意の回）。ここから C-a／C-b／C-c を送ります。",flush=True)
        for u in re.findall(r"https?://\S+", r["answer"]):
            clean = bool(re.fullmatch(r"https://[A-Za-z0-9._~:/?#\[\]@!$&'()*+,;=%-]+", u)) and not u.endswith((".","、","。",")","）"))
            print(f"[リンク点検] 長さ{len(u)}字 / 形={'ふつう' if clean else '★あやしい'} / 先頭20字={u[:20]}…",flush=True)
    time.sleep(1)
print("止めた理由:",stop or "16往復を流しきりました")
print("同意の回:",consent_turn)
os.makedirs("docs/loop/v39/C",exist_ok=True)
json.dump({"script":"C","user":user,"conversation_id":conv,"consent_turn":consent_turn,"turns":rows},
          open("docs/loop/v39/C/raw_C_1.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("会話ID:",conv)
