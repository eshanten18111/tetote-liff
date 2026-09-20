import json, subprocess, sys, time, os
SAFE=("経過時間","期限切れ","IF/ELSE","相談外","支援必要度","定数生成","現在時刻","危機の速報","着地後書き込み","採点","パラメータ抽出","返信整形","サマリー")
user,conv,q,turn=sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4])
body={"inputs":{},"query":q,"response_mode":"streaming","user":user,"conversation_id":conv}
cmd=["curl","-sS","-N","--max-time","600","-X","POST","https://api.dify.ai/v1/chat-messages","-H","Content-Type: application/json","-d",json.dumps(body,ensure_ascii=False)]
t0=time.time();titles=[];outs=[];ans="";created=None
p=subprocess.Popen(cmd,stdout=subprocess.PIPE,text=True,bufsize=1)
for line in p.stdout:
    if not line.startswith("data:"): continue
    try: ev=json.loads(line[5:].strip())
    except Exception: continue
    if ev.get("event") in ("message","agent_message"): ans+=ev.get("answer","")
    elif ev.get("event")=="node_finished":
        d=ev.get("data") or {}; t=d.get("title")
        if t:
            titles.append(t)
            if created is None and d.get("created_at"): created=d["created_at"]
            if any(k in t for k in SAFE) and "HTTP" not in t: outs.append({"title":t,"outputs":d.get("outputs")})
p.wait()
r={"query":q,"answer":ans,"titles":titles,"outs":outs,"elapsed":round(time.time()-t0,1),"created_at":created,"turn":turn}
os.makedirs("docs/loop/v36/L",exist_ok=True)
json.dump({"script":"L","user":user,"conversation_id":conv,"turns":[r]},open(f"docs/loop/v36/L/raw_L_{turn}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
hs=[o["outputs"] for o in outs if "返信整形" in o["title"] and o["outputs"]]
ex=[o["outputs"] for o in outs if "期限切れ" in o["title"] and o["outputs"]]
sn=[o["outputs"] for o in outs if "支援必要度" in o["title"] and o["outputs"]]
i6=[o["outputs"] for o in outs if "IF/ELSE 6" in o["title"] and o["outputs"]]
print(f"--- {turn}通目 / {r['elapsed']}秒 / {len(ans)}字 / node{len(titles)}")
print("  forced_close =",repr(hs[0].get("forced_close") if hs else "?"))
print("  length_alerted =",repr(ex[0].get("length_alerted") if ex else "?"))
print("  IF/ELSE 6 =",(i6[0].get("result") if i6 else "-"))
print("  支援必要度ノード:",json.dumps(sn[0],ensure_ascii=False) if sn else "-")
print("  サマリーHTTP:",[x for x in titles if "サマリー" in x and "HTTP" in x] or "なし")
print("  Slack:",[x for x in titles if "Slack" in x] or "なし")
print(); print(ans)
