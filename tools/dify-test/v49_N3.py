# -*- coding: utf-8 -*-
"""第49版 台本N3：引き継ぎに至らない相談で、お知らせが出る位置を見る（31往復）。
提案が出たら毎回「もう少し話を聞いてほしいです」で続け、同意はしない。"""
import json, subprocess, time, os, datetime
JST=datetime.timezone(datetime.timedelta(hours=9))
SAFE=("経過時間","期限切れ","IF/ELSE","相談外","支援必要度","定数生成","現在時刻","危機の速報",
      "着地後書き込み","採点","パラメータ抽出","返信整形","サマリー","まとめ","お知らせ")
FIXED=["隣の家との音のことで、いつも気を張っています。",
       "挨拶をしても、返ってこないことが増えました。",
       "自治会の集まりにも行きにくくなりました。",
       "夫は取り合ってくれません。",
       "家にいても落ち着かないです。"]
FACTS=["引っ越してきたのは6年前です。",
 "隣は年配のご夫婦です。",
 "音というのは、夜10時ごろの物音です。",
 "うちは子どもが二人います。",
 "上の子は中学生、下の子は小学生です。",
 "下の子が家の中で走ることがあります。",
 "一度、壁を叩かれたことがあります。",
 "そのあと防音マットを敷きました。",
 "でも音が減ったかどうかは分かりません。",
 "回覧板は前より遅く回ってくる気がします。",
 "町内の掃除の日も気が重いです。",
 "スーパーで会っても目をそらされます。",
 "夫は仕事が忙しくて帰りが遅いです。",
 "夫は「気にしすぎだ」と言います。",
 "実家の母には少しだけ話しました。",
 "母は「引っ越せば」と言いました。",
 "でも子どもの学校のことがあります。",
 "住宅ローンもあと20年あります。",
 "最近、玄関を出るときに周りを見るようになりました。",
 "洗濯物を干す時間もずらしています。",
 "夜、物音がすると体がこわばります。",
 "眠りが浅くなった気がします。",
 "昼間は仕事をしています。パートです。",
 "職場の人にはこの話をしていません。",
 "休みの日は家から出ないことが増えました。",
 "前は近所の方と立ち話をしていました。",
 "庭の手入れもしなくなりました。",
 "郵便受けを開けるのが少し怖いです。"]
def now(): return datetime.datetime.now(JST)
def hm(d): return d.strftime("%m/%d %H:%M:%S")
def send(user,query,conv):
    body={"inputs":{},"query":query,"response_mode":"streaming","user":user}
    if conv: body["conversation_id"]=conv
    cmd=["curl","-sS","-N","--max-time","600","-X","POST","https://api.dify.ai/v1/chat-messages",
         "-H","Content-Type: application/json","-d",json.dumps(body,ensure_ascii=False)]
    sent=now(); t0=time.time(); titles=[]; outs=[]; ans=""; cid=conv; created=None; err=None
    p=subprocess.Popen(cmd,stdout=subprocess.PIPE,text=True,bufsize=1)
    for line in p.stdout:
        if not line.startswith("data:"): continue
        try: ev=json.loads(line[5:].strip())
        except Exception: continue
        cid=ev.get("conversation_id") or cid
        if ev.get("event") in ("message","agent_message"): ans+=ev.get("answer","")
        elif ev.get("event")=="error": err=ev
        elif ev.get("event")=="node_finished":
            d=ev.get("data") or {}; t=d.get("title")
            if t:
                titles.append(t)
                if created is None and d.get("created_at"): created=d["created_at"]
                if any(k in t for k in SAFE) and "HTTP" not in t:
                    outs.append({"title":t,"outputs":d.get("outputs")})
    p.wait()
    return {"query":query,"answer":ans,"titles":titles,"outs":outs,"sent_jst":sent.isoformat(),
            "elapsed":round(time.time()-t0,1),"created_at":created,"conversation_id":cid,"error":err}
def grab(r,sub,key,exact=False):
    for o in r["outs"]:
        if not o["outputs"]: continue
        if (o["title"]==sub) if exact else (sub in o["title"]):
            if key in o["outputs"]: return o["outputs"][key]
    return None
