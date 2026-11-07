# -*- coding: utf-8 -*-
"""台本DD の続き：3通目はフォームの案内ではなく同意の問いだったため、
DD-3（フォームの案内に「お電話番号はうかがいません」が入っているか）が測れない。
ループの判断で1通だけ足して、フォームの案内の回まで進める。"""
import json, os, sys, time
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from v52_common import send,g,show
P="docs/loop/v64/DD/raw_DD_1.json"
d=json.load(open(P,encoding="utf-8")); rows=d["turns"]; conv=d["conversation_id"]; user=d["user"]
t=rows[-1]["turn"]+1
q="すみません、まだフォームは出していませんでした。どこから入力すればいいですか。"
r=send(user,q,conv); r["turn"]=t; r["why"]="フォームの案内の回まで進めるため、ループの判断で足した"; rows.append(r)
show(t,q,r,"（ループが足した回）")
a=r["answer"]
print(f"[IF6] {g(r,'IF/ELSE 6','result')} / consent={g(r,'パラメータ抽出3','consent_status')!r}",flush=True)
print(f"[HTTP] {[x for x in r['titles'] if 'HTTP' in x]}",flush=True)
for w in ("お電話番号はうかが","お電話番号をうかが","こちらからお電話","折り返し","30分","LINE通話","LINEの通話","お選びいただいた"):
    if w in a: print(f"   ☆「{w}」 {a.count(w)}件",flush=True)
print(f"[forced_close] {g(r,'返信整形','forced_close')!r}",flush=True)
d["turns"]=rows
d["note_more"]="3通目がフォームの案内ではなく同意の問いだったため、DD-3 を測るためにループの判断で5通目を足した"
json.dump(d,open(P,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("全",len(rows),"往復")
