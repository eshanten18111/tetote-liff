# -*- coding: utf-8 -*-
"""第47版 台本N の続き：26通目で区切られたため、その次の回がどうなるかを1通だけ見る。"""
import json, subprocess, time, datetime
JST=datetime.timezone(datetime.timedelta(hours=9))
SAFE=("経過時間","期限切れ","IF/ELSE","相談外","支援必要度","定数生成","現在時刻","危機の速報",
      "着地後書き込み","採点","パラメータ抽出","返信整形","サマリー","まとめ","お知らせ")
def now(): return datetime.datetime.now(JST)
def send(user,query,conv):
    body={"inputs":{},"query":query,"response_mode":"streaming","user":user,"conversation_id":conv}
    cmd=["curl","-sS","-N","--max-time","600","-X","POST","https://api.dify.ai/v1/chat-messages",
         "-H","Content-Type: application/json","-d",json.dumps(body,ensure_ascii=False)]
    sent=now(); t0=time.time(); titles=[]; outs=[]; ans=""; cid=conv; created=None; err=None
    p=subprocess.Popen(cmd,stdout=subprocess.PIPE,text=True,bufsize=1)
    for line in p.stdout:
        if not line.startswith("data:"): continue
        try: ev=json.loads(line[5:].strip())
        except Exception: continue
        cid=ev.get("conversation_id") or cid
        if ev.get("event") in ("message","agent_message"): ans+=ev.get("answer","")
        elif ev.get("event")=="error": err=ev
        elif ev.get("event")=="node_finished":
            d=ev.get("data") or {}; t=d.get("title")
            if t:
                titles.append(t)
                if created is None and d.get("created_at"): created=d["created_at"]
                if any(k in t for k in SAFE) and "HTTP" not in t:
                    outs.append({"title":t,"outputs":d.get("outputs")})
    p.wait()
    return {"query":query,"answer":ans,"titles":titles,"outs":outs,"sent_jst":sent.isoformat(),
            "elapsed":round(time.time()-t0,1),"created_at":created,"conversation_id":cid,"error":err}
d=json.load(open("docs/loop/v50/N4/raw_N4_1.json",encoding="utf-8"))
rows=d["turns"]; t=rows[-1]["turn"]+1
r=send(d["user"],"もう少しだけ話してもいいですか。",d["conversation_id"]); r["turn"]=t; rows.append(r)
print(f"--- {t}通目（区切りの次） {r['sent_jst'][5:19]} / {r['elapsed']}秒 / {len(r['answer'])}字 / node{len(r['titles'])} / HTTP={[x for x in r['titles'] if 'HTTP' in x]}",flush=True)
print(r["answer"],flush=True)
print(); print("通ったノード:")
for x in r["titles"]: print("  ",x)
d["turns"]=rows; d["note"]="26通目で区切られたため、その次の回（27通目）を1通だけ足して確かめた"
json.dump(d,open("docs/loop/v50/N4/raw_N4_1.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
