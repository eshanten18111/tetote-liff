# -*- coding: utf-8 -*-
"""第53版 台本T。使い方: python3 v53_run.py"""
import json, os, sys, time
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from v52_common import send,g,show,check_first,now,hm
VER="2026-09-24a"
USER="t-53-T"; MAXT=30; LAST=31
FIXED5=["隣の家との音のことで、いつも気を張っています。",
        "挨拶をしても、返ってこないことが増えました。",
        "自治会の集まりにも行きにくくなりました。",
        "夫は取り合ってくれません。",
        "家にいても落ち着かないです。"]
# 家族の話（指示書の3つ）を途中で入れる回
KAZOKU={13:"夫は仕事が忙しくて帰りが遅いです。",
        16:"夫は「気にしすぎだ」と言います。",
        19:"実家の母には少しだけ話しました。"}
FACTS=["引っ越してきたのは6年前です。","隣は年配のご夫婦です。","音というのは、夜10時ごろの物音です。",
 "うちは子どもが二人います。","上の子は中学生、下の子は小学生です。","下の子が家の中で走ることがあります。",
 "一度、壁を叩かれたことがあります。","そのあと防音マットを敷きました。","でも音が減ったかどうかは分かりません。",
 "回覧板は前より遅く回ってくる気がします。","町内の掃除の日も気が重いです。","スーパーで会っても目をそらされます。",
 "でも子どもの学校のことがあります。","住宅ローンもあと20年あります。",
 "最近、玄関を出るときに周りを見るようになりました。","洗濯物を干す時間もずらしています。",
 "夜、物音がすると体がこわばります。","眠りが浅くなった気がします。","昼間は仕事をしています。パートです。",
 "職場の人にはこの話をしていません。","休みの日は家から出ないことが増えました。",
 "前は近所の方と立ち話をしていました。","庭の手入れもしなくなりました。","郵便受けを開けるのが少し怖いです。",
 "ベランダに出る回数も減りました。","町内会の班長が来年まわってきます。","town の掃除は年に4回あります。".replace("town ","町内の"),
 "去年までは普通に話せていました。"]
NAMEQ=("お名前","呼び名","なんとお呼び","何とお呼び","どのようにお呼び","どうお呼び","お呼びすれば","ニックネーム")
# 整理・まとめの確認を返されたとき
MATOME=("ずれ","近いでしょうか","近い感じ","合っていますか","合っていますでしょうか","このような理解",
        "認識で","間違って","違っていたら","違っていましたら","受け取り方で","お気持ちと近い")
conv=None; rows=[]; fi=0; prev=""; stop=""; closed_at=None; otto=[]
print(f"[開始] {hm(now())} JST ／台本T／{USER}／版={VER}",flush=True)
for turn in range(1,LAST+1):
    if closed_at is not None or turn==LAST: q="もう少しだけ話してもいいですか。"
    elif turn<=5: q=FIXED5[turn-1]
    elif turn in KAZOKU: q=KAZOKU[turn]
    elif any(k in prev for k in MATOME): q="近いです。"
    elif any(k in prev for k in NAMEQ): q="名前は出したくないです。"
    elif ("相談員" in prev) and any(k in prev for k in ("いかがでしょうか","よろしいでしょうか","できますが","ご連絡","おつなぎ","つなぐ","関心はあります")):
        q="もう少し話を聞いてほしいです。"
    else: q=FACTS[fi%len(FACTS)]; fi+=1
    r=send(USER,q,conv); conv=r["conversation_id"]; r["turn"]=turn; rows.append(r); prev=r["answer"]
    show(turn,q,r,"（締まった次の回）" if closed_at is not None else "")
    if "混み合っております" in r["answer"]:
        em=g(r,"パラメータ抽出","error_message",True)
        stop=f"★★ {turn}通目で定型文（混み合っております）が返りました。AIの上限と読んで、ここで止めます"
        print(stop,flush=True); print(f"[error_message] {str(em)[:400]!r}",flush=True); break
    if turn==1:
        s=check_first(r,VER)
        if s: stop=s; break
    if r["answer"].startswith("さん"):
        print(f"★ {turn}通目の返事が「さん」で始まっています（T-1/T-2）。",flush=True)
    for w in ("夫さん","妻さん"):
        if w in r["answer"]:
            otto.append((turn,w)); print(f"★ {turn}通目の返事に「{w}」が出ています（T-3）。",flush=True)
    fc=g(r,"返信整形","forced_close")
    if fc: print(f"[forced_close] {turn}通目: {fc!r}",flush=True)
    need=g(r,"パラメータ抽出","support_need",True)
    try:
        if need is not None and int(need)>=8 and turn<=25:
            print(f"★★ {turn}通目で support_need={need} です。上限が40に延びます。指示書のとおり31往復で止めます。",flush=True)
    except (TypeError,ValueError): pass
    if closed_at is not None or turn==LAST:
        stop=f"{turn}通目まで送り終えました"; break
    cl=g(r,"支援必要度","closing"); cr=g(r,"支援必要度","closing_reason")
    if cl is True or cl=="true":
        closed_at=turn
        print(f"★ {turn}通目で closing が true になりました。closing_reason={cr!r} / left={g(r,'支援必要度','left')!r} / near={g(r,'支援必要度','near')!r} / forced_close={fc!r}",flush=True)
        print(f"[締めの回の先頭10文字] {r['answer'][:10]!r}",flush=True)
        dt=g(r,"その日のまとめの本文組み立て","day_text")
        if dt: print("[day_text]\n"+dt,flush=True)
        if turn<MAXT: print(f"★★ 30通目より前（{turn}通目）で締まりました。次の回を1通だけ送って止めます。",flush=True)
    time.sleep(1)
print("止めた理由:",stop or "流しきりました")
print("締まった回:",closed_at)
print("「夫さん」「妻さん」が出た回:",otto or "0件")
os.makedirs("docs/loop/v53/T",exist_ok=True)
json.dump({"script":"T","user":USER,"conversation_id":conv,"closed_at":closed_at,"turns":rows},
          open("docs/loop/v53/T/raw_T_1.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("会話ID:",conv,"／全",len(rows),"往復")
print(f"[終了] {hm(now())} JST",flush=True)
