# -*- coding: utf-8 -*-
import json, glob, os, time
def jst(ts): return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(ts+9*3600)) if ts else "（不明）"
KEY=("現在時刻","経過時間","期限切れ","支援必要度","相談外","パラメータ抽出","返信整形","IF/ELSE 6","IF/ELSE 7","IF/ELSE 10","IF/ELSE 11","IF/ELSE 15","IF/ELSE 19","着地後書き込み")
seen=set(); G={}
for f in sorted(glob.glob('docs/loop/v34/*/raw_*.json')):
    d=json.load(open(f)); who=d['user']
    if who=='t-34-MSG': who='t-34-'+f.split('raw_')[1].split('_')[0]
    for t in d['turns']:
        k=(who,int(t['turn']))
        if k in seen: continue
        seen.add(k); G.setdefault(who,{})[int(t['turn'])]=(t,d['conversation_id'])
for who,turns in G.items():
    name=who.replace('t-34-','')
    os.makedirs(f'docs/loop/v34/{name}',exist_ok=True)
    out=f'docs/loop/v34/{name}/台本{name}_出力.md'
    conv=list(turns.values())[0][1]
    L=[f"# 台本{name} 生出力（第34版）","",f"- 利用者ID: `{who}`",f"- 会話ID: `{conv}`",
       "- 版の目印: `定数生成（true文字列）／版 2026-09-19z3`","","本文は一字も直していません。","","---",""]
    for n in sorted(turns):
        t,_=turns[n]
        L += [f"## {n}通目","",f"- 送った文: `{t['query']}`",
              f"- Dify側の時刻(JST): {jst(t.get('created_at'))}",
              f"- 所要: {t['elapsed']}秒 ／ 返事 {len(t['answer'])}字 ／ ノード {len(t['titles'])}個","",
              "**返ってきた本文（そのまま）**","","```",t['answer'],"```",""]
        picks=[o for o in t.get('outs',[]) if any(k in o['title'] for k in KEY) and o.get('outputs')]
        if picks:
            L += ["**判定・分岐ノードの出力**","","```"]
            for o in picks:
                v={k:x for k,x in o['outputs'].items() if k not in ('madoguchi','__usage','result')}
                L.append(f"{o['title']}\n  → {json.dumps(v,ensure_ascii=False)[:500]}")
            L += ["```",""]
        L += ["<details><summary>通ったノード</summary>",""]
        for x in t['titles']: L.append(f"- {x}")
        L += ["","</details>","","---",""]
    open(out,'w',encoding='utf-8').write("\n".join(L)); print(out)
