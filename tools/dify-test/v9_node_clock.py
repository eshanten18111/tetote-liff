import json, subprocess, time, datetime
Q = "呼び名：そうた／年代：30代／性別：男性／都道府県：徳島県／一番の悩み：仕事"
TARGETS = {"HTTP リクエスト（カルテ照会）", "HTTP リクエスト（相談記録登録：初回受付）"}
def jst(ep):
    return datetime.datetime.utcfromtimestamp(ep + 9*3600).strftime("%H:%M:%S") if ep else "-"
rows = []
run_span = []
for n in range(1, 7):
    user = f"t-v9-{time.strftime('%H%M%S')}-{n}"
    cmd = ["curl","-sS","-N","--max-time","360","-X","POST","https://api.dify.ai/v1/chat-messages",
           "-H","Content-Type: application/json",
           "-d", json.dumps({"inputs":{},"query":Q,"response_mode":"streaming","user":user}, ensure_ascii=False)]
    t0 = time.time(); started = {}
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True, bufsize=1)
    for line in p.stdout:
        if not line.startswith("data:"): continue
        try: ev = json.loads(line[5:].strip())
        except Exception: continue
        e = ev.get("event"); d = ev.get("data", {}) or {}
        t = d.get("title")
        if t not in TARGETS: continue
        if e == "node_started":
            started[t] = d.get("created_at")
        elif e == "node_finished":
            out = d.get("outputs") or {}
            rows.append({"run": n, "node": t,
                "start_ep": started.get(t) or d.get("created_at"),
                "end_ep": d.get("finished_at") or d.get("created_at"),
                "elapsed": d.get("elapsed_time"),
                "status": out.get("status_code"),
                "node_status": d.get("status")})
    p.wait()
    wall = time.time() - t0
    run_span.append((t0, time.time()))
    print(f"実行{n} 完了 実測{wall:.1f}秒 利用者={user}", flush=True)

print()
print("回 | ノード                              | 始まった時刻 | 終わった時刻 | elapsed | status")
print("---|-------------------------------------|--------------|--------------|---------|-------")
for r in rows:
    short = "カルテ照会" if "カルテ" in r["node"] else "初回受付"
    print(f"{r['run']:<2} | {short:<35} | {jst(r['start_ep']):<12} | {jst(r['end_ep']):<12} | {str(r['elapsed'])[:6]:>7} | {r['status']}")
print()
print("測定した時間帯（JST）:", jst(int(run_span[0][0])), "〜", jst(int(run_span[-1][1])))
json.dump(rows, open("v9_rows.json","w"), ensure_ascii=False, indent=1)
