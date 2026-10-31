import json,subprocess,threading,time
U="ord-test-0914-a"; C="4e0a6763-3e8c-4223-8952-5b19813ae210"
FALLBACK="いま混み合っています。少し待ってからもう一度お送りください。"
WANT="はい"
res={}
def fire():
    p={"inputs":{},"query":WANT,"response_mode":"blocking","user":U,"conversation_id":C}
    r=subprocess.run(["curl","-sS","--max-time","300","-X","POST","https://api.dify.ai/v1/chat-messages",
      "-H","Content-Type: application/json","-d",json.dumps(p,ensure_ascii=False)],capture_output=True,text=True)
    res["raw"]=r.stdout
t=threading.Thread(target=fire); t0=time.time(); t.start()
def scan(list_):
    for i in range(len(list_)-1,-1,-1):
        m=list_[i] or {}
        if str(m.get("query") or "").strip()!=WANT: continue
        a=str(m.get("answer") or "").strip()
        if not a or a==FALLBACK: return ("null(=まだ→再試行)", m.get("created_at"))
        return (a[:38].replace("\n","/"), m.get("created_at"))
    return ("一致なし", None)
while t.is_alive():
    r=subprocess.run(["curl","-sS","--max-time","30",
      f"https://api.dify.ai/v1/messages?conversation_id={C}&user={U}&limit=3"],capture_output=True,text=True)
    try: d=json.loads(r.stdout).get("data",[])
    except Exception: d=[]
    qs=[(str(x.get('query'))[:8],x.get('created_at')) for x in d]
    v,ca=scan(d)
    print(f"t+{time.time()-t0:5.1f}s window={qs} => worker取得: {v!r} (created_at={ca})",flush=True)
    time.sleep(2)
t.join()
try:
    d=json.loads(res["raw"]); print("\n実際の新しい返事:",d.get("answer","")[:38].replace("\n","/"),"created_at=",d.get("created_at"))
except Exception: print("RAW:",res.get("raw","")[:200])
