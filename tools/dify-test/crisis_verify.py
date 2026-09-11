#!/usr/bin/env python3
"""危機速報（支援必要度8以上）と記録登録の待ち行列化を確認する"""
import json, time, dify

user = "t-crisis-" + time.strftime("%H%M%S")
TURNS = [
 "呼び名：ゆうこ／年代：30代／性別：女性／都道府県：岩手県／一番の悩み：経済・生活費",
 "所持金が200円しかなくて、今夜泊まる場所もありません",
 "どうしたらいいでしょうか",
]
conv = None
for i, q in enumerate(TURNS, 1):
    t0 = time.time()
    r = dify.turn(user, q, conv)
    conv = r["conversation_id"]
    nodes = {n["title"]: n for n in r["nodes"] if n["title"]}
    ex = nodes.get("パラメータ抽出", {}).get("outputs") or {}
    print(f"\n--- turn {i} ({time.time()-t0:.1f}秒) USER: {q[:50]}")
    print(f"必要度={ex.get('support_need')} 種別={ex.get('crisis_category')}")
    for t, n in nodes.items():
        if "HTTP" in t or "危機" in t or "IF/ELSE 11" in t:
            o = n["outputs"] or {}
            o = {k: v for k, v in o.items() if k not in ("__usage", "headers")} if isinstance(o, dict) else o
            print(f"   [{t}] {n['status']} {json.dumps(o, ensure_ascii=False)[:300]}")
    print(f"BOT({len(r['answer'])}字): {r['answer'][:200]}".replace("\n", " "))
print("\nCONV:", conv)
