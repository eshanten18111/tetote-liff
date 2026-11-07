# -*- coding: utf-8 -*-
"""台本N5c の続き：25往復を過ぎてから「提案」に入れて、目安の区切りが立つかを見る。
28通目以降に「どうしたらいいでしょうか。」を送り、締まったら次の回を1通だけ送って止める。"""
import json, os, sys, time
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from v51_common import send,g,show,now,hm
P="docs/loop/v51/N5/raw_N5_1.json"
d=json.load(open(P,encoding="utf-8")); rows=d["turns"]; conv=d["conversation_id"]; user=d["user"]
closed=None
for i in range(4):
    t=rows[-1]["turn"]+1
    q="もう少しだけ話してもいいですか。" if closed is not None else "どうしたらいいでしょうか。"
    r=send(user,q,conv); conv=r["conversation_id"]; r["turn"]=t; rows.append(r)
    show(t,q,r,"（締まった次の回）" if closed is not None else "（続き）")
    if "混み合っております" in r["answer"]:
        print(f"★★ {t}通目で定型文が返りました。AIの上限と読んで止めます。",flush=True); break
    if closed is not None: break
    cl=g(r,"支援必要度","closing")
    if cl is True or cl=="true":
        closed=t
        print(f"★ {t}通目で closing が true。closing_reason={g(r,'支援必要度','closing_reason')!r} / left={g(r,'支援必要度','left')!r} / near={g(r,'支援必要度','near')!r}",flush=True)
        dt=g(r,"その日のまとめの本文組み立て","day_text")
        if dt: print("[day_text]\n"+dt,flush=True)
    time.sleep(1)
d["turns"]=rows; d["closed_at"]=closed
d["note_more"]="27往復で締まらなかったため、25往復を過ぎてから『どうしたらいいでしょうか。』を送って続けた"
json.dump(d,open(P,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("締まった回:",closed,"／全",len(rows),"往復")
