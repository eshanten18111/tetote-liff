#!/usr/bin/env python3
"""残高切れで無効になった V2/V3 を測り直す。モデル失敗を検知したら即中断する。"""
import json, time, dify

OPENING = [
 "呼び名：{name}／年代：40代／性別：女性／都道府県：{pref}／一番の悩み：経済・生活費",
 "収入が減ってしまい、来月の家賃が払えそうにありません",
 "夜も眠れません。ひとり暮らしで頼れる人もいなくて",
 "貯金も尽きました。何から手をつけていいか分からず、頭が真っ白です",
 "はい、正直もう限界です。誰かに助けてほしいです",
]
VARIANTS = {
 "V2-短く「はい」": ("のぶこ", "長野県", ["はい"] * 6),
 "V3-言い方を変える": ("さとみ", "宮城県",
   ["はい、お願いします", "伝えていただいて大丈夫です", "その内容で合っています",
    "ぜひ相談員さんとお話ししたいです", "はい", "はい"]),
}

def failed(r):
    for n in r["nodes"]:
        if n["status"] == "failed" or (n.get("error") and "RESOURCE_EXHAUSTED" in str(n["error"])):
            return str(n.get("error"))[:120] or "node failed"
    return None

results = {}
for label, (name, pref, consent) in VARIANTS.items():
    print(f"\n### {label}")
    user = f"t-cr-{name}-{time.strftime('%H%M%S')}"
    conv, consent_at, verdict = None, len(OPENING) + 1, None
    for i, q in enumerate([t.format(name=name, pref=pref) for t in OPENING] + consent, 1):
        r = dify.turn(user, q, conv)
        conv = r["conversation_id"]
        f = failed(r)
        if f or not r["answer"]:
            print(f"  turn{i} 中断: モデル失敗またはの空応答 ({f})")
            verdict = "計測不能"
            break
        nodes = {n["title"]: n for n in r["nodes"] if n["title"]}
        phase = (nodes.get("コード（支援必要度の保持・フェーズ・着地判定）", {}).get("outputs") or {}).get("phase")
        if any("引き継ぎサマリー" in t and "相談記録登録" in t for t in nodes):
            verdict = i - consent_at + 1
            print(f"  同意 turn{consent_at} → 着地 turn{i} （同意から {verdict} 往復）")
            break
        if i >= consent_at:
            print(f"    turn{i} [{phase}] 未着地: {r['answer'][:80]}".replace("\n", " "))
    if verdict is None:
        verdict = f"{len(consent)}往復同意しても着地せず"
        print(f"  {verdict}")
    results[label] = verdict

print("\n" + "=" * 60)
for k, v in results.items():
    print(f"  {k}: {v}")
