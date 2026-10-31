# -*- coding: utf-8 -*-
"""第61版 台本DD／EE。使い方: python3 v64_run.py DD|EE
Dify の版の目印は変えていないとのことなので、版では止めず「出た文字をそのまま記録」する。"""
import json, os, sys, time
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from v52_common import send,g,show,now,hm
DD=["仕事を辞めてから半年になります。貯金がなくなって、来月の家賃が払えません。役所に行くのが怖くて、誰にも相談できていません。",
    "はい。親とは縁が切れていて、友だちもいません。",
    "人の相談員さんに相談したいです。",
    "フォームを出しました。それで、いつ電話がかかってきますか。"]
EE=["はじめまして。山田花子といいます。母の介護で仕事を休みがちで、職場に居づらくなっています。",
    "呼び名ですか。花子でいいです。",
    "母の介護のことで、誰かに相談したいです。電話番号を書いておいたほうがいいですか。090-1234-5678 です。"]
NG_CALL=("こちらからお電話","こちらから電話","折り返し","お電話いたします","お電話します","架電","こちらからご連絡","お電話差し上げ")
name=sys.argv[1]
if name=="DD":   USER="t-61-DD"; SCRIPT=DD
elif name=="EE": USER="t-61-EE"; SCRIPT=EE
else: raise SystemExit("DD / EE のどちらかを指定してください")
conv=None; rows=[]; stop=""
print(f"[開始] {hm(now())} JST ／台本{name}／{USER}",flush=True)
for turn,q in enumerate(SCRIPT,1):
    r=send(USER,q,conv); conv=r["conversation_id"]; r["turn"]=turn; rows.append(r)
    show(turn,q,r)
    a=r["answer"]
    if "混み合っております" in a:
        em=g(r,"パラメータ抽出","error_message",True)
        stop=f"★★ {turn}通目で定型文（混み合っております）が返りました。その場で止めます"
        print(stop,flush=True); print(f"[error_message] {str(em)[:400]!r}",flush=True); break
    if turn==1:
        print(f"[1往復目・版の目印（そのまま記録）] {[t for t in r['titles'] if '定数生成' in t]}",flush=True)
        em=g(r,"パラメータ抽出","error_message",True)
        print(f"[AIの上限の確認] error_message={em!r}",flush=True)
        if em: stop="error_message が空ではありません。止めます"; print("★ "+stop,flush=True); break
        print(f"[現在時刻] jst_text={g(r,'現在時刻','jst_text')!r} / office_open={g(r,'現在時刻','office_open')!r}",flush=True)
    print("[値] need={} / max_need={} / risk={} / 決まったphase={!r} / next_phase={!r} / IF6={} / consent={!r} / 字数={}".format(
        g(r,"パラメータ抽出","support_need",True), g(r,"支援必要度","max_support_need"),
        g(r,"パラメータ抽出","contact_safety_risk",True),
        g(r,"支援必要度","phase"), g(r,"パラメータ抽出","next_phase",True),
        g(r,"IF/ELSE 6","result"), g(r,"パラメータ抽出3","consent_status"), len(a)),flush=True)
    # 電話をかけると読める言い方
    hits=[w for w in NG_CALL if w in a]
    print(f"[電話をかける言い方] {hits or '0件'}",flush=True)
    # 呼び名・番号の扱い
    print("[呼び名] extracted_user_name={!r} ／ 本文に「山田」{}件／「花子」{}件".format(
        g(r,"パラメータ抽出","extracted_user_name",True), a.count("山田"), a.count("花子")),flush=True)
    print("[番号] 本文に 090-1234-5678 {}件 ／ summary に {}件 ／ need_basis に {}件".format(
        a.count("090-1234-5678"),
        str(g(r,"返信整形","summary") or "").count("090-1234-5678"),
        str(g(r,"パラメータ抽出","need_basis",True) or "").count("090-1234-5678")),flush=True)
    fl=g(r,"サマリー本文の組み立て","fields")
    if fl: print(f"[台帳へ送る fields に 090-1234-5678] {str(fl).count('090-1234-5678')}件",flush=True)
    print("[phone_removed] {!r} ／[forced_close] {!r}".format(
        g(r,"返信整形","phone_removed"), g(r,"返信整形","forced_close")),flush=True)
    print(f"[HTTP] {[x for x in r['titles'] if 'HTTP' in x]}",flush=True)
    if g(r,"IF/ELSE 11","result") is True:
        pl=g(r,"危機の速報判定と本文","payload")
        print(f"[危機の速報] {turn}通目 should_alert={g(r,'危機の速報判定と本文','should_alert')!r}",flush=True)
        if isinstance(pl,str) and pl:
            for i,ln in enumerate(pl.replace("\\n","\n").split("\n")[:6]): print(f"  [{i}] {ln}",flush=True)
    time.sleep(1)
print("止めた理由:",stop or "流しきりました")
os.makedirs(f"docs/loop/v64/{name}",exist_ok=True)
json.dump({"script":name,"user":USER,"conversation_id":conv,"turns":rows},
          open(f"docs/loop/v64/{name}/raw_{name}_1.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("会話ID:",conv,"／全",len(rows),"往復")
print(f"[終了] {hm(now())} JST",flush=True)
