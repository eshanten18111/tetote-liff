import json, subprocess, time, statistics
U = "t-v10b-" + time.strftime("%H%M%S")
WARM = ["呼び名：そうた／年代：30代／性別：男性／都道府県：徳島県／一番の悩み：仕事",
        "職場でうまくいかなくて、続けられるか不安です",
        "上司から強く当たられることが増えました",
        "夜も眠れず、朝になると体が重いです",
        "誰にも相談できていません"]
MEAS = ["家族にも心配をかけたくなくて","少しずつでも話せたらと思います","うまく言葉にできないです",
        "今日はここまでにします","聞いてもらえて助かりました","またお願いするかもしれません"]
conv=None
def send(q, mode):
    global conv
    pl={"inputs":{},"query":q,"response_mode":mode,"user":U}
    if conv: pl["conversation_id"]=conv
    cmd=["curl","-sS","-N","--max-time","360","-X","POST","https://api.dify.ai/v1/chat-messages",
         "-H","Content-Type: application/json","-d",json.dumps(pl,ensure_ascii=False)]
    t0=time.time()
    if mode=="blocking":
        r=subprocess.run(cmd,capture_output=True,text=True); el=time.time()-t0
        try: d=json.loads(r.stdout); conv=d.get("conversation_id") or conv
        except Exception: return {"mode":mode,"ok":False,"raw":r.stdout[:80],"el":el}
        return {"mode":mode,"ok":True,"el":el}
    t_last=t_end=None
    p=subprocess.Popen(cmd,stdout=subprocess.PIPE,text=True,bufsize=1)
    for line in p.stdout:
        if not line.startswith("data:"): continue
        try: ev=json.loads(line[5:].strip())
        except Exception: continue
        now=time.time(); conv=ev.get("conversation_id") or conv
        if ev.get("event")=="message": t_last=now
        elif ev.get("event")=="message_end": t_end=now
    p.wait()
    return {"mode":mode,"ok":True,"t_last":t_last-t0,"t_end":t_end-t0}

print("利用者:",U)
for i,q in enumerate(WARM,1):
    r=send(q,"streaming"); print(f"  下ごしらえ {i}通目 完了",flush=True)
res=[]
for i,q in enumerate(MEAS,1):
    mode = "blocking" if i%2==1 else "streaming"   # 交互に投げて時間帯の偏りを避ける
    r=send(q,mode); r["turn"]=5+i; res.append(r)
    print(f"  {5+i}通目 {mode}: {r}",flush=True)
print()
print("=== B の結果 ===")
bl=[r["el"] for r in res if r["mode"]=="blocking" and r.get("ok")]
st_end=[r["t_end"] for r in res if r["mode"]=="streaming" and r.get("ok")]
st_last=[r["t_last"] for r in res if r["mode"]=="streaming" and r.get("ok")]
print("blocking の所要        :", [round(x,1) for x in bl], " p50", round(statistics.median(bl),1) if bl else "-")
print("streaming の t_end-t0  :", [round(x,1) for x in st_end], " p50", round(statistics.median(st_end),1) if st_end else "-")
print("streaming の t_last-t0 :", [round(x,1) for x in st_last]," p50", round(statistics.median(st_last),1) if st_last else "-")
print("会話ID:",conv)
json.dump(res, open("b_rows.json","w"), ensure_ascii=False, indent=1)
