# -*- coding: utf-8 -*-
"""第41版 台本C の続き：同意が16通目（上限）に出たため、C-a／C-b／C-c だけを
同じ会話に足して送る。17〜19通目として記録する。"""
import json, subprocess, time, os, sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
SAFE = ("経過時間","期限切れ","IF/ELSE","相談外","支援必要度","定数生成","現在時刻","危機の速報",
        "着地後書き込み","採点","パラメータ抽出","返信整形","サマリー")
AFTER = ["ありがとうございます。いつごろ連絡をもらえますか。","夜はやっぱり眠れません。","母のことが心配です。"]
def send(user, query, conv):
    body={"inputs":{},"query":query,"response_mode":"streaming","user":user,"conversation_id":conv}
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
def grab(r,sub,key):
    for o in r["outs"]:
        if o["outputs"] and sub in o["title"] and key in o["outputs"]: return o["outputs"][key]
    return None
d=json.load(open("docs/loop/v41/C/raw_C_1.json",encoding="utf-8"))
user=d["user"]; conv=d["conversation_id"]; rows=d["turns"]
for i,q in enumerate(AFTER,17):
    r=send(user,q,conv); conv=r["conversation_id"]; r["turn"]=i; rows.append(r)
    print(f"--- {i}通目 送={q} / {r['elapsed']}秒 / {len(r['answer'])}字 / node{len(r['titles'])} / IF6={grab(r,'IF/ELSE 6','result')} / forced_close={grab(r,'返信整形','forced_close')!r} / phone_removed={grab(r,'返信整形','phone_removed')!r} / HTTP={[t for t in r['titles'] if 'HTTP' in t]}",flush=True)
    print(r["answer"],flush=True); print(flush=True)
    time.sleep(1)
d["turns"]=rows; d["note"]="同意が16通目（上限）に出たため、C-a〜C-c を17〜19通目として足した"
json.dump(d,open("docs/loop/v41/C/raw_C_1.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("会話ID:",conv,"／全",len(rows),"往復")
