#!/usr/bin/env python3
"""task_next.md（18時台版）の測定。設定は1つも変えない。
a) カルテ照会・初回受付の elapsed を4階級で数える
b) 打ち手B見積り  c) 打ち手A見積り  A+B見積り
1-3の注意：実測 < ノード合計 の回があれば、式を使わず事実だけ報告する
"""
import json, os, subprocess, sys, time, statistics

API = "https://api.dify.ai/v1/chat-messages"
Q = "呼び名：そうた／年代：30代／性別：男性／都道府県：徳島県／一番の悩み：仕事"
CLIENT_TIMEOUT, N = 360, 12
KARTE = "HTTP リクエスト（カルテ照会）"
INTAKE = "HTTP リクエスト（相談記録登録：初回受付）"
BINS = [(0.0, 5.0, "0-5秒   "), (5.0, 10.0, "5-10秒  "),
        (10.0, 15.0, "10-15秒 "), (15.0, 10**9, "15秒以上")]

def one(user):
    payload = {"inputs": {}, "query": Q, "response_mode": "streaming", "user": user}
    cmd = ["curl", "-sS", "-N", "--max-time", str(CLIENT_TIMEOUT), "-X", "POST", API,
           "-H", "Content-Type: application/json"]
    key = os.environ.get("DIFY_API_KEY")
    if key:
        cmd += ["-H", f"Authorization: Bearer {key}"]
    cmd += ["-d", json.dumps(payload, ensure_ascii=False)]
    t0 = time.time(); nodes = {}
    p = subprocess.run(cmd, capture_output=True, text=True)
    for line in p.stdout.splitlines():
        if not line.startswith("data:"):
            continue
        try:
            ev = json.loads(line[5:].strip())
        except json.JSONDecodeError:
            continue
        if ev.get("event") == "node_finished":
            d = ev["data"]
            nodes[d.get("title")] = d.get("elapsed_time") or 0.0
    return time.time() - t0, nodes

rows = []
for k in range(1, N + 1):
    wall, nodes = one(f"t-est-{time.strftime('%H%M%S')}-{k}")
    kt, it = nodes.get(KARTE, 0.0), nodes.get(INTAKE, 0.0)
    total = sum(nodes.values())
    rows.append(dict(k=k, wall=wall, total=total, karte=kt, intake=it))
    print(f"実行{k:2}  実測 {wall:6.1f}  ノード合計 {total:6.1f}  差 {wall-total:5.1f}  "
          f"カルテ照会 {kt:6.2f}  初回受付 {it:6.2f}")
    sys.stdout.flush()

# 1-3 の注意：直列の前提が崩れていないか
broken = [r for r in rows if r["wall"] < r["total"]]
print("\n" + "=" * 70)
if broken:
    print("!! 実測 < ノード合計 の回がある（並列に走っている証拠）。式は使わない。")
    for r in broken:
        print(f"   実行{r['k']}: 実測 {r['wall']:.1f} < ノード合計 {r['total']:.1f}")
    sys.exit(0)
print("直列の前提は崩れていない（全12回で 実測 ≧ ノード合計）")

def bins(vals, label):
    print(f"\n=== 階級（{label}・n={len(vals)}）")
    for lo, hi, name in BINS:
        c = sum(1 for v in vals if lo <= v < hi)
        print(f"    {name}: {c}回" + ("  ★" if lo == 15.0 else ""))

bins([r["karte"] for r in rows], "カルテ照会")
bins([r["intake"] for r in rows], "初回受付")

est = {
    "実測     ": [r["wall"] for r in rows],
    "B見積り  ": [r["wall"] - max(0.0, r["karte"] - 8.0) for r in rows],
    "A見積り  ": [r["wall"] - r["intake"] for r in rows],
    "A+B見積り": [r["wall"] - max(0.0, r["karte"] - 8.0) - r["intake"] for r in rows],
}
print("\n=== over24pct の比較")
for k, v in est.items():
    print(f"    {k}: {round(sum(1 for x in v if x > 24) * 100 / len(v))}%  "
          f"({sum(1 for x in v if x > 24)}/{len(v)})")
print("\n=== p50 の比較")
for k, v in est.items():
    print(f"    {k}: {statistics.median(v):.1f}秒")
print("\n=== max の比較")
for k, v in est.items():
    print(f"    {k}: {max(v):.1f}秒")
