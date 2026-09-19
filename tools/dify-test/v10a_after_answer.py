import json, subprocess, time, statistics
Q = "呼び名：そうた／年代：30代／性別：男性／都道府県：徳島県／一番の悩み：仕事"
rows=[]
for n in range(1,7):
    user=f"t-v10a-{time.strftime('%H%M%S')}-{n}"
    cmd=["curl","-sS","-N","--max-time","360","-X","POST","https://api.dify.ai/v1/chat-messages",
         "-H","Content-Type: application/json",
         "-d",json.dumps({"inputs":{},"query":Q,"response_mode":"streaming","user":user},ensure_ascii=False)]
    t0=time.time(); t_first=t_last=t_end=t_ans=None; after=[]
    p=subprocess.Popen(cmd,stdout=subprocess.PIPE,text=True,bufsize=1)
    for line in p.stdout:
        if not line.startswith("data:"): continue
        try: ev=json.loads(line[5:].strip())
        except Exception: continue
        now=time.time(); e=ev.get("event"); d=ev.get("data",{}) or {}
        if e=="message":
            if t_first is None: t_first=now
            t_last=now
        elif e=="message_end":
            t_end=now
        elif e=="node_finished":
            ttl=d.get("title")
            if ttl=="回答": t_ans=now
            if t_last is not None and now>t_last:
                after.append((ttl, d.get("elapsed_time")))
    p.wait()
    rows.append({"run":n,"user":user,"t0":t0,"t_first":t_first,"t_last":t_last,
                 "t_end":t_end,"t_ans":t_ans,"after":after})
    print(f"実行{n} 完了 t_last-t0={t_last-t0:.1f} t_end-t0={t_end-t0:.1f} 差={t_end-t_last:.1f}",flush=True)

print()
print("回 | t_last-t0 | t_end-t0 | 差(t_end-t_last) | 回答ノード終了-t0")
print("---|-----------|----------|------------------|------------------")
for r in rows:
    ans = f"{r['t_ans']-r['t0']:.1f}" if r['t_ans'] else "-"
    print(f"{r['run']:<2} | {r['t_last']-r['t0']:9.1f} | {r['t_end']-r['t0']:8.1f} | {r['t_end']-r['t_last']:16.1f} | {ans:>17}")
d=[r['t_end']-r['t_last'] for r in rows]
tl=[r['t_last']-r['t0'] for r in rows]; te=[r['t_end']-r['t0'] for r in rows]
print(f"p50| {statistics.median(tl):9.1f} | {statistics.median(te):8.1f} | {statistics.median(d):16.1f} |")
print(f"max| {max(tl):9.1f} | {max(te):8.1f} | {max(d):16.1f} |")
print()
print("=== 差の中で動いていたノード（t_last より後に node_finished が来たもの） ===")
for r in rows:
    print(f"回{r['run']} の差 {r['t_end']-r['t_last']:.1f}秒 の中身")
    if not r["after"]: print("   （なし）")
    for ttl,el in r["after"]: print(f"   {ttl}  {el}")
json.dump([{k:v for k,v in r.items()} for r in rows], open("a_rows.json","w"), ensure_ascii=False, indent=1)
