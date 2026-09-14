#!/usr/bin/env python3
"""1通目の所要時間を、ノードごとに分解する（仮説B・Cの材料）"""
import json, time, statistics, dify

Q = "呼び名：そうた／年代：30代／性別：男性／都道府県：徳島県／一番の悩み：仕事"
N = 6
runs = []
for i in range(1, N + 1):
    t0 = time.time()
    r = dify.turn(f"t-nt-{time.strftime('%H%M%S')}-{i}", Q)
    wall = time.time() - t0
    rows = [(n["title"], n.get("elapsed") or 0.0) for n in r["nodes"] if n["title"]]
    total = sum(e for _, e in rows)
    runs.append((wall, rows))
    print(f"\n=== 実行{i}  実測 {wall:.1f}秒 ／ ノード合計 {total:.1f}秒 ／ 差 {wall-total:.1f}秒")
    for t, e in sorted(rows, key=lambda x: -x[1])[:6]:
        print(f"   {e:7.2f}秒  {t}")

print("\n" + "=" * 66)
print("ノード別の所要時間（4回ぶん）")
agg = {}
for _, rows in runs:
    for t, e in rows:
        agg.setdefault(t, []).append(e)
for t, v in sorted(agg.items(), key=lambda x: -statistics.median(x[1]))[:10]:
    print(f"  p50={statistics.median(v):6.2f}  max={max(v):6.2f}  min={min(v):6.2f}  n={len(v)}  {t}")
walls = [w for w, _ in runs]
print(f"\n1通目の実測: {[round(w,1) for w in walls]}  p50={statistics.median(walls):.1f}秒")
