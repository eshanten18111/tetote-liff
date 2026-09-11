#!/usr/bin/env python3
"""着地させて、返信整形ノードの項目割り当て（Aの修正）を確認する"""
import json, time, dify

user = "t-sum-" + time.strftime("%H%M%S")
TURNS = [
 "呼び名：あさみ／年代：30代／性別：女性／都道府県：福井県／一番の悩み：人間関係",
 "職場で孤立していて、誰とも話せない日が続いています",
 "上司からも無視されるようになり、朝起きるのがつらいです",
 "家族にも心配をかけたくなくて、誰にも言えていません",
 "このまま消えてしまいたいと思うこともあります",
 "もう自分ひとりでは抱えきれません。だれかに聞いてほしいです",
 "はい、その理解で合っています",
 "はい",
 "はい、お願いします",
 "はい",
 "はい",
]
conv = None
for i, q in enumerate(TURNS, 1):
    r = dify.turn(user, q, conv)
    conv = r["conversation_id"]
    nodes = {n["title"]: n for n in r["nodes"] if n["title"]}
    fmt = nodes.get("返信整形（サマリー除去）", {}).get("outputs") or {}
    landed = any("引き継ぎサマリー" in t and "相談記録登録" in t for t in nodes)
    liff = "liff.line.me" in r["answer"]
    bad = [(t, (n["outputs"] or {}).get("error_message") or str((n["outputs"] or {}).get("body"))[:70])
           for t, n in nodes.items() if "HTTP" in t and n["status"] != "succeeded"]
    print(f"\n--- turn {i} LIFF={liff} サマリー登録={landed} USER: {q[:40]}")
    for t, e in bad:
        print(f"    ⚠ {t}: {e}")
    if fmt.get("summary") or fmt.get("main_category"):
        print("  ★返信整形ノードの出力:")
        for k in ("main_category", "related_issue", "urgency", "summary", "next_action", "consent"):
            v = fmt.get(k)
            if v is None:
                continue
            mark = "空" if v == "" else f"{len(str(v))}字"
            print(f"     {k:15} [{mark}] {str(v)[:160]}".replace("\n", "⏎"))
    if landed or liff:
        for t, n in nodes.items():
            if "HTTP" in t:
                print(f"    [{t}] {n['status']} {str((n['outputs'] or {}).get('body'))[:120]}")
        break
print("\nCONV:", conv)
