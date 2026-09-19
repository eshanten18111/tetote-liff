#!/usr/bin/env python3
"""task_next.md §7F の測定。
300秒は「返らない」のか「301秒で返るのに諦めている」のかを区別する。
a) クライアント側タイムアウト 360秒  b) 最初のトークン時刻  c) LLMのnode_started
d) 打ち切り時の最後のイベント名  e) N=12（跳ねを1回捕まえたら止める）
"""
import json, os, subprocess, sys, time, statistics

API = "https://api.dify.ai/v1/chat-messages"
Q = "呼び名：そうた／年代：30代／性別：男性／都道府県：徳島県／一番の悩み：仕事"
CLIENT_TIMEOUT = 360
N = 12
SPIKE = 120

def one(user):
    payload = {"inputs": {}, "query": Q, "response_mode": "streaming", "user": user}
    cmd = ["curl", "-sS", "-N", "--max-time", str(CLIENT_TIMEOUT), "-X", "POST", API,
           "-H", "Content-Type: application/json"]
    key = os.environ.get("DIFY_API_KEY")
    if key:
        cmd += ["-H", f"Authorization: Bearer {key}"]
    cmd += ["-d", json.dumps(payload, ensure_ascii=False)]

    t0 = time.time()
    first_token = None
    llm_started = False
    last_event = None
    nodes = []
    err = None
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)
    try:
        for line in p.stdout:
            if not line.startswith("data:"):
                continue
            try:
                ev = json.loads(line[5:].strip())
            except json.JSONDecodeError:
                continue
            e = ev.get("event")
            d = ev.get("data") or {}
            title = d.get("title") or ""
            last_event = f"{e}({title})" if title else str(e)
            if e in ("message", "agent_message") and first_token is None:
                first_token = time.time() - t0
            elif e == "node_started":
                if (d.get("node_type") == "llm") or title == "LLM":
                    llm_started = True
            elif e == "node_finished":
                nodes.append((title, d.get("elapsed_time") or 0.0))
            elif e == "error":
                err = json.dumps(ev, ensure_ascii=False)[:200]
        p.wait(timeout=30)
    except Exception as ex:
        err = f"{type(ex).__name__}: {ex}"
        p.kill()
    wall = time.time() - t0
    rc = p.returncode
    if rc == 28 or wall >= CLIENT_TIMEOUT - 2:
        ending = f"タイムアウト({CLIENT_TIMEOUT}秒)"
    elif err:
        ending = f"例外({err})"
    elif rc not in (0, None):
        ending = f"curl終了コード {rc}"
    else:
        ending = "正常"
    return dict(wall=wall, nodes=nodes, first_token=first_token,
                llm_started=llm_started, last_event=last_event, ending=ending)

walls, spike = [], None
for k in range(1, N + 1):
    r = one(f"t-7f-{time.strftime('%H%M%S')}-{k}")
    walls.append(r["wall"])
    total = sum(e for _, e in r["nodes"])
    ft = f"{r['first_token']:.1f}秒" if r["first_token"] is not None else "none"
    print(f"\n=== 実行{k}  実測 {r['wall']:.1f}秒 ／ ノード合計 {total:.1f}秒 ／ 差 {r['wall']-total:.1f}秒")
    print(f"    first_token   = {ft}")
    print(f"    llm_started   = {'yes' if r['llm_started'] else 'no'}")
    print(f"    last_event    = {r['last_event']}")
    print(f"    終了のしかた   = {r['ending']}")
    for t, e in sorted(r["nodes"], key=lambda x: -x[1])[:4]:
        print(f"      {e:7.2f}秒  {t}")
    sys.stdout.flush()
    if r["wall"] >= SPIKE:
        spike = k
        print(f"\n>>> 跳ね（{SPIKE}秒超）を捕まえたので、ここで止めます")
        break

over = sum(1 for w in walls if w > 24)
print("\n" + "=" * 66)
print(f"n={len(walls)} p50={statistics.median(walls):.1f} min={min(walls):.1f} "
      f"max={max(walls):.1f} over24={over} over24pct={round(over*100/len(walls))}")
print("実測:", [round(w, 1) for w in walls])
print("跳ね:", f"実行{spike}で捕捉" if spike else f"{len(walls)}回とも{SPIKE}秒未満")
