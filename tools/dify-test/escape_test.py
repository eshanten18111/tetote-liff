#!/usr/bin/env python3
"""初回受付・追記ノードが改行/引用符/バックスラッシュで壊れないか確認する"""
import json, sys, time, dify

CASES = [
 ("A-改行あり", "呼び名：かおる\n年代：50代\n性別：その他\n都道府県：北海道\n一番の悩み：仕事\n\n長く勤めた職場を辞めることになりました。\n次が決まっておらず、不安です。"),
 ("B-引用符", '呼び名："たろう"／年代：20代／性別：男性／都道府県：福岡県／一番の悩み：人間関係'),
 ("C-バックスラッシュ", "呼び名：やま\\だ／年代：60代／性別：女性／都道府県：新潟県／一番の悩み：身体の悩み"),
 ("D-制御文字混在", "呼び名：みか\t／年代：40代／性別：女性／都道府県：沖縄県／一番の悩み：DV・虐待\r\n夫から暴力を受けています。"),
]

def run(tag, q):
    user = f"t-esc-{tag}-{time.strftime('%H%M%S')}"
    r = dify.turn(user, q)
    out = []
    for n in r["nodes"]:
        t = n["title"] or ""
        if "HTTP" in t:
            body = str((n["outputs"] or {}).get("body"))
            ok = '"ok":true' in body
            out.append((t, n["status"], "OK" if ok else "NG", body[:220]))
    ex = next((n["outputs"] for n in r["nodes"] if n["title"] == "パラメータ抽出"), {}) or {}
    return out, {k: ex.get(k) for k in ("extracted_user_name","extracted_prefecture","need_basis")}, r["answer"][:150]

for tag, q in CASES:
    print(f"\n{'='*60}\n### {tag}")
    print("送信:", repr(q[:90]))
    nodes, ex, ans = run(tag, q)
    for t, st, verdict, body in nodes:
        print(f"  [{verdict}] {t} status={st}")
        print(f"        body={body}")
    print("  抽出:", json.dumps(ex, ensure_ascii=False)[:260])
    print("  返答:", ans.replace("\n", " ")[:150])
