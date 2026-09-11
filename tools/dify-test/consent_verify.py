#!/usr/bin/env python3
"""引き継ぎの提案が出るか、出たら「はい」だけで着地するかを測る"""
import json, re, time, dify

OPENING = [
 "呼び名：みどり／年代：40代／性別：女性／都道府県：静岡県／一番の悩み：経済・生活費",
 "パートの収入だけでは家賃が払えず、来月から住むところがなくなりそうです",
 "夜も眠れず、食欲もありません。ひとり暮らしで頼れる人もいなくて",
 "貯金も尽きました。何から手をつけていいか分からず、頭が真っ白です",
 "もう自分では動けないので、だれかに一緒に考えてほしいです。相談員さんに話を聞いてもらえるなら、お願いしたいです",
]
FILLER = [
 "はい、その理解で合っています",
 "そうですね、その通りだと思います",
 "他に付け足すことはありません",
 "はい、お話しした内容で間違いありません",
 "特に修正したいところはありません",
 "はい",
]
# 引き継ぎの可否を尋ねている合図
ASK = re.compile(r"(相談員|担当者|スタッフ).{0,80}(よろしいでしょうか|いかがでしょうか|お伝えして|つないで|おつなぎ|お話ししませんか|введ)"
                 r"|よろしいでしょうか|いかがでしょうか", re.S)

user = "t-cv-" + time.strftime("%H%M%S")
conv, proposed_at, landed_at, consent_sent_at = None, None, None, None
log = []

for i in range(1, 13):
    if i <= len(OPENING):
        q = OPENING[i-1]
    elif proposed_at and consent_sent_at is None:
        q = "はい"                      # ← 提案が出たので、短い同意だけを送る
        consent_sent_at = i
    else:
        q = FILLER[min(i - len(OPENING) - 1, len(FILLER)-1)]

    r = dify.turn(user, q, conv)
    conv = r["conversation_id"]
    nodes = {n["title"]: n for n in r["nodes"] if n["title"]}
    phase = (nodes.get("コード（支援必要度の保持・フェーズ・着地判定）", {}).get("outputs") or {}).get("phase")
    ex = nodes.get("パラメータ抽出", {}).get("outputs") or {}
    http_bad = [(t, (n["outputs"] or {}).get("error_message") or str((n["outputs"] or {}).get("body"))[:80])
                for t, n in nodes.items() if "HTTP" in t and ('"ok":true' not in str((n["outputs"] or {}).get("body")))]
    landed = any("引き継ぎサマリー" in t and "相談記録登録" in t for t in nodes)
    liff = "liff.line.me" in r["answer"]
    asks = bool(ASK.search(r["answer"]))

    print(f"\n--- turn {i} [{phase}] 必要度={ex.get('support_need')} USER: {q[:56]}")
    print(f"BOT({len(r['answer'])}字): {r['answer'][:420]}")
    print(f"    提案らしき問いかけ={asks} LIFF案内={liff} サマリー登録={landed}")
    for t, e in http_bad:
        print(f"    ⚠ {t}: {e}")
    if r["error"]:
        print("    !!ERROR", json.dumps(r["error"], ensure_ascii=False)[:200])

    if asks and proposed_at is None and i >= len(OPENING):
        proposed_at = i
    if landed or liff:
        landed_at = i
        break

print("\n" + "="*60)
print(f"引き継ぎの提案が出たターン : {proposed_at or '出ず'}")
print(f"「はい」だけを送ったターン : {consent_sent_at or '送れず'}")
print(f"着地したターン            : {landed_at or '着地せず'}")
if consent_sent_at and landed_at:
    print(f"→ 同意から着地まで {landed_at - consent_sent_at + 1} 往復")
print("CONV:", conv)
