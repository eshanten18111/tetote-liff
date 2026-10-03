import json, subprocess, time
Q = "呼び名：めぐみ／年代：40代／性別：女性／都道府県：秋田県／一番の悩み：その他"
U = "t-v-mark-" + time.strftime("%H%M%S")
cmd = ["curl","-sS","-N","--max-time","360","-X","POST","https://api.dify.ai/v1/chat-messages",
       "-H","Content-Type: application/json",
       "-d", json.dumps({"inputs":{},"query":Q,"response_mode":"streaming","user":U}, ensure_ascii=False)]
titles=[]; outs={}
p=subprocess.Popen(cmd,stdout=subprocess.PIPE,text=True,bufsize=1)
for line in p.stdout:
    if not line.startswith("data:"): continue
    try: ev=json.loads(line[5:].strip())
    except Exception: continue
    if ev.get("event")=="node_finished":
        d=ev.get("data") or {}
        t=d.get("title")
        if t:
            titles.append(t)
            if "現在時刻" in t: outs[t]=d.get("outputs")
p.wait()
print("利用者ID:",U)
print("版の目印:",[t for t in titles if "／版" in t])
print("2026-09-19v を含むか:", any("2026-09-19v" in t.lower() for t in titles))
print("着地アラートSlack通知 があるか:", any("着地アラート" in t for t in titles))
for k,v in outs.items(): print(k,"→",json.dumps(v,ensure_ascii=False))
