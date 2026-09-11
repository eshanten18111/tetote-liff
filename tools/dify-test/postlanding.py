#!/usr/bin/env python3
"""着地後の直書きが記録されるか（A）と、初回受付の保存判定（B）を確認する"""
import json, time, dify

user = "t-post-" + time.strftime("%H%M%S")
KEY = ("追記本文抽出", "コード（追記", "コード（初回受付", "IF/ELSE 14", "IF/ELSE 7",
       "コード（期限切れ", "HTTP", "コード（サマリー", "IF/ELSE 12")

SCRIPT = [
 ("①入口フォーム", "呼び名：かなえ／年代：30代／性別：女性／都道府県：鳥取県／一番の悩み：DV・虐待"),
 ("②本題",        "夫から毎日怒鳴られ、先週は突き飛ばされました。今も同じ家にいます"),
 ("③切迫",        "所持金も少なく、逃げる先もありません"),
 ("④孤立",        "誰にも言えていません。実家も頼れなくて"),
 ("⑤求める",      "もう自分では動けません。だれかに助けてほしいです"),
 ("⑥同意",        "はい、その理解で合っています"),
 ("⑦同意",        "はい"),
 ("⑧同意",        "はい、お願いします"),
 ("⑨同意",        "はい"),
 ("⑩同意",        "はい"),
 ("⑪同意",        "はい"),
 # --- ここから着地後 ---
 ("⑫相槌",        "ありがとうございました"),
 ("⑬直書き追記",  'あのあと夫から"出ていけ"と言われました。\n夜も眠れていません。'),
 ("⑭短い訴え",    "死にたい"),
]

conv = None
for label, q in SCRIPT:
    t0 = time.time()
    r = dify.turn(user, q, conv)
    conv = r["conversation_id"]
    nodes = [n for n in r["nodes"] if n["title"]]
    titles = [n["title"] for n in nodes]
    print(f"\n{'='*70}\n### {label} ({time.time()-t0:.0f}秒) USER: {q[:55]}".replace("\n", " "))
    for n in nodes:
        t = n["title"]
        if not any(k in t for k in KEY):
            continue
        o = n["outputs"]
        if isinstance(o, dict):
            o = {k: v for k, v in o.items() if k not in ("__usage", "headers", "__reason", "__is_success", "madoguchi")}
        print(f"   [{t}] {n['status']} {json.dumps(o, ensure_ascii=False)[:330]}")
    print(f"   BOT({len(r['answer'])}字): {r['answer'][:260]}".replace("\n", " "))
print("\nCONV:", conv)
