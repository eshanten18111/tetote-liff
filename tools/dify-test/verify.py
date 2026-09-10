#!/usr/bin/env python3
"""着地まで会話を進め、引き継ぎサマリー登録ノードの応答を確認する"""
import json, sys, time, dify

USER = "t-verify-" + time.strftime("%H%M%S")
OPENING = [
 "呼び名：まなみ／年代：30代／性別：女性／都道府県：兵庫県／一番の悩み：経済・生活費／その他の悩み1：メンタル不調（精神疾患含む）",
 "パートの契約が今月で切れてしまって、来月の家賃が払えそうにありません",
 "夜も眠れず、食事も喉を通らない日が続いています。ひとり暮らしで頼れる人もいません",
 "貯金も底をつきました。何から手をつけていいか分からなくて、頭が真っ白です",
 "はい、正直もう限界だと感じています。誰かに助けてほしいです",
]
NUDGE = "はい、お願いします。相談員さんに伝えてください"

conv, found = None, None
turns = OPENING + [NUDGE] * 6

for i, q in enumerate(turns, 1):
    r = dify.turn(USER, q, conv)
    conv = r["conversation_id"]
    nodes = {n["title"]: n for n in r["nodes"] if n["title"]}
    ex = nodes.get("パラメータ抽出", {}).get("outputs") or {}
    phase = (nodes.get("コード（支援必要度の保持・フェーズ・着地判定）", {}).get("outputs") or {}).get("phase")
    print(f"\n--- turn {i} [{phase}] USER: {q[:60]}")
    print(f"BOT: {r['answer'][:300]}")
    for title, n in nodes.items():
        if "HTTP" in title:
            o = n["outputs"] or {}
            print(f"   ★[{title}] status={n['status']} body={str(o.get('body'))[:300]}")
            if "引き継ぎサマリー" in title and "相談記録登録" in title:
                found = (title, n["status"], o.get("body"))
    if found:
        print("\n" + "="*60)
        print("引き継ぎサマリー登録ノードの応答:", json.dumps(found, ensure_ascii=False))
        break

print("\nCONV:", conv)
if not found:
    print("!! 着地に至らず、サマリー登録ノードが発火しませんでした")
