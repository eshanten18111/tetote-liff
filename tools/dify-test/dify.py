#!/usr/bin/env python3
"""Dify advanced-chat テストハーネス: streaming で node 出力まで取得する"""
import json, os, subprocess, sys

API = "https://api.dify.ai/v1/chat-messages"
WATCH = {"パラメータ抽出", "パラメータ抽出3（有人対応同意）", "IF/ELSE", "IF/ELSE 2",
         "IF/ELSE 4（有人対応同意判定）", "変数代入", "HTTP リクエスト",
         "HTTP リクエスト（LIFF案内・仮設定）"}

def turn(user, query, conv=None, inputs=None, timeout=300):
    payload = {"inputs": inputs or {}, "query": query,
               "response_mode": "streaming", "user": user}
    if conv:
        payload["conversation_id"] = conv
    cmd = ["curl", "-sS", "-N", "--max-time", str(timeout), "-X", "POST", API,
           "-H", "Content-Type: application/json"]
    key = os.environ.get("DIFY_API_KEY")
    if key:
        cmd += ["-H", f"Authorization: Bearer {key}"]
    cmd += ["-d", json.dumps(payload, ensure_ascii=False)]
    p = subprocess.run(cmd, capture_output=True, text=True)
    answer, nodes, conv_id, err = [], [], conv, None
    for line in p.stdout.splitlines():
        if not line.startswith("data:"):
            continue
        try:
            ev = json.loads(line[5:].strip())
        except json.JSONDecodeError:
            continue
        e = ev.get("event")
        conv_id = ev.get("conversation_id") or conv_id
        if e == "message":
            answer.append(ev.get("answer", ""))
        elif e == "node_finished":
            d = ev.get("data", {})
            nodes.append({"title": d.get("title"), "type": d.get("node_type"),
                          "status": d.get("status"),
                          "outputs": d.get("outputs"), "error": d.get("error"),
                          "elapsed": d.get("elapsed_time")})
        elif e == "error":
            err = ev
    return {"answer": "".join(answer), "nodes": nodes,
            "conversation_id": conv_id, "error": err, "raw_stderr": p.stderr}

def brief(res, show_all_nodes=False):
    out = []
    for n in res["nodes"]:
        if not show_all_nodes and n["title"] not in WATCH:
            continue
        o = n["outputs"]
        if isinstance(o, dict):
            o = {k: v for k, v in o.items() if k not in ("__reason", "__is_success")}
        out.append(f"  [{n['title']}] status={n['status']} out={json.dumps(o, ensure_ascii=False)}"
                   + (f" ERR={n['error']}" if n.get("error") else ""))
    return "\n".join(out)

if __name__ == "__main__":
    user, query = sys.argv[1], sys.argv[2]
    conv = sys.argv[3] if len(sys.argv) > 3 and sys.argv[3] else None
    inputs = json.loads(sys.argv[4]) if len(sys.argv) > 4 else {}
    r = turn(user, query, conv, inputs)
    print("CONV:", r["conversation_id"])
    print("ANSWER:", r["answer"])
    print("NODES:")
    print(brief(r, show_all_nodes=True))
    if r["error"]:
        print("ERROR:", json.dumps(r["error"], ensure_ascii=False))
