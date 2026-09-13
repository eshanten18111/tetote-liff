#!/usr/bin/env python3
"""カルテが無い人（初めての方）で、照会が落ちても相談が進むかを見る"""
import json, time, dify
user = "t-karte-" + time.strftime("%H%M%S")   # 台帳に存在しないLINEユーザーID
TURNS = [
 "呼び名：はじめ／年代：20代／性別：男性／都道府県：三重県／一番の悩み：仕事",
 "職場でうまくいかず、続けられるか不安です",
]
conv = None
for i, q in enumerate(TURNS, 1):
    t0 = time.time()
    r = dify.turn(user, q, conv)
    conv = r["conversation_id"]
    print(f"\n--- turn {i} ({time.time()-t0:.0f}秒) USER: {q[:50]}")
    for n in r["nodes"]:
        t = n["title"] or ""
        if not any(k in t for k in ("カルテ", "IF/ELSE 16", "HTTP")):
            continue
        o = n["outputs"]
        if isinstance(o, dict):
            o = {k: v for k, v in o.items() if k not in ("__usage", "headers", "__reason", "__is_success")}
        print(f"   [{t}] {n['status']} {json.dumps(o, ensure_ascii=False)[:300]}")
    print(f"   BOT({len(r['answer'])}字): {r['answer'][:180]}".replace("\n", " "))
print("\nCONV:", conv)
