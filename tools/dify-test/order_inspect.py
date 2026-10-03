import json, subprocess, sys
U=sys.argv[1]; C=sys.argv[2]
def get(url):
    r=subprocess.run(["curl","-sS","--max-time","60",url],capture_output=True,text=True)
    return json.loads(r.stdout)

print("========== GET /messages (limit=20) ==========")
m=get(f"https://api.dify.ai/v1/messages?conversation_id={C}&user={U}&limit=20")
data=m.get("data",[])
print("has_more=",m.get("has_more"),"limit=",m.get("limit"),"count=",len(data))
for i,x in enumerate(data):
    print(f"[{i}] created_at={x.get('created_at')} q={str(x.get('query'))[:24]!r} a={str(x.get('answer'))[:40].replace(chr(10),'/')!r}")
ts=[x.get("created_at") for x in data]
print("ORDER:", "OLDEST_FIRST(末尾が最新)" if ts==sorted(ts) else ("NEWEST_FIRST(先頭が最新)" if ts==sorted(ts,reverse=True) else "UNSORTED"))

print()
print("========== worker fetchReadyAnswer の走査を再現 (want='はい') ==========")
FALLBACK="いま混み合っています。少し待ってからもう一度お送りください。"
want="はい"
# worker: for (let i = list.length - 1; i >= 0; i--)
for i in range(len(data)-1,-1,-1):
    mm=data[i] or {}
    if str(mm.get("query") or "").strip()!=want: continue
    ans=str(mm.get("answer") or "").strip()
    print(f"  -> 拾ったのは index={i} created_at={mm.get('created_at')}")
    print(f"     answer[:60]={ans[:60].replace(chr(10),'/')!r}")
    break
else:
    print("  -> 一致なし")
hits=[(i,x.get("created_at")) for i,x in enumerate(data) if str(x.get("query") or "").strip()==want]
print("  「はい」の全出現:",hits)
if hits:
    newest=max(hits,key=lambda t:t[1])
    print("  本当の最新は index=",newest[0],"created_at=",newest[1])

print()
print("========== GET /conversations (limit=5, sort_by未指定) ==========")
c=get(f"https://api.dify.ai/v1/conversations?user={U}&limit=5")
cd=c.get("data",[])
for i,x in enumerate(cd):
    print(f"[{i}] id={x.get('id')} created_at={x.get('created_at')} updated_at={x.get('updated_at')} name={str(x.get('name'))[:20]!r}")
if cd:
    print("target_conv=",C)
    print("list[0] == target ?", cd[0].get("id")==C)
    ua=[x.get("updated_at") for x in cd]
    ca=[x.get("created_at") for x in cd]
    print("updated_at order:", "DESC(新しい順)" if ua==sorted(ua,reverse=True) else ("ASC(古い順)" if ua==sorted(ua) else "UNSORTED"))
    print("created_at order:", "DESC(新しい順)" if ca==sorted(ca,reverse=True) else ("ASC(古い順)" if ca==sorted(ca) else "UNSORTED"))
