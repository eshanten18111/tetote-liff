import json, subprocess, time
Q = "呼び名：めぐみ／年代：40代／性別：女性／都道府県：秋田県／一番の悩み：その他"
U = "t-s5-" + time.strftime("%H%M%S") + "-mark19"
cmd = ["curl","-sS","-N","--max-time","360","-X","POST","https://api.dify.ai/v1/chat-messages",
       "-H","Content-Type: application/json",
       "-d", json.dumps({"inputs":{},"query":Q,"response_mode":"streaming","user":U}, ensure_ascii=False)]
titles=[]; conv=None; created=None
t0=time.time()
p=subprocess.Popen(cmd,stdout=subprocess.PIPE,text=True,bufsize=1)
for line in p.stdout:
    if not line.startswith("data:"): continue
    try: ev=json.loads(line[5:].strip())
    except Exception: continue
    conv=ev.get("conversation_id") or conv
    if ev.get("event")=="node_finished":
        d=ev.get("data") or {}
        t=d.get("title")
        if t: titles.append(t)
        if created is None and d.get("created_at"): created=d["created_at"]
p.wait()
print("利用者ID:",U); print("会話ID  :",conv)
print("Dify側の時刻(JST):", time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(created+9*3600)) if created else "?")
print("コンテナ時刻(JST):", time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time()+9*3600)))
print("所要    :",round(time.time()-t0,1),"秒"); print("ノード数:",len(titles)); print()
for i,t in enumerate(titles,1): print(f"  {i:2}. {t}")
print()
hit=[t for t in titles if "／版" in t or "/版" in t]
print("版の目印:", hit if hit else "（なし）")
print("2026-09-17K を含むか:", any("2026-09-17K" in t for t in titles))
print("2026-09-17k を含むか:", any("2026-09-17k" in t for t in titles))
