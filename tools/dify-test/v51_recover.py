# -*- coding: utf-8 -*-
# 0字だった回を、Dify に保存されている本文で補う（受信側の取りこぼしか、Dify側の失敗かを見分ける）
import json,os,sys,subprocess
S,CONV,USER=sys.argv[1],sys.argv[2],sys.argv[3]
KEY=os.environ.get("DIFY_API_KEY","dummy")
url=f"https://api.dify.ai/v1/messages?conversation_id={CONV}&user={USER}&limit=100"
out=subprocess.run(["curl","-sS","--max-time","60","-H",f"Authorization: Bearer {KEY}",url],capture_output=True,text=True).stdout
ms=json.loads(out)["data"]
p=f"docs/loop/v51/{S}/raw_{S}_1.json"
d=json.load(open(p,encoding="utf-8"))
byq={}
for m in ms: byq.setdefault(m.get("query",""),[]).append(m)
fixed=[]
for r in d["turns"]:
    if r["answer"]!="": continue
    cands=byq.get(r["query"],[])
    m=None
    for c in cands:
        if abs(c.get("created_at",0)-r.get("created_at",0))<=5: m=c;break
    if m is None and len(cands)==1: m=cands[0]
    print(f"--- {r['turn']}通目 query={r['query']!r}")
    if m is None:
        print("   Dify 側に見つかりませんでした"); continue
    print(f"   Dify の error = {m.get('error')!r} ／ 保存本文 {len(m.get('answer') or '')}字")
    if m.get("answer"):
        r["answer_streamed"]=""; r["answer"]=m["answer"]; fixed.append(r["turn"])
        print("   ↑ この本文で補いました")
if fixed:
    d["recovered_turns"]=fixed
    json.dump(d,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print("補った回:",fixed)
else:
    print("補える回はありませんでした")
