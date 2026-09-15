#!/usr/bin/env python3
"""着地済みの会話に同じ文を2回送り、速報が黙らないか／判定が3状態かを見る"""
import json, time, dify
USER, CONV = "t-post-133714", "a8cb9b20-6362-4f69-9138-ab67afe2132a"
MSG = "あのあとも眠れない日が続いています"
for i in (1, 2):
    t0 = time.time()
    r = dify.turn(USER, MSG, CONV)
    print(f"\n--- {i}回目 ({time.time()-t0:.0f}秒) USER: {MSG}")
    for n in r["nodes"]:
        t = n["title"] or ""
        if not any(k in t for k in ("速報", "IF/ELSE 15", "追記", "HTTP", "IF/ELSE 13", "IF/ELSE 7")):
            continue
        o = n["outputs"]
        if isinstance(o, dict):
            o = {k: v for k, v in o.items() if k not in ("__usage", "headers", "__reason", "__is_success")}
        print(f"   [{t}] {n['status']} {json.dumps(o, ensure_ascii=False)[:260]}")
