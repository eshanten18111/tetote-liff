# -*- coding: utf-8 -*-
import json, glob, os, time
def jst(ts): return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(ts+9*3600)) if ts else "（不明）"
for f in sorted(glob.glob('docs/loop/v19/*/raw_*.json')):
    d=json.load(open(f)); name=d['script']; out=os.path.dirname(f)+"/台本"+name+"_"+d["user"].split("-")[-1]+"_出力.md"
    L=[f"# 台本{name} 生出力（第19版）","",
       f"- 利用者ID: `{d['user']}`",f"- 会話ID: `{d['conversation_id']}`",
       f"- 版の目印: `定数生成（true文字列）／版 2026-09-17k`","",
       "本文は一字も直していません。","","---",""]
    for t in d['turns']:
        L += [f"## {t['turn']}通目",""
              ,f"- 送った文: `{t['query'] if t['query'] else '（空文字）'}`"
              ,f"- Dify側の時刻(JST): {jst(t['created_at'])}"
              ,f"- 所要: {t['elapsed']}秒 ／ 返事 {len(t['answer'])}字 ／ 通ったノード {len(t['titles'])}個",""
              ,"**返ってきた本文（そのまま）**","","```",t['answer'] if t['answer'] else "（返事なし）","```",""
              ,"<details><summary>通ったノード</summary>",""]
        for x in t['titles']: L.append(f"- {x}")
        if not t['titles']: L.append("- （ノードは1つも動いていません）")
        L += ["","</details>","","---",""]
    open(out,'w',encoding='utf-8').write("\n".join(L))
    print(out)
