import json, subprocess, time, statistics, datetime
U = "t-v16-" + time.strftime("%H%M%S")
WARM = ["呼び名：そうた／年代：30代／性別：男性／都道府県：徳島県／一番の悩み：仕事",
        "職場でうまくいかなくて、続けられるか不安です",
        "上司から強く当たられることが増えました",
        "夜も眠れず、朝になると体が重いです",
        "誰にも相談できていません"]
MEAS = ["家族にも心配をかけたくなくて","少しずつでも話せたらと思います","うまく言葉にできないです",
        "眠れない日が続いています","考えが堂々めぐりになります","少し楽になった気がします"]
def jst(ep): return datetime.datetime.utcfromtimestamp(ep+9*3600).strftime("%H:%M:%S.%f")[:-3]
conv=None
def send(q):
    global conv
    pl={"inputs":{},"query":q,"response_mode":"streaming","user":U}
    if conv: pl["conversation_id"]=conv
    cmd=["curl","-sS","-N","--max-time","360","-X","POST","https://api.dify.ai/v1/chat-messages",
         "-H","Content-Type: application/json","-d",json.dumps(pl,ensure_ascii=False)]
    t0=time.time(); t_first=t_last=t_end=None; after=[]
    p=subprocess.Popen(cmd,stdout=subprocess.PIPE,text=True,bufsize=1)
    for line in p.stdout:
        if not line.startswith("data:"): continue
        try: ev=json.loads(line[5:].strip())
        except Exception: continue
        now=time.time(); e=ev.get("event"); d=ev.get("data",{}) or {}
        conv=ev.get("conversation_id") or conv
        if e=="message":
            if t_first is None: t_first=now
            t_last=now
        elif e=="message_end": t_end=now
        elif e=="node_finished":
            if t_last is not None and now>t_last:
                after.append((d.get("title"), d.get("elapsed_time"), d.get("status"), now))
    p.wait()
    return {"t0":t0,"t_first":t_first,"t_last":t_last,"t_end":t_end,"after":after}

print("利用者:",U,flush=True)
for i,q in enumerate(WARM,1):
    send(q); print(f"  下ごしらえ {i}通目 完了",flush=True)
rows=[]
for i,q in enumerate(MEAS,1):
    r=send(q); r["turn"]=5+i; rows.append(r)
    print(f"  {5+i}通目 t0={jst(r['t0'])} t_first={r['t_first']-r['t0']:.1f} "
          f"t_last={r['t_last']-r['t0']:.1f} t_end={r['t_end']-r['t0']:.1f} 差={r['t_end']-r['t_last']:.1f}",flush=True)

print()
print("通目 | t_first-t0 | t_last-t0 | t_end-t0 | 差")
print("-----|------------|-----------|----------|------")
for r in rows:
    print(f"{r['turn']:<4} | {r['t_first']-r['t0']:10.1f} | {r['t_last']-r['t0']:9.1f} | "
          f"{r['t_end']-r['t0']:8.1f} | {r['t_end']-r['t_last']:5.1f}")
d=[r['t_end']-r['t_last'] for r in rows]
print(f"p50  | {'':10} | {'':9} | {'':8} | {statistics.median(d):5.1f}")
print(f"max  | {'':10} | {'':9} | {'':8} | {max(d):5.1f}")
print()
print("=== 差の中で動いたノード（t_last より後の node_finished） ===")
for r in rows:
    print(f"{r['turn']}通目 の差 {r['t_end']-r['t_last']:.1f}秒")
    if not r["after"]: print("   （なし）")
    for ttl,el,st,tm in r["after"]:
        print(f"   {ttl}  elapsed={el}  status={st}  受信 t_last+{tm-r['t_last']:.1f}秒")
print()
print("会話ID:",conv)
json.dump([{k:(v if k!='after' else [[a,b,c,round(dd,3)] for a,b,c,dd in v]) for k,v in r.items()} for r in rows],
          open("v16_rows.json","w"),ensure_ascii=False,indent=1,default=str)
