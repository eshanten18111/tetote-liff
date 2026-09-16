import json, subprocess, time
Q = "呼び名：めぐみ／年代：40代／性別：女性／都道府県：秋田県／一番の悩み：その他"
U = "t-v13-mark-" + time.strftime("%H%M%S")
cmd = ["curl","-sS","-N","--max-time","360","-X","POST","https://api.dify.ai/v1/chat-messages",
       "-H","Content-Type: application/json",
       "-d", json.dumps({"inputs":{},"query":Q,"response_mode":"streaming","user":U}, ensure_ascii=False)]
titles=[]; conv=None
t0=time.time()
p=subprocess.Popen(cmd,stdout=subprocess.PIPE,text=True,bufsize=1)
for line in p.stdout:
    if not line.startswith("data:"): continue
    try: ev=json.loads(line[5:].strip())
    except Exception: continue
    conv=ev.get("conversation_id") or conv
    if ev.get("event")=="node_finished":
        t=(ev.get("data") or {}).get("title")
        if t: titles.append(t)
p.wait()
print("利用者ID:",U)
print("会話ID  :",conv)
print("所要    :",round(time.time()-t0,1),"秒")
print("ノード数:",len(titles))
print()
print("=== node_finished の title（全部） ===")
for i,t in enumerate(titles,1): print(f"  {i:2}. {t}")
print()
hit=[t for t in titles if "／版" in t or "/版" in t]
print("=== 版の目印 ===")
print("  『／版』を含むノード名:", hit if hit else "（なし）")
print("  『／版 2026-09-16a』を含むか:", any("2026-09-16a" in t for t in titles))
open("titles.json","w",encoding="utf-8").write(json.dumps(titles,ensure_ascii=False,indent=1))
