# -*- coding: utf-8 -*-
"""第51版 台本ランナー。使い方: python3 v51_run.py N5|P|Q"""
import json, os, sys, time
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from v51_common import send,g,show,check_first,now,hm
VER="2026-09-23c"
FIXED5=["隣の家との音のことで、いつも気を張っています。",
        "挨拶をしても、返ってこないことが増えました。",
        "自治会の集まりにも行きにくくなりました。",
        "夫は取り合ってくれません。",
        "家にいても落ち着かないです。"]
FACTS=["引っ越してきたのは6年前です。","隣は年配のご夫婦です。","音というのは、夜10時ごろの物音です。",
 "うちは子どもが二人います。","上の子は中学生、下の子は小学生です。","下の子が家の中で走ることがあります。",
 "一度、壁を叩かれたことがあります。","そのあと防音マットを敷きました。","でも音が減ったかどうかは分かりません。",
 "回覧板は前より遅く回ってくる気がします。","町内の掃除の日も気が重いです。","スーパーで会っても目をそらされます。",
 "夫は仕事が忙しくて帰りが遅いです。","夫は「気にしすぎだ」と言います。","実家の母には少しだけ話しました。",
 "母は「引っ越せば」と言いました。","でも子どもの学校のことがあります。","住宅ローンもあと20年あります。",
 "最近、玄関を出るときに周りを見るようになりました。","洗濯物を干す時間もずらしています。",
 "夜、物音がすると体がこわばります。","眠りが浅くなった気がします。","昼間は仕事をしています。パートです。",
 "職場の人にはこの話をしていません。","休みの日は家から出ないことが増えました。",
 "前は近所の方と立ち話をしていました。","庭の手入れもしなくなりました。","郵便受けを開けるのが少し怖いです。"]
name=sys.argv[1]
if name=="N5":
    user="t-51-N5c"; MAXT=27; ASK={22,24}; LAST=None
elif name=="P":
    user="t-51-Pb"; MAXT=31; ASK=set(); LAST=31
elif name=="Q":
    user="t-51-Q"; MAXT=9; ASK=set(); LAST=None
else: raise SystemExit("N5 / P / Q のどれかを指定してください")
conv=None; rows=[]; fi=0; prev=""; stop=""; closed_at=None
print(f"[開始] {hm(now())} JST ／台本{name}／{user}",flush=True)
for turn in range(1,MAXT+1):
    if name=="Q":
        q="仕事のことでずっと悩んでいます。" if turn==1 else "どうしても納得できないんです。"
        if closed_at is not None: q="もう少しだけ話してもいいですか。"
    elif closed_at is not None:
        q="もう少しだけ話してもいいですか。"
    elif turn<=5: q=FIXED5[turn-1]
    elif LAST and turn==LAST: q="もう少しだけ話してもいいですか。"
    elif turn in ASK: q="どうしたらいいでしょうか。"
    elif "ずれ" in prev or "近い感じ" in prev: q="近いです。"
    elif ("相談員" in prev) and any(k in prev for k in ("いかがでしょうか","よろしいでしょうか","できますが","ご連絡","おつなぎ","つなぐ","関心はあります")):
        q="もう少し話を聞いてほしいです。"
    else: q=FACTS[fi%len(FACTS)]; fi+=1
    r=send(user,q,conv); conv=r["conversation_id"]; r["turn"]=turn; rows.append(r); prev=r["answer"]
    show(turn,q,r,"（締まった次の回）" if closed_at is not None and turn==closed_at+1 else "")
    if "混み合っております" in r["answer"]:
        em=g(r,"パラメータ抽出","error_message",True)
        stop=f"★★ {turn}通目で定型文（混み合っております）が返りました。AIの上限と読んで、ここで止めます"
        print(stop,flush=True)
        print(f"[error_message] {str(em)[:400]!r}",flush=True)
        break
    if turn==1:
        s=check_first(r,VER)
        if s: stop=s; break
    cl=g(r,"支援必要度","closing"); cr=g(r,"支援必要度","closing_reason")
    if name=="Q" and turn==6 and not cr and closed_at is None:
        stop="☆ 台本Q：同じ訴えを5回続けても closing_reason が空のままでした。指示書のとおり、6通目で止めます"
        print(stop,flush=True); break
    if closed_at is not None:
        stop=f"締まった次の回（{turn}通目）まで送り終えました"; break
    if cl is True or cl=="true":
        closed_at=turn
        print(f"★ {turn}通目で closing が true になりました。closing_reason={cr!r} / left={g(r,'支援必要度','left')!r} / near={g(r,'支援必要度','near')!r}",flush=True)
        dt=g(r,"その日のまとめの本文組み立て","day_text")
        if dt: print("[day_text]\n"+dt,flush=True)
        if name=="P" and turn<30:
            print(f"★★ 台本P は30通目より前（{turn}通目）で締まりました。指示書のとおり、次の回を1通だけ送って止めます。",flush=True)
    time.sleep(1)
print("止めた理由:",stop or "流しきりました")
print("締まった回:",closed_at)
os.makedirs(f"docs/loop/v51/{name}",exist_ok=True)
json.dump({"script":name,"user":user,"conversation_id":conv,"closed_at":closed_at,"turns":rows},
          open(f"docs/loop/v51/{name}/raw_{name}_1.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("会話ID:",conv,"／全",len(rows),"往復")
print(f"[終了] {hm(now())} JST",flush=True)
