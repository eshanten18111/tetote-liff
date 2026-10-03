import json, subprocess, sys, time
API="https://api.dify.ai/v1/chat-messages"
USER=sys.argv[1]
def send(q, conv=None):
    p={"inputs":{},"query":q,"response_mode":"blocking","user":USER}
    if conv: p["conversation_id"]=conv
    for attempt in range(5):
        r=subprocess.run(["curl","-sS","--max-time","300","-X","POST",API,
            "-H","Content-Type: application/json","-d",json.dumps(p,ensure_ascii=False)],
            capture_output=True,text=True)
        try:
            d=json.loads(r.stdout); break
        except Exception:
            print(f"  retry{attempt+1} RAW:",r.stdout[:200]); time.sleep(5*(attempt+1))
    else:
        raise SystemExit("give up")
    if "answer" not in d: print("ERR:",json.dumps(d,ensure_ascii=False)[:500]); raise SystemExit(1)
    return d
c=None
seq=["呼び名：順序テスト／年代：40代／都道府県：東京都","はい","つらいです","はい"]
for i,q in enumerate(seq,1):
    d=send(q,c); c=d["conversation_id"]
    print(f"--- turn{i} q={q!r} msg_id={d['id']} created_at={d['created_at']}")
    print("   ans:",d["answer"][:70].replace("\n","⏎"))
    time.sleep(1)
print("CONV="+c)
