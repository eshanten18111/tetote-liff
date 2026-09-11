#!/usr/bin/env python3
"""同意後に応答が空になる原因を調べる（全ノードとエラーをダンプ）"""
import json, time, dify

OPENING = [
 "呼び名：ちひろ／年代：40代／性別：女性／都道府県：栃木県／一番の悩み：経済・生活費",
 "収入が減ってしまい、来月の家賃が払えそうにありません",
 "夜も眠れません。ひとり暮らしで頼れる人もいなくて",
 "貯金も尽きました。何から手をつけていいか分からず、頭が真っ白です",
 "はい、正直もう限界です。誰かに助けてほしいです",
]
CONSENT = ["はい"] * 5

user = "t-diag-" + time.strftime("%H%M%S")
conv = None
for i, q in enumerate(OPENING + CONSENT, 1):
    r = dify.turn(user, q, conv)
    conv = r["conversation_id"]
    verbose = i > len(OPENING)
    print(f"\n--- turn {i} USER: {q[:60]}")
    print(f"BOT[{len(r['answer'])}文字]: {r['answer'][:400]}")
    if r["error"]:
        print("  !!ERROR:", json.dumps(r["error"], ensure_ascii=False)[:600])
    if verbose or not r["answer"]:
        for n in r["nodes"]:
            o = n["outputs"]
            if isinstance(o, dict):
                o = {k: v for k, v in o.items() if k not in ("__usage", "headers")}
            print(f"   [{n['title']}] {n['status']} {json.dumps(o, ensure_ascii=False)[:260]}"
                  + (f" ERR={n['error']}" if n.get("error") else ""))
print("\nCONV:", conv)
