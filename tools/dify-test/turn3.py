#!/usr/bin/env python3
"""task_next.md 第4版。3会話×8往復＝24往復。設定は1つも変えない。
a) prompt_tokens / completion_tokens  b) first_token  c) LLMのexecution_metadata
d) 遅いGAS(10秒以上)の status_code / body長 / location / node_retry回数
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
    t0 = time.time()
    nodes, cid, ft, usage, llm_meta = {}, conv, None, {}, {}
    retries, slow = {}, []
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)
    for line in p.stdout:
        if not line.startswith("data:"):
            continue
        try:
            ev = json.loads(line[5:].strip())
        except json.JSONDecodeError:
            continue
        e, d = ev.get("event"), ev.get("data") or {}
        cid = ev.get("conversation_id") or cid
        if e in ("message", "agent_message") and ft is None:
            ft = time.time() - t0
        elif e == "node_retry":
            retries[d.get("title")] = retries.get(d.get("title"), 0) + 1
        elif e == "node_finished":
            t = d.get("title"); el = d.get("elapsed_time") or 0.0
            nodes[t] = el
            if t == "LLM":
                llm_meta = d.get("execution_metadata") or {}
            if t in (KARTE, INTAKE) and el >= 10.0:
                o = d.get("outputs") or {}
                h = o.get("headers") or {}
                slow.append(dict(node=t, el=el, status=o.get("status_code"),
                                 blen=len(str(o.get("body") or "")),
                                 loc=("location" in {k.lower() for k in h}),
                                 err=(o.get("error_message") or d.get("error"))))
        elif e == "message_end":
            usage = ((ev.get("metadata") or {}).get("usage")) or {}
    p.wait(timeout=30)
    return dict(wall=time.time() - t0, nodes=nodes, cid=cid, ft=ft, usage=usage,
                llm_meta=llm_meta, retries=retries, slow=slow)

rows, slows = [], []
for c in (1, 2, 3):
    user = f"t-t3-{time.strftime('%H%M%S')}-{c}"
    conv = None
    for i, q in enumerate(TURNS, 1):
        r = turn(user, q, conv); conv = r["cid"]
        pt = int(r["usage"].get("prompt_tokens") or 0)
        ct = int(r["usage"].get("completion_tokens") or 0)
        gas = r["nodes"].get(KARTE, 0) + r["nodes"].get(INTAKE, 0)
        rows.append(dict(c=c, i=i, wall=r["wall"], llm=r["nodes"].get("LLM", 0.0),
                         pt=pt, ct=ct, ft=r["ft"], gas=gas,
                         retries=r["retries"], meta=r["llm_meta"]))
        for s in r["slow"]:
            s.update(c=c, i=i, retries=r["retries"].get(s["node"], 0))
            slows.append(s)
        print(f"会話{c} {i}通目  実測{r['wall']:6.1f}  LLM{r['nodes'].get('LLM',0):6.2f}  "
              f"prompt{pt:7}  completion{ct:6}  first_token{(r['ft'] or 0):6.1f}  GAS{gas:6.2f}")
        sys.stdout.flush()

def pct(v, q):
    v = sorted(v); k = (len(v) - 1) * q
    f = int(k); return v[f] if f + 1 >= len(v) else v[f] + (v[f+1] - v[f]) * (k - f)

print("\n" + "=" * 78)
print("=== 往復の深さ別")
for label, sel in (("1通目", lambda r: r["i"] == 1),
                   ("2〜5通目", lambda r: 2 <= r["i"] <= 5),
                   ("6通目以降", lambda r: r["i"] >= 6)):
    g = [r for r in rows if sel(r)]
    w = [r["wall"] for r in g]; f = [r["ft"] or 0 for r in g]
    over = sum(1 for x in w if x > 24)
    print(f"\n{label}  n={len(g)}")
    print(f"  実測         p50={statistics.median(w):6.1f}  p90={pct(w,.9):6.1f}  max={max(w):6.1f}  over24pct={round(over*100/len(g))}")
    print(f"  first_token  p50={statistics.median(f):6.1f}  p90={pct(f,.9):6.1f}  max={max(f):6.1f}")
    print(f"  LLM          p50={statistics.median([r['llm'] for r in g]):6.2f}")
    print(f"  prompt_tok   p50={statistics.median([r['pt'] for r in g]):7.0f}  max={max(r['pt'] for r in g):7}")
    print(f"  completion   p50={statistics.median([r['ct'] for r in g]):7.0f}  max={max(r['ct'] for r in g):7}")

def slope(xs, ys):
    n = len(xs); mx, my = sum(xs)/n, sum(ys)/n
    den = sum((x-mx)**2 for x in xs)
    return (sum((x-mx)*(y-my) for x, y in zip(xs, ys))/den) if den else 0.0

print("\n=== 入力トークンとLLM時間の関係")
xs = [r["pt"] for r in rows]; ys = [r["llm"] for r in rows]
print(f"  prompt_tokens 1,000 増あたり LLM {slope(xs, ys)*1000:+.2f}秒   "
      f"（範囲 {min(xs)}〜{max(xs)}）")
xs2 = [r["ct"] for r in rows]
print(f"  completion_tokens 1,000 増あたり LLM {slope(xs2, ys)*1000:+.2f}秒   "
      f"（範囲 {min(xs2)}〜{max(xs2)}）")

print("\n=== 遅いGASの証拠（10秒以上）")
if not slows:
    print("  該当なし")
for s in slows:
    print(f"  会話{s['c']} {s['i']}通目 {s['node']} {s['el']:.2f}秒  "
          f"status={s['status']}  body長={s['blen']}  location={s['loc']}  "
          f"node_retry={s['retries']}  err={s['err']}")

print("\n=== LLMノードの execution_metadata（最後の1件）")
print(" ", json.dumps(rows[-1]["meta"], ensure_ascii=False)[:300])
