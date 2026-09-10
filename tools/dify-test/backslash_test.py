#!/usr/bin/env python3
"""バックスラッシュを含む入力で事前情報の抽出が壊れるか確認する"""
import json, time, dify, concurrent.futures as cf

CASES = [
 ("C1-呼び名にバックスラッシュ再現", "呼び名：やま\\だ／年代：60代／性別：女性／都道府県：新潟県／一番の悩み：身体の悩み"),
 ("C2-同内容・バックスラッシュなし", "呼び名：やまだ／年代：60代／性別：女性／都道府県：新潟県／一番の悩み：身体の悩み"),
 ("C3-本文にバックスラッシュ", "呼び名：けんじ／年代：50代／性別：男性／都道府県：香川県／一番の悩み：仕事\n上司から「C:\\書類\\提出用」を今日中にと言われ、無理でした"),
 ("C4-呼び名にバックスラッシュ2回目", "呼び名：やま\\だ／年代：60代／性別：女性／都道府県：新潟県／一番の悩み：身体の悩み"),
]

def one(t):
    tag, q = t
    r = dify.turn(f"t-bs-{tag[:2]}-{time.strftime('%H%M%S')}", q)
    ex = next((n["outputs"] for n in r["nodes"] if n["title"] == "パラメータ抽出"), {}) or {}
    stage = next((n["outputs"] for n in r["nodes"] if n["title"] == "入口フォームかどうかの判定"), {}) or {}
    http = [(n["title"], str((n["outputs"] or {}).get("body"))[:120])
            for n in r["nodes"] if n["title"] and "HTTP" in n["title"]]
    return tag, {k: ex.get(k) for k in ("extracted_user_name","extracted_age_group","extracted_gender",
                                        "extracted_prefecture","extracted_main_issue")}, stage, http, r["answer"][:120]

with cf.ThreadPoolExecutor(max_workers=4) as p:
    for tag, ex, stage, http, ans in p.map(one, CASES):
        print(f"\n=== {tag}")
        print("  stage:", json.dumps(stage, ensure_ascii=False))
        print("  抽出 :", json.dumps(ex, ensure_ascii=False))
        for t, b in http:
            print(f"  {t}: {b}")
        print("  返答 :", ans.replace("\n"," "))
