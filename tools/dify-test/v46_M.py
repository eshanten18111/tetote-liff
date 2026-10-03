# -*- coding: utf-8 -*-
"""第46版 台本M：整理が途中のまま30往復まで延びるかを見る（31往復）。
提案が出たら毎回「もう少し話を聞いてほしいです」で続ける。"""
import json, subprocess, time, os, datetime
JST=datetime.timezone(datetime.timedelta(hours=9))
SAFE=("経過時間","期限切れ","IF/ELSE","相談外","支援必要度","定数生成","現在時刻","危機の速報",
      "着地後書き込み","採点","パラメータ抽出","返信整形","サマリー","まとめ","お知らせ")
FACTS=["仕事を辞めてから、これからのことが不安です。",
 "辞めたのは先月で、上司との折り合いが悪かったからです。",
 "同じ業界で探していますが、求人が少ないです。",
 "貯金は3か月分くらいしかありません。",
 "家賃は月に5万5千円です。",
 "履歴書を10社くらい出しましたが、面接まで進んだのは1社だけです。",
 "その1社も、年齢のことを言われて断られました。",
 "私はいま42歳です。",
 "履歴書の書き方が合っているのか分かりません。",
 "ハローワークには一度だけ行きました。",
 "担当の方は親切でしたが、また行くのが気まずいです。",
 "親には辞めたことをまだ言えていません。",
 "実家は県外で、年に一度しか帰っていません。",
 "妻には話しましたが、あまり反応がありませんでした。",
 "子どもが小学生で、習い事をやめさせようか迷っています。",
 "朝起きるのがだんだんつらくなってきました。",
 "昼間もぼんやりして、何もしない日があります。",
 "以前は休みの日に走っていましたが、最近はしていません。",
 "体重が3キロ減りました。",
 "健康保険の切り替えの手続きがまだ途中です。",
 "失業保険の手続きは済ませました。",
 "来月から給付が始まる予定です。",
 "資格の勉強を始めようか考えています。",
 "でも何から手をつければいいか分かりません。",
 "паソコンは家に一台だけあります。",
 "車は手放そうか迷っています。",
 "近所づきあいはほとんどありません。",
 "雨の日は特に気分が沈みます。",
 "今日は夕方まで横になっていました。"]
FACTS=[f.replace("паソコン","パソコン") for f in FACTS]

def now(): return datetime.datetime.now(JST)
def hm(d): return d.strftime("%m/%d %H:%M:%S")

def send(user,query,conv):
    body={"inputs":{},"query":query,"response_mode":"streaming","user":user}
    if conv: body["conversation_id"]=conv
    cmd=["curl","-sS","-N","--max-time","600","-X","POST","https://api.dify.ai/v1/chat-messages",
         "-H","Content-Type: application/json","-d",json.dumps(body,ensure_ascii=False)]
    sent=now(); t0=time.time(); titles=[]; outs=[]; ans=""; cid=conv; created=None
    p=subprocess.Popen(cmd,stdout=subprocess.PIPE,text=True,bufsize=1)
    for line in p.stdout:
        if not line.startswith("data:"): continue
        try: ev=json.loads(line[5:].strip())
        except Exception: continue
        cid=ev.get("conversation_id") or cid
        if ev.get("event") in ("message","agent_message"): ans+=ev.get("answer","")
        elif ev.get("event")=="node_finished":
            d=ev.get("data") or {}; t=d.get("title")
            if t:
                titles.append(t)
                if created is None and d.get("created_at"): created=d["created_at"]
                if any(k in t for k in SAFE) and "HTTP" not in t:
                    outs.append({"title":t,"outputs":d.get("outputs")})
    p.wait()
    return {"query":query,"answer":ans,"titles":titles,"outs":outs,"sent_jst":sent.isoformat(),
            "elapsed":round(time.time()-t0,1),"created_at":created,"conversation_id":cid}

def grab(r,sub,key,exact=False):
    for o in r["outs"]:
        if not o["outputs"]: continue
        if (o["title"]==sub) if exact else (sub in o["title"]):
            if key in o["outputs"]: return o["outputs"][key]
    return None

user="t-46-M"; conv=None; rows=[]; fi=0; prev=""; stop=""
print(f"[開始] {hm(now())} JST",flush=True)
for turn in range(1,32):
    if turn==31: q="もう少しだけ話してもいいですか。"
    elif "ずれ" in prev or "近い感じ" in prev: q="近いです。"
    elif ("相談員" in prev) and any(k in prev for k in ("いかがでしょうか","よろしいでしょうか","できますが","ご連絡","おつなぎ","つなぐ")):
        q="もう少し話を聞いてほしいです。"
    else: q=FACTS[fi%len(FACTS)]; fi+=1
    r=send(user,q,conv); conv=r["conversation_id"]; r["turn"]=turn; rows.append(r); prev=r["answer"]
    cl=grab(r,"支援必要度","closing"); 
    if cl is None: cl=grab(r,"期限切れ","closing")
    cr=grab(r,"支援必要度","closing_reason"); lf=grab(r,"支援必要度","left")
    if lf is None: lf=grab(r,"期限切れ","left")
    ph=grab(r,"支援必要度","phase")
    tn=grab(r,"返信整形","turn_notice"); fc=grab(r,"返信整形","forced_close")
    i6=grab(r,"IF/ELSE 6","result")
    sn=grab(r,"パラメータ抽出","support_need",True); sr=grab(r,"パラメータ抽出","contact_safety_risk",True)
    mark=[t for t in r["titles"] if "定数生成" in t]
    http=[t for t in r["titles"] if "HTTP" in t]
    print(f"--- {turn}通目 送={q} / {hm(datetime.datetime.fromisoformat(r['sent_jst']))} / {r['elapsed']}秒 / {len(r['answer'])}字 / node{len(r['titles'])} / 版={mark} / IF6={i6} / closing={cl!r} / reason={cr!r} / left={lf!r} / phase={ph!r} / turn_notice={tn!r} / forced_close={fc!r} / need={sn} / risk={sr} / HTTP={http}",flush=True)
    print(r["answer"],flush=True); print(flush=True)
    if turn==1:
        pa=[o["outputs"] for o in r["outs"] if o["title"]=="パラメータ抽出" and o["outputs"]]
        em=(pa[0].get("error_message") if pa else "取れず")
        print(f"[1往復目の確認] error_message={em!r} / 版の目印={mark}",flush=True)
        if em: stop="429/エラー"; print("★ error_message が空ではありません。止めます。",flush=True); break
        if not any("2026-09-21d" in t for t in mark):
            stop="版ちがい"; print("★ 版の目印が 2026-09-21d ではありません。止めます。",flush=True); break
    if (cl is True or cl=="true") and turn<30:
        stop=f"closing が true（{turn}通目・30通目より前）"
        print(f"★ {turn}通目で closing が true になりました。30通目より前なので、ここで止めます。",flush=True); break
    time.sleep(1)
print("止めた理由:",stop or "31往復を流しきりました")
os.makedirs("docs/loop/v46/M",exist_ok=True)
json.dump({"script":"M","user":user,"conversation_id":conv,"turns":rows},
          open("docs/loop/v46/M/raw_M_1.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("会話ID:",conv,"／全",len(rows),"往復")
print(f"[終了] {hm(now())} JST",flush=True)
