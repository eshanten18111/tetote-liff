# -*- coding: utf-8 -*-
import json, glob, os, time
def jst(ts): return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(ts+9*3600)) if ts else "（不明）"
KEY=("経過時間","期限切れ","支援必要度","相談外","IF/ELSE 7","IF/ELSE 18","IF/ELSE 11","IF/ELSE 6","IF/ELSE 4","IF/ELSE 15","着地後書き込み")
for f in sorted(glob.glob('docs/loop/v23/*/raw_*.json')):
    d=json.load(open(f)); name=d['script']
    out=os.path.dirname(f)+"/台本"+name+"_"+d["user"].split("-")[-1]+"_出力.md"
    L=[f"# 台本{name} 生出力（第20版）","",
       f"- 利用者ID: `{d['user']}`",f"- 会話ID: `{d['conversation_id']}`",
       "- 版の目印: `定数生成（true文字列）／版 2026-09-18s`","",
       "本文は一字も直していません。","","---",""]
    for t in (d['turns'] if 'turns' in d else [dict(d['turn'], turn=1, outs=[n for n in d['turn'].get('nodes',[]) if 'outputs' in n], titles=[n['title'] for n in d['turn'].get('nodes',[])])]):
        L += [f"## {t['turn']}通目","",
              f"- 送った文: `{t['query'] if t['query'] else '（空文字）'}`",
              f"- Dify側の時刻(JST): {jst(t['created_at'])}",
              f"- 所要: {t['elapsed']}秒 ／ 返事 {len(t['answer'])}字 ／ 通ったノード {len(t['titles'])}個","",
              "**返ってきた本文（そのまま）**","","```",t['answer'] if t['answer'] else "（返事なし）","```",""]
        picks=[o for o in t.get('outs',[]) if any(k in o['title'] for k in KEY) and o.get('outputs')]
        if picks:
            L += ["**判定・分岐ノードの出力**","","```"]
            for o in picks:
                v=json.dumps(o['outputs'],ensure_ascii=False)
                L.append(f"{o['title']}\n  → {v[:500]}")
            L += ["```",""]
        L += ["<details><summary>通ったノード</summary>",""]
        for x in t['titles']: L.append(f"- {x}")
        if not t['titles']: L.append("- （ノードは1つも動いていません）")
        L += ["","</details>","","---",""]
    open(out,'w',encoding='utf-8').write("\n".join(L))
    print(out)
