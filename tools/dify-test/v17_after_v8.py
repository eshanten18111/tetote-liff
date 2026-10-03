import json, subprocess, time, statistics
Q = "呼び名：そうた／年代：30代／性別：男性／都道府県：徳島県／一番の悩み：仕事"
FOLLOW = ["最近、眠れない日が続いています","仕事のことで気持ちが重いです",
          "人に話すのは初めてです","少し楽になりました"]
KARTE="HTTP リクエスト（カルテ照会）"; INIT="HTTP リクエスト（相談記録登録：初回受付）"
def send(q, user, conv=None):
    pl={"inputs":{},"query":q,"response_mode":"streaming","user":user}
    if conv: pl["conversation_id"]=conv
    cmd=["curl","-sS","-N","--max-time","360","-X","POST","https://api.dify.ai/v1/chat-messages",
         "-H","Content-Type: application/json","-d",json.dumps(pl,ensure_ascii=False)]
    t0=time.time(); t_last=t_end=None; gas={}; ans=[]; cid=conv
    p=subprocess.Popen(cmd,stdout=subprocess.PIPE,text=True,bufsize=1)
    for line in p.stdout:
        if not line.startswith("data:"): continue
        try: ev=json.loads(line[5:].strip())
        except Exception: continue
        now=time.time(); e=ev.get("event"); d=ev.get("data",{}) or {}
        cid=ev.get("conversation_id") or cid
        if e=="message": t_last=now; ans.append(ev.get("answer",""))
        elif e=="message_end": t_end=now
        elif e=="node_finished" and d.get("title") in (KARTE,INIT):
            o=d.get("outputs") or {}
            gas[d["title"]]={"el":d.get("elapsed_time"),"status":o.get("status_code"),
                             "body":str(o.get("body"))[:300],"node":d.get("status")}
    p.wait()
    return {"t0":t0,"t_last":t_last,"t_end":t_end,"gas":gas,"cid":cid,"ans":"".join(ans)}

rows=[]
for n in range(1,7):
    u=f"t-v17-{time.strftime('%H%M%S')}-{n}"
    r=send(Q,u); r["run"]=n; r["user"]=u; rows.append(r)
    k=r["gas"].get(KARTE,{}); i=r["gas"].get(INIT,{})
    print(f"実行{n} t_last={r['t_last']-r['t0']:.1f} t_end={r['t_end']-r['t0']:.1f} "
          f"カルテ={k.get('el')}/{k.get('status')} 初回受付={i.get('el')}/{i.get('status')} 返事={len(r['ans'])}字",flush=True)

print()
print("【1通目・6回】")
print("回 | t_last-t0 | t_end-t0 | カルテ照会(秒/status) | 初回受付(秒/status)")
for r in rows:
    k=r["gas"].get(KARTE,{}); i=r["gas"].get(INIT,{})
    print(f"{r['run']:<2} | {r['t_last']-r['t0']:9.1f} | {r['t_end']-r['t0']:8.1f} | "
          f"{str(k.get('el'))[:6]:>8} / {k.get('status')}  | {str(i.get('el'))[:6]:>8} / {i.get('status')}")
tl=[r['t_last']-r['t0'] for r in rows]; te=[r['t_end']-r['t0'] for r in rows]
kl=[r['gas'].get(KARTE,{}).get('el') for r in rows]; il=[r['gas'].get(INIT,{}).get('el') for r in rows]
print(f"p50| {statistics.median(tl):9.1f} | {statistics.median(te):8.1f} | "
      f"{statistics.median([x for x in kl if x is not None]):8.3f}    | {statistics.median([x for x in il if x is not None]):8.3f}")
print(f"max| {max(tl):9.1f} | {max(te):8.1f} | {max(x for x in kl if x is not None):8.3f}    | {max(x for x in il if x is not None):8.3f}")
o24=sum(1 for x in tl if x>24)
print(f"\n24秒を超えた回 … {o24}/6（over24pct={round(o24/6*100)}）")
print()
print("=== 初回受付の body（先頭300字・via/queued を見る） ===")
for r in rows:
    print(f"  実行{r['run']}: {r['gas'].get(INIT,{}).get('body')}")
print()
print("=== カルテ照会の body ===")
for r in rows:
    print(f"  実行{r['run']}: {r['gas'].get(KARTE,{}).get('body')}")
print()
print("=== 0字の返事 ===")
z=[r['run'] for r in rows if len(r['ans'])==0]
print("  ", z if z else "なし")

print()
print("【2〜5通目】（実行1の会話を伸ばす）")
conv=rows[0]["cid"]; u=rows[0]["user"]
print("通目 | t_last-t0 | 初回受付(秒/status)")
f=[]
for j,q in enumerate(FOLLOW,2):
    r=send(q,u,conv); conv=r["cid"]
    i=r["gas"].get(INIT,{})
    print(f"{j:<4} | {r['t_last']-r['t0']:9.1f} | {str(i.get('el'))[:6]:>8} / {i.get('status')}   返事={len(r['ans'])}字",flush=True)
    f.append({"turn":j,"t_last":r['t_last']-r['t0'],"init":i,"len":len(r['ans'])})
json.dump({"first":[{k:v for k,v in r.items() if k!='ans'} for r in rows],"follow":f},
          open("v15_rows.json","w"),ensure_ascii=False,indent=1,default=str)
