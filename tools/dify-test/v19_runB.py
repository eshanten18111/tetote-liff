# -*- coding: utf-8 -*-
"""台本B / D4 用。安全なノード（判定・分岐系）だけ outputs も記録する。
HTTP ノードの outputs は GAS の URL や合言葉を含みうるので一切拾わない。"""
import json, subprocess, sys, time, os
SAFE = ("経過時間", "期限切れ", "IF/ELSE", "相談外", "支援必要度", "定数生成", "現在時刻")
def send(user, query, conv):
    body = {"inputs": {}, "query": query, "response_mode": "streaming", "user": user,
            "conversation_id": conv}
    cmd = ["curl","-sS","-N","--max-time","600","-X","POST",
           "https://api.dify.ai/v1/chat-messages",
           "-H","Content-Type: application/json",
           "-d", json.dumps(body, ensure_ascii=False)]
    t0=time.time(); nodes=[]; answer=""; created=None
    p=subprocess.Popen(cmd,stdout=subprocess.PIPE,text=True,bufsize=1)
    for line in p.stdout:
        if not line.startswith("data:"): continue
        try: ev=json.loads(line[5:].strip())
        except Exception: continue
        e=ev.get("event")
        if e in ("message","agent_message"): answer+=ev.get("answer","")
        elif e=="node_finished":
            d=ev.get("data") or {}; t=d.get("title") or ""
            rec={"title":t}
            if created is None and d.get("created_at"): created=d["created_at"]
            if any(k in t for k in SAFE) and "HTTP" not in t:
                rec["outputs"]=d.get("outputs")
            nodes.append(rec)
    p.wait()
    return {"query":query,"answer":answer,"nodes":nodes,"elapsed":round(time.time()-t0,1),"created_at":created}

name, user, conv, q = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
r = send(user, q, conv)
print(f"--- {name} / {r['elapsed']}秒 / {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(r['created_at']+9*3600)) if r['created_at'] else '?'} / {len(r['answer'])}字 / node {len(r['nodes'])}")
print(r["answer"]); print()
for n in r["nodes"]:
    if "outputs" in n: print("  *", n["title"], "→", json.dumps(n["outputs"], ensure_ascii=False)[:400])
    else: print("   ", n["title"])
os.makedirs("docs/loop/v19/B", exist_ok=True)
json.dump({"script":name,"user":user,"conversation_id":conv,"turn":r},
          open(f"docs/loop/v19/B/raw_{name}.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
