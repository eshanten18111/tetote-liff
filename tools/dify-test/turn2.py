#!/usr/bin/env python3
"""2通目以降を測る。GASノードが走る往復と走らない往復を分けて集計する。
初回受付は最初の5往復まで走るので、GASを完全に通らないのは6往復目以降。
"""
import json, os, statistics, subprocess, sys, time

API = "https://api.dify.ai/v1/chat-messages"
KARTE = "HTTP リクエスト（カルテ照会）"
INTAKE = "HTTP リクエスト（相談記録登録：初回受付）"
TURNS = [
 "呼び名：そうた／年代：30代／性別：男性／都道府県：徳島県／一番の悩み：仕事",
 "職場でうまくいかず、続けられるか不安です",
 "上司から強く当たられることが増えました",
 "夜も眠れず、朝になると体が重いです",
 "誰にも相談できていません",
 "家族にも心配をかけたくなくて",
 "このまま働き続けられるのか分かりません",
 "少し楽になる方法があれば知りたいです",
]

def turn(user, q, conv):
    payload = {"inputs": {}, "query": q, "response_mode": "streaming", "user": user}
    if conv:
        payload["conversation_id"] = conv
    cmd = ["curl", "-sS", "-N", "--max-time", "360", "-X", "POST", API,
           "-H", "Content-Type: application/json"]
    key = os.environ.get("DIFY_API_KEY")
    if key:
        cmd += ["-H", f"Authorization: Bearer {key}"]
    cmd += ["-d", json.dumps(payload, ensure_ascii=False)]
    t0 = time.time(); nodes = {}; cid = conv
    p = subprocess.run(cmd, capture_output=True, text=True)
    for line in p.stdout.splitlines():
        if not line.startswith("data:"):
            continue
        try:
            ev = json.loads(line[5:].strip())
        except json.JSONDecodeError:
            continue
        cid = ev.get("conversation_id") or cid
        if ev.get("event") == "node_finished":
            d = ev["data"]
            nodes[d.get("title")] = d.get("elapsed_time") or 0.0
    return time.time() - t0, nodes, cid

rows = []
for c in (1, 2):
    user = f"t-t2-{time.strftime('%H%M%S')}-{c}"
    conv = None
    print(f"\n########## 会話{c}")
    for i, q in enumerate(TURNS, 1):
        wall, nodes, conv = turn(user, q, conv)
        gas = {k: v for k, v in nodes.items() if k in (KARTE, INTAKE)}
        total = sum(nodes.values())
        llm = nodes.get("LLM", 0.0)
        rows.append(dict(c=c, i=i, wall=wall, total=total, llm=llm,
                         gas=sum(gas.values()), gas_nodes=sorted(gas)))
        tag = "／".join(("カルテ照会" if k == KARTE else "初回受付") + f" {v:.2f}" for k, v in gas.items()) or "GASなし"
        print(f"  {i}通目  実測 {wall:6.1f}  ノード合計 {total:6.1f}  LLM {llm:5.2f}  [{tag}]")
        sys.stdout.flush()

print("\n" + "=" * 70)
for label, sel in (("1通目", lambda r: r["i"] == 1),
                   ("2〜5通目（初回受付あり）", lambda r: 2 <= r["i"] <= 5),
                   ("6通目以降（GASを通らない）", lambda r: r["i"] >= 6)):
    v = [r["wall"] for r in rows if sel(r)]
    g = [r["gas"] for r in rows if sel(r)]
    l = [r["llm"] for r in rows if sel(r)]
    if not v:
        continue
    over = sum(1 for x in v if x > 24)
    print(f"\n{label}  n={len(v)}")
    print(f"  実測    p50={statistics.median(v):6.1f}  max={max(v):6.1f}  min={min(v):5.1f}  over24={over}({round(over*100/len(v))}%)")
    print(f"  GAS合計 p50={statistics.median(g):6.2f}  max={max(g):6.2f}")
    print(f"  LLM     p50={statistics.median(l):6.2f}  max={max(l):6.2f}")
