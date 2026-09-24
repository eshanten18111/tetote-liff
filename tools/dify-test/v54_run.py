# -*- coding: utf-8 -*-
"""第54版 台本U：引き継ぎに同意して「完結」で締まることを見る。使い方: python3 v54_run.py"""
import json, os, sys, time
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from v52_common import send,g,show,check_first,now,hm
VER="2026-09-24a"
USER="t-54-U"; MAXT=18
FIXED=["母の介護をひとりでしています。最近、母に強く当たってしまいます。",
       "手が出そうになることもあって、自分が怖いです。",
       "誰にも相談したことはありません。兄弟もいませんし、ケアマネさんもいません。",
       "母は要介護の認定も受けていないと思います。",
       "夜も何度も起こされて、眠れていません。",
       "どこに言えばいいのかも分からなくて。"]
SHORT=["つらいです。","母は83歳です。","昼間も家にいます。","仕事は今はしていません。",
       "自分の食事も作れていません。","助けてほしいです。","どうしたらいいか分かりません。"]
AFTER=["今日は少し食べられました。","デイサービスのことが気になります。"]
conv=None; rows=[]; prev=""; si=0; ai=0; stop=""; consent=None
print(f"[開始] {hm(now())} JST ／台本U／{USER}／版={VER}",flush=True)
for turn in range(1,MAXT+1):
    if turn<=6: q=FIXED[turn-1]
    elif consent is not None:
        if ai>=len(AFTER): stop="＋1・＋2 を送り終えました"; break
        q=AFTER[ai]; ai+=1
    elif "ずれ" in prev or "近い感じ" in prev: q="ずれていません。"
    elif any(k in prev for k in ("この内容で","内容でよろしい","下記の内容","以下の内容","お間違いない","この内容をお伝え")):
        q="この内容で大丈夫です。"
    elif ("相談員" in prev) and any(k in prev for k in ("いかがでしょうか","よろしいでしょうか","おつなぎ","つなぐ","ご連絡")):
        q="はい、お願いします。"
    else: q=SHORT[si%len(SHORT)]; si+=1
    r=send(USER,q,conv); conv=r["conversation_id"]; r["turn"]=turn; rows.append(r); prev=r["answer"]
    tag=f"（＋{ai}通目）" if (consent is not None and ai>0) else ""
    show(turn,q,r,tag)
    if "混み合っております" in r["answer"]:
        em=g(r,"パラメータ抽出","error_message",True)
        stop=f"★★ {turn}通目で定型文（混み合っております）が返りました。AIの上限と読んで、ここで止めます"
        print(stop,flush=True); print(f"[error_message] {str(em)[:400]!r}",flush=True); break
    if turn==1:
        s=check_first(r,VER)
        if s: stop=s; break
    if r["answer"].startswith("さん"):
        print(f"★ {turn}通目の返事が「さん」で始まっています（U-2/U-7）。",flush=True)
    for w in ("夫さん","妻さん"):
        if w in r["answer"]: print(f"★ {turn}通目の返事に「{w}」が出ています（U-7）。",flush=True)
    # 危機の速報が飛んだ回
    if g(r,"IF/ELSE 11","result") is True:
        pl=g(r,"危機の速報判定と本文","payload"); sa=g(r,"危機の速報判定と本文","should_alert")
        print(f"[危機の速報] {turn}通目 should_alert={sa!r}",flush=True)
        if isinstance(pl,str) and pl:
            lines=pl.split("\\n")
            print(f"  見出し（1行目）: {lines[0][:200]!r}",flush=True)
            for ln in lines[1:8]:
                if any(k in ln for k in ("種別","自傷","カテゴリ","必要度","危険度")):
                    print(f"  種別まわりの行: {ln[:220]!r}",flush=True)
    if g(r,"IF/ELSE 6","result") is True and consent is None:
        consent=turn
        print(f"★ {turn}通目で IF/ELSE 6 が true になりました（同意の回）。",flush=True)
        print(f"[同意の回に通ったノード]",flush=True)
        for t in r["titles"]: print("   ",t,flush=True)
    cl=g(r,"支援必要度","closing"); cr=g(r,"支援必要度","closing_reason")
    if cl is True or cl=="true":
        print(f"★ {turn}通目で closing が true。closing_reason={cr!r} / left={g(r,'支援必要度','left')!r} / IF20={g(r,'IF/ELSE 20','result')} / forced_close={g(r,'返信整形','forced_close')!r}",flush=True)
        print(f"[締めの回の先頭10文字] {r['answer'][:10]!r}",flush=True)
        dt=g(r,"その日のまとめの本文組み立て","day_text")
        print("[day_text]\n"+dt if dt else "[day_text] なし",flush=True)
        print(f"[その日のまとめ登録が動いたか] {'動いた' if any('その日のまとめ登録' in t for t in r['titles']) else '動いていない'}",flush=True)
    if turn==16 and consent is None:
        print("☆ 16往復たっても同意の提案が出ていません。指示書のとおり18往復で止めます。",flush=True)
    time.sleep(1)
print("止めた理由:",stop or "流しきりました")
print("同意の回:",consent)
os.makedirs("docs/loop/v54/U",exist_ok=True)
json.dump({"script":"U","user":USER,"conversation_id":conv,"consent_turn":consent,"turns":rows},
          open("docs/loop/v54/U/raw_U_1.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("会話ID:",conv,"／全",len(rows),"往復")
print(f"[終了] {hm(now())} JST",flush=True)