user="t-49-N3"; conv=None; rows=[]; fi=0; prev=""; stop=""
print(f"[開始] {hm(now())} JST",flush=True)
for turn in range(1,32):
    if turn<=5: q=FIXED[turn-1]
    elif turn==31: q="もう少しだけ話してもいいですか。"
    elif turn==26: q="どうしたらいいでしょうか。"          # 提案の段階に入りやすくする
    elif turn==27: q="もう少し話を聞いてほしいです。"      # 指示書のとおり戻す
    elif "ずれ" in prev or "近い感じ" in prev: q="近いです。"
    elif ("相談員" in prev) and any(k in prev for k in ("いかがでしょうか","よろしいでしょうか","できますが","ご連絡","おつなぎ","つなぐ")):
        q="もう少し話を聞いてほしいです。"
    else: q=FACTS[fi%len(FACTS)]; fi+=1
    r=send(user,q,conv); conv=r["conversation_id"]; r["turn"]=turn; rows.append(r); prev=r["answer"]
    cl=grab(r,"支援必要度","closing"); cr=grab(r,"支援必要度","closing_reason")
    lf=grab(r,"支援必要度","left"); nr=grab(r,"支援必要度","near"); ph=grab(r,"支援必要度","phase")
    lk=grab(r,"期限切れの解除","locked")
    rs=grab(r,"期限切れの解除","rescore"); ur=grab(r,"期限切れの解除","urgent"); cw=grab(r,"期限切れの解除","crisis_word")
    tn=grab(r,"返信整形","turn_notice"); fc=grab(r,"返信整形","forced_close")
    i6=grab(r,"IF/ELSE 6","result"); i7=grab(r,"IF/ELSE 7","result"); i18=grab(r,"IF/ELSE 18","result")
    sn=grab(r,"パラメータ抽出","support_need",True); sr=grab(r,"パラメータ抽出","contact_safety_risk",True)
    mark=[t for t in r["titles"] if "定数生成" in t]; http=[t for t in r["titles"] if "HTTP" in t]
    print(f"--- {turn}通目 送={q} / {hm(datetime.datetime.fromisoformat(r['sent_jst']))} / {r['elapsed']}秒 / {len(r['answer'])}字 / node{len(r['titles'])} / 版={mark} / IF6={i6} / IF7={i7} / IF18={i18} / locked={lk!r} / rescore={rs!r} / urgent={ur!r} / crisis_hard={grab(r,'期限切れの解除','crisis_hard')!r} / crisis_word={cw!r} / IF11={grab(r,'IF/ELSE 11','result')} / IF19={grab(r,'IF/ELSE 19','result')} / cat={grab(r,'パラメータ抽出','crisis_category',True)!r} / closing={cl!r} / reason={cr!r} / left={lf!r} / near={nr!r} / phase={ph!r} / turn_notice={tn!r} / forced_close={fc!r} / need={sn} / risk={sr} / HTTP={http}",flush=True)
    print(r["answer"],flush=True); print(flush=True)
    if not r["answer"].strip():
        print(f"☆ {turn}通目の返事が0字でした（node{len(r['titles'])}）。error={r['error']!r}。記録して次に進みます。",flush=True)
    if turn==1:
        print(f"[1往復目の確認] 版の目印={mark}",flush=True)
        if not any("2026-09-23a" in t for t in mark):
            stop="版ちがい"; print(f"★ 版の目印が 2026-09-23a ではありません（出たのは {mark}）。止めます。",flush=True); break
        pa=[o["outputs"] for o in r["outs"] if o["title"]=="パラメータ抽出" and o["outputs"]]
        em=(pa[0].get("error_message") if pa else None)
        print(f"[AIの上限の確認] error_message={em!r}",flush=True)
        if em: stop="429/エラー"; print("★ error_message が空ではありません。止めます。",flush=True); break
    try: need=int(sn)
    except Exception: need=None
    if need is not None and need>=8:
        stop=f"support_need が 8 以上（{turn}通目・need={need}）。上限が40に延びるため、指示書のとおりここで止めます"
        print(f"★★ {turn}通目で support_need={need}。上限が40に延びます。N-4 は35通目、N-5〜N-9 は測れません。ここで止めます。",flush=True); break
    if (cl is True or cl=="true") and turn<30:
        stop=f"closing が true（{turn}通目・30通目より前）"
        print(f"★ {turn}通目で closing が true になりました。30通目より前なので、ここで止めます。",flush=True); break
    time.sleep(1)
print("止めた理由:",stop or "31往復を流しきりました")
os.makedirs("docs/loop/v49/N3",exist_ok=True)
json.dump({"script":"N3","user":user,"conversation_id":conv,"turns":rows},
          open("docs/loop/v49/N3/raw_N3_1.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("会話ID:",conv,"／全",len(rows),"往復")
print(f"[終了] {hm(now())} JST",flush=True)
