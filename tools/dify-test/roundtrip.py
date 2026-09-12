#!/usr/bin/env python3
"""実運用の一周を通しでテストする。
入口フォーム → 相談 → 着地 → フォーム受領 → 追記(合図) → 追記(直書き) → 再開 → 2周目
"""
import json, time, dify

user = "t-round-" + time.strftime("%H%M%S")
KEY = ("パラメータ抽出", "コード（支援必要度", "コード（危機", "IF/ELSE 11", "IF/ELSE 12",
       "コード（サマリー", "コード（追記", "追記本文抽出", "返信整形", "HTTP",
       "コード（期限切れ", "IF/ELSE 7")

SCRIPT = [
 # --- 1周目 ---
 ("①入口フォーム",   "呼び名：みさき／年代：40代／性別：女性／都道府県：長崎県／一番の悩み：DV・虐待／その他の悩み1：経済・生活費"),
 ("②本題",           "夫から毎日怒鳴られ、先週は腕をつかまれて痣ができました。今も同じ家にいます"),
 ("③切迫",           "所持金も少なく、逃げる先もありません。子どもも怯えています"),
 ("④孤立",           "誰にも言えていません。実家も頼れなくて"),
 ("⑤求める",         "もう自分では動けません。だれかに助けてほしいです"),
 ("⑥同意",           "はい、その理解で合っています"),
 ("⑦同意",           "はい"),
 ("⑧同意",           "はい、お願いします"),
 ("⑨同意",           "はい"),
 ("⑩同意",           "はい"),
 ("⑪同意",           "はい"),
 # --- 着地後 ---
 ("⑫詳細確認フォーム", "詳細確認フォーム回答：受付しました"),
 ("⑬追記(合図)",      "追記フォーム回答：受付しました"),
 ("⑭追記(直書き)",    'あのあと夫から"出ていけ"と言われました。\n夜も眠れていません。'),
 # --- 2周目 ---
 ("⑮再開",           "相談を再開します"),
 ("⑯2周目の相談",     "あれから家を出ました。今は知人の家にいますが、長くはいられません"),
 ("⑰2周目の深掘り",   "仕事も探さないといけません。何から手をつけたらいいか分かりません"),
 ("⑱2周目の同意",     "はい、また相談員さんにお願いしたいです"),
]

conv = None
for label, q in SCRIPT:
    t0 = time.time()
    r = dify.turn(user, q, conv)
    conv = r["conversation_id"]
    nodes = [n for n in r["nodes"] if n["title"]]
    ex = next((n["outputs"] for n in nodes if n["title"] == "パラメータ抽出"), {}) or {}
    code = next((n["outputs"] for n in nodes if "コード（支援必要度" in n["title"]), {}) or {}
    print(f"\n{'='*70}\n### {label} ({time.time()-t0:.0f}秒) USER: {q[:60]}".replace("\n", " "))
    print(f"必要度={ex.get('support_need')} 最高={code.get('max_support_need')} "
          f"contact_safety_risk={ex.get('contact_safety_risk')} phase={code.get('phase')}")
    for n in nodes:
        t = n["title"]
        if not any(k in t for k in KEY) or t == "パラメータ抽出":
            continue
        o = n["outputs"]
        if isinstance(o, dict):
            o = {k: v for k, v in o.items() if k not in ("__usage", "headers", "__reason", "__is_success")}
        s = json.dumps(o, ensure_ascii=False)
        if t.startswith("HTTP") or "追記" in t or "サマリー" in t or "危機" in t or "IF/ELSE 1" in t or "期限切れ" in t or "返信整形" in t:
            print(f"   [{t}] {n['status']} {s[:300]}")
    print(f"   BOT({len(r['answer'])}字): {r['answer'][:230]}".replace("\n", " "))
    if r["error"]:
        print("   !!ERROR", json.dumps(r["error"], ensure_ascii=False)[:200])
print("\nCONV:", conv)
