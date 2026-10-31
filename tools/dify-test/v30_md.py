# -*- coding: utf-8 -*-
import json, glob, os, time
def jst(ts): return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(ts+9*3600)) if ts else "（不明）"
KEY=("現在時刻","経過時間","期限切れ","支援必要度","相談外","パラメータ抽出","IF/ELSE 7","IF/ELSE 18","IF/ELSE 19","IF/ELSE 11","IF/ELSE 6","IF/ELSE 4")
def turns(d):
    if 'turns' in d: return d['turns']
    t=d['turn']
    return [dict(t, turn=d['script'], titles=[n['title'] for n in t.get('nodes',[])],
                 outs=[n for n in t.get('nodes',[]) if 'outputs' in n])]
groups={}
for f in sorted(glob.glob('docs/loop/v30/*/raw_*.json')):
    d=json.load(open(f)); groups.setdefault(d['user'],[]).append(d)
for user,ds in groups.items():
    out=f"docs/loop/v30/{ds[0]['script'][:2]}/台本_{user}_出力.md"
    os.makedirs(os.path.dirname(out),exist_ok=True)
    L=[f"# {user} の生出力（第27版）","",f"- 利用者ID: `{user}`",
       f"- 会話ID: `{ds[0]['conversation_id']}`",
       "- 版の目印: `定数生成（true文字列）／版 2026-09-19y`","",
       "本文は一字も直していません。","","---",""]
    rows=[]
    for d in ds:
        for t in turns(d): rows.append(t)
    rows.sort(key=lambda t: int(t['turn']) if str(t['turn']).isdigit() else 0)
    for t in rows:
        if True:
            L += [f"## {t['turn']} 通目","",
                  f"- 送った文: `{t['query']}`",
                  f"- Dify側の時刻(JST): {jst(t.get('created_at'))}",
                  f"- 所要: {t['elapsed']}秒 ／ 返事 {len(t['answer'])}字 ／ ノード {len(t['titles'])}個","",
                  "**返ってきた本文（そのまま）**","","```",t['answer'],"```",""]
            picks=[o for o in t.get('outs',[]) if any(k in o['title'] for k in KEY) and o.get('outputs')]
            if picks:
                L += ["**判定・分岐ノードの出力**","","```"]
                for o in picks:
                    v={k:x for k,x in o['outputs'].items() if k not in ('madoguchi','__usage')}
                    L.append(f"{o['title']}\n  → {json.dumps(v,ensure_ascii=False)[:600]}")
                L += ["```",""]
            L += ["<details><summary>通ったノード</summary>",""]
            for x in t['titles']: L.append(f"- {x}")
            L += ["","</details>","","---",""]
    open(out,'w',encoding='utf-8').write("\n".join(L))
    print(out)
