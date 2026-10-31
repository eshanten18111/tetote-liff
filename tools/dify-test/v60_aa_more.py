# -*- coding: utf-8 -*-
"""台本AA の続き：4通目で相談員につなぐ提案が出たが、予約フォームの案内はまだ出ていない。
AA-4〜AA-7（フォームの案内の中身）は、同意しないと測れないため、
ループの判断で「はい、お願いします。」を1通だけ足す。"""
import json, os, sys, time
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from v52_common import send,g,show
P="docs/loop/v60/AA/raw_AA_1.json"
d=json.load(open(P,encoding="utf-8")); rows=d["turns"]; conv=d["conversation_id"]; user=d["user"]
t=rows[-1]["turn"]+1
q="はい、お願いします。"
r=send(user,q,conv); r["turn"]=t; rows.append(r)
show(t,q,r,"（ループが足した回：同意）")
print(f"[IF6] {g(r,'IF/ELSE 6','result')} / HTTP={[x for x in r['titles'] if 'HTTP' in x]}",flush=True)
print(f"[forced_close] {g(r,'返信整形','forced_close')!r}",flush=True)
d["turns"]=rows
d["note_more"]="4通目では予約フォームの案内が出なかったため、AA-4〜AA-7 を測るためにループの判断で『はい、お願いします。』を1通足した"
json.dump(d,open(P,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("全",len(rows),"往復")
