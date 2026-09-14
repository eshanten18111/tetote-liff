import json,subprocess,time
API="https://api.dify.ai/v1/chat-messages"
cases=[
 ("存在しないUUID","ord-test-0914-a","00000000-0000-4000-8000-000000000000"),
 ("他人の会話ID","ord-test-0914-b","4e0a6763-3e8c-4223-8952-5b19813ae210"),
 ("UUIDでない文字列","ord-test-0914-a","not-a-uuid"),
 ("空文字（正常系の対照）","ord-test-0914-a",""),
]
for name,user,conv in cases:
    p={"inputs":{},"query":"テスト","response_mode":"blocking","user":user}
    if conv: p["conversation_id"]=conv
    r=subprocess.run(["curl","-sS","--max-time","120","-o","/dev/stdout","-w","\n<<HTTP %{http_code}>>","-X","POST",API,
      "-H","Content-Type: application/json","-d",json.dumps(p,ensure_ascii=False)],capture_output=True,text=True)
    out=r.stdout
    code=out.rsplit("<<HTTP ",1)[-1].rstrip(">>\n") if "<<HTTP " in out else "?"
    body=out.rsplit("\n<<HTTP ",1)[0][:200]
    hit = "conversation" in body.lower()
    print(f"--- {name}")
    print(f"    status={code}")
    print(f"    body={body}")
    print(f"    /conversation/i にあたる？ {hit}  -> looksStaleConversation={'true' if code=='404' or (code=='400' and hit) else 'false'}")
    time.sleep(2)
