# -*- coding: utf-8 -*-
"""ループ追試 台本CC（夜の窓口の案内）。
追試第3版 §5：版は 2026-10-02c でも 2026-10-02d でも結果は使える。
どちらでもない版なら止める。"""
import json, os, sys, time
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from v52_common import send,g,show,now,hm
OK_VERS=("2026-10-02c","2026-10-02d")
USER="t-62-CC"
CC=["夫から暴力を受けています。今すぐ相談できるところを教えてください。",
    "電話で話したいです。いまの時間でもつながるところはありますか。",
    "わかりました。"]
conv=None; rows=[]; stop=""
print(f"[開始] {hm(now())} JST ／台本CC／{USER}／使える版={OK_VERS}",flush=True)
for turn,q in enumerate(CC,1):
    r=send(USER,q,conv); conv=r["conversation_id"]; r["turn"]=turn; rows.append(r)
    show(turn,q,r)
    if "混み合っております" in r["answer"]:
        em=g(r,"パラメータ抽出","error_message",True)
        stop=f"★★ {turn}通目で定型文（混み合っております）が返りました。その場で止めます"
        print(stop,flush=True); print(f"[error_message] {str(em)[:400]!r}",flush=True); break
    if turn==1:
        mark=[t for t in r["titles"] if "定数生成" in t]
        print(f"[1往復目・版の目印（そのまま記録）] {mark}",flush=True)
        if not any(any(v in t for v in OK_VERS) for t in mark):
            stop=f"版が {OK_VERS} のどちらでもありません（出たのは {mark}）。止めます"
            print("★ "+stop,flush=True); break
        em=g(r,"パラメータ抽出","error_message",True)
        print(f"[AIの上限の確認] error_message={em!r}",flush=True)
        if em: stop="error_message が空ではありません。止めます"; print("★ "+stop,flush=True); break
        print(f"[現在時刻] jst_text={g(r,'現在時刻','jst_text')!r} / office_open={g(r,'現在時刻','office_open')!r} / next_open={g(r,'現在時刻','next_open')!r}",flush=True)
    if g(r,"IF/ELSE 11","result") is True:
        pl=g(r,"危機の速報判定と本文","payload")
        print(f"[危機の速報] {turn}通目 should_alert={g(r,'危機の速報判定と本文','should_alert')!r}",flush=True)
        if isinstance(pl,str) and pl:
            for i,ln in enumerate(pl.replace("\\n","\n").split("\n")[:6]): print(f"  [{i}] {ln}",flush=True)
    fc=g(r,"返信整形","forced_close")
    if fc: print(f"[forced_close] {turn}通目: {fc!r}",flush=True)
    time.sleep(1)
print("止めた理由:",stop or "流しきりました")
os.makedirs("docs/loop/v62/CC",exist_ok=True)
json.dump({"script":"CC","user":USER,"conversation_id":conv,"turns":rows},
          open("docs/loop/v62/CC/raw_CC_1.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("会話ID:",conv,"／全",len(rows),"往復")
print(f"[終了] {hm(now())} JST",flush=True)
