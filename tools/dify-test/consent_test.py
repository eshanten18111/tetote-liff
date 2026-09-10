#!/usr/bin/env python3
"""同意してから着地するまでに何往復かかるか測る"""
import json, sys, time, dify

OPENING = [
 "呼び名：{name}／年代：40代／性別：女性／都道府県：{pref}／一番の悩み：経済・生活費",
 "収入が減ってしまい、来月の家賃が払えそうにありません",
 "夜も眠れません。ひとり暮らしで頼れる人もいなくて",
 "貯金も尽きました。何から手をつけていいか分からず、頭が真っ白です",
 "はい、正直もう限界です。誰かに助けてほしいです",
]

VARIANTS = {
 "V1-同じ文言を繰り返す": ["はい、お願いします。相談員さんに伝えてください"] * 8,
 "V2-短く「はい」":       ["はい"] * 8,
 "V3-言い方を変える":     ["はい、お願いします",
                            "伝えていただいて大丈夫です",
                            "その内容で合っています",
                            "ぜひ相談員さんとお話ししたいです",
                            "はい", "はい", "はい", "はい"],
}

def run(label, name, pref, consent_turns):
    user = f"t-cons-{name}-{time.strftime('%H%M%S')}"
    conv, consent_at, landed_at = None, None, None
    turns = [t.format(name=name, pref=pref) for t in OPENING] + consent_turns
    for i, q in enumerate(turns, 1):
        r = dify.turn(user, q, conv)
        conv = r["conversation_id"]
        nodes = {n["title"]: n for n in r["nodes"] if n["title"]}
        phase = (nodes.get("コード（支援必要度の保持・フェーズ・着地判定）", {}).get("outputs") or {}).get("phase")
        if i == len(OPENING) + 1:
            consent_at = i
        landed = any("引き継ぎサマリー" in t and "相談記録登録" in t for t in nodes)
        if landed:
            landed_at = i
            print(f"  {label}: 同意 turn{consent_at} → 着地 turn{i} （同意から {i - consent_at + 1} 往復）")
            return i - consent_at + 1
        if i > len(OPENING):
            print(f"    turn{i} [{phase}] まだ着地せず: {r['answer'][:90]}".replace("\n", " "))
    print(f"  {label}: 8往復同意し続けても着地せず")
    return None

results = {}
for label, turns in VARIANTS.items():
    print(f"\n### {label}")
    results[label] = run(label, {"V1-同じ文言を繰り返す":"あけみ","V2-短く「はい」":"のぶこ","V3-言い方を変える":"さとみ"}[label],
                         {"V1-同じ文言を繰り返す":"岡山県","V2-短く「はい」":"長野県","V3-言い方を変える":"宮城県"}[label], turns)

print("\n" + "="*60)
print("同意してから着地するまでの往復数:")
for k, v in results.items():
    print(f"  {k}: {v if v else '着地せず'}")
