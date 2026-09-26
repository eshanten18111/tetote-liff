import json,subprocess,time
U="ord-test-0914-a"; OLD="42839bcf-abac-4037-9790-7b869a08109d"
p={"inputs":{},"query":"古い会話を掘り起こします","response_mode":"blocking","user":U,"conversation_id":OLD}
for a in range(5):
    r=subprocess.run(["curl","-sS","--max-time","300","-X","POST","https://api.dify.ai/v1/chat-messages",
      "-H","Content-Type: application/json","-d",json.dumps(p,ensure_ascii=False)],capture_output=True,text=True)
    try:
        d=json.loads(r.stdout); break
    except Exception:
        print("retry",a+1,r.stdout[:150]); time.sleep(5*(a+1))
else: raise SystemExit("giveup")
print("revived conv=",d.get("conversation_id"),"created_at=",d.get("created_at"))
print("err?",json.dumps(d,ensure_ascii=False)[:300] if "answer" not in d else "ok")
time.sleep(3)
r=subprocess.run(["curl","-sS","--max-time","60",f"https://api.dify.ai/v1/conversations?user={U}&limit=5"],capture_output=True,text=True)
for i,x in enumerate(json.loads(r.stdout).get("data",[])):
    mark="  <== 掘り起こした古い会話" if x.get("id")==OLD else ""
    print(f"[{i}] id={x.get('id')[:8]} created_at={x.get('created_at')} updated_at={x.get('updated_at')}{mark}")
