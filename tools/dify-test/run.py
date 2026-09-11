#!/usr/bin/env python3
"""シナリオ実行: 複数ターンを1会話で流し、要点だけ出力する"""
import json, sys, dify

KEEP_NODES = ("パラメータ抽出", "入口フォーム", "IF/ELSE", "コード", "HTTP", "変数代入", "経過時間")
DROP_KEYS = ("__usage", "__reason", "__is_success", "headers")

def clean(o):
    if isinstance(o, dict):
        return {k: v for k, v in o.items() if k not in DROP_KEYS}
    return o

def run(name, turns, inputs=None):
    conv = None
    print(f"\n{'='*70}\n### {name}\n{'='*70}")
    for i, q in enumerate(turns, 1):
        r = dify.turn(name, q, conv, inputs if i == 1 else {})
        conv = r["conversation_id"]
        print(f"\n--- turn {i} USER: {q[:120]}")
        print(f"BOT: {r['answer'][:1200]}")
        for n in r["nodes"]:
            if any(k in (n["title"] or "") for k in KEEP_NODES):
                print(f"   [{n['title']}] {n['status']} {json.dumps(clean(n['outputs']), ensure_ascii=False)[:600]}")
        if r["error"]:
            print("   !!ERROR", json.dumps(r["error"], ensure_ascii=False)[:400])
    print(f"\n(conversation_id: {conv})")
    return conv

if __name__ == "__main__":
    spec = json.load(open(sys.argv[1]))
    run(spec["name"], spec["turns"], spec.get("inputs"))
