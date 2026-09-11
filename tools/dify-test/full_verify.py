#!/usr/bin/env python3
"""着地 → 相談を再開します → 追記 を通しで確認する"""
import json, time, dify

user = "t-full-" + time.strftime("%H%M%S")
TURNS = [
 ("入口フォーム", "呼び名：れいこ／年代：50代／性別：女性／都道府県：香川県／一番の悩み：DV・虐待"),
 ("本題", "夫から毎日怒鳴られ、先週は殴られました。今も同じ家にいます"),
 ("深掘り", "怖くて眠れません。子どもも怯えています"),
 ("孤立", "誰にも言えていません。実家も頼れなくて"),
 ("求める", "もう自分では動けません。だれかに助けてほしいです"),
 ("同意", "はい、その理解で合っています"),
 ("同意", "はい"),
 ("同意", "はい、お願いします"),
 ("同意", "はい"),
 ("同意", "はい"),
 ("同意", "はい"),
]
WATCH = ("パラメータ抽出", "コード（支援必要度", "コード（サマリー", "コード（追記",
         "IF/ELSE 12", "IF/ELSE 6", "HTTP", "返信整形", "コード（期限切れ")

def dump(r, label):
    nodes = [n for n in r["nodes"] if n["title"]]
    print(f"\n--- {label} ({len(r['answer'])}字)")
    for n in nodes:
        t = n["title"]
        if not any(k in t for k in WATCH):
            continue
        o = n["outputs"]
        if isinstance(o, dict):
            o = {k: v for k, v in o.items() if k not in ("__usage", "headers")}
        s = json.dumps(o, ensure_ascii=False)
        print(f"   [{t}] {n['status']} {s[:340]}")
    return nodes

conv = None
landed = False
for label, q in TURNS:
    r = dify.turn(user, q, conv)
    conv = r["conversation_id"]
    titles = [n["title"] for n in r["nodes"] if n["title"]]
    landed = any("引き継ぎサマリー" in t and "相談記録登録" in t for t in titles)
    if landed or "liff.line.me" in r["answer"]:
        dump(r, f"着地ターン USER:{q[:30]}")
        print("   BOT:", r["answer"][:200].replace("\n", " "))
        break
    ex = next((n["outputs"] for n in r["nodes"] if n["title"] == "パラメータ抽出"), {}) or {}
    bad = [t for t in titles if "HTTP" in t]
    print(f"[{label}] 必要度={ex.get('support_need')} contact_safety_risk={ex.get('contact_safety_risk', '(項目なし)')} safety_risk={ex.get('safety_risk', '(項目なし)')}")

print("\n" + "="*60 + "\n### 相談を再開します（ロック解除の確認）")
r = dify.turn(user, "相談を再開します", conv); dump(r, "再開")
print("   BOT:", r["answer"][:260].replace("\n", " "))

print("\n" + "="*60 + "\n### 追記フォーム回答（本文が何になるか）")
r = dify.turn(user, "追記フォーム回答：受付しました", conv); dump(r, "追記")
print("   BOT:", r["answer"][:200].replace("\n", " "))
print("\nCONV:", conv)
