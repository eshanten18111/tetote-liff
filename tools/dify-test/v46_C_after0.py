# -*- coding: utf-8 -*-
"""第46版 台本C の続き：0時を過ぎてから3往復送り、C-3（追記が動くか）を確かめる。
27〜29通目として同じ会話に足す（上限29往復の内側）。"""
import json, subprocess, time, os, datetime
JST=datetime.timezone(datetime.timedelta(hours=9))
SAFE=("経過時間","期限切れ","IF/ELSE","相談外","支援必要度","定数生成","現在時刻","危機の速報",
      "着地後書き込み","採点","パラメータ抽出","返信整形","サマリー","まとめ","お知らせ")
MSGS=["昨日は雨が降っていました。","テレビはあまり見なくなりました。","母が好きだった花が咲いています。"]
def now(): return datetime.datetime.now(JST)
def hm(d): return d.strftime("%m/%d %H:%M:%S")
def send(user,query,conv):
    body={"inputs":{},"query":query,"response_mode":"streaming","user":user,"conversation_id":conv}
    cmd=["curl","-sS","-N","--max-time","600","-X","POST","https://api.dify.ai/v1/chat-messages",
         "-H","Content-Type: application/json","-d",json.dumps(body,ensure_ascii=False)]
    sent=now(); t0=time.time(); titles=[]; outs=[]; ans=""; cid=conv; created=None
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
    return {"query":query,"answer":ans,"titles":titles,"outs":outs,"sent_jst":sent.isoformat(),
            "elapsed":round(time.time()-t0,1),"created_at":created,"conversation_id":cid}
def grab(r,sub,key):
    for o in r["outs"]:
        if o["outputs"] and sub in o["title"] and key in o["outputs"]: return o["outputs"][key]
    return None
d=json.load(open("docs/loop/v46/C/raw_C_1.json",encoding="utf-8"))
user=d["user"]; conv=d["conversation_id"]; rows=d["turns"]
mid=(now()+datetime.timedelta(days=1)).replace(hour=0,minute=0,second=20,microsecond=0)
if now().hour==0: mid=now()
wait=(mid-now()).total_seconds()
print(f"[いま] {hm(now())} JST ／ 0時20秒まで {int(max(wait,0))} 秒待ちます",flush=True)
if wait>0:
    if wait>3600:
        print("★ 0時まで1時間以上あります。流さずに終わります。",flush=True); raise SystemExit(0)
    time.sleep(wait)
for i,q in enumerate(MSGS,rows[-1]["turn"]+1):
    r=send(user,q,conv); conv=r["conversation_id"]; r["turn"]=i; rows.append(r)
    add="あり" if any("追記" in t and "HTTP" in t for t in r["titles"]) else "★なし"
    print(f"--- {i}通目 送={q} / {hm(datetime.datetime.fromisoformat(r['sent_jst']))} JST / {r['elapsed']}秒 / {len(r['answer'])}字 / node{len(r['titles'])} / IF7={grab(r,'IF/ELSE 7','result')} / 追記={add} / HTTP={[t for t in r['titles'] if 'HTTP' in t]}",flush=True)
    print(r["answer"][:200],flush=True); print(flush=True)
    time.sleep(1)
d["turns"]=rows; d["note"]="26往復が23:46に終わり0時をまたがなかったため、0時を過ぎてから27〜29通目を足した"
json.dump(d,open("docs/loop/v46/C/raw_C_1.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("会話ID:",conv,"／全",len(rows),"往復")
print(f"[終了] {hm(now())} JST",flush=True)
