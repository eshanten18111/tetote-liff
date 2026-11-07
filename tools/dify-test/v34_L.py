# -*- coding: utf-8 -*-
"""台本L：25往復で区切りに入るかを見る。毎回あたらしい事実を1つ足す。
AIの返事を見て、提案されたら「もう少し話を聞いてほしいです」、
ずれを聞かれたら「近いです」を返す。"""
import json, subprocess, time, os
SAFE = ("経過時間","期限切れ","IF/ELSE","相談外","支援必要度","定数生成","現在時刻","危機の速報",
        "着地後書き込み","採点","パラメータ抽出","返信整形")
FACTS = [
 "仕事を辞めてから、これからのことが不安です。",
 "辞めたのは先月で、上司との折り合いが悪かったからです。",
 "同じ業界で探していますが、求人が少ないです。",
 "貯金は3か月分くらいしかありません。",
 "家賃は月に5万5千円です。",
 "履歴書を10社くらい出しましたが、面接まで進んだのは1社だけです。",
 "その1社も、年齢のことを言われて断られました。",
 "私はいま42歳です。",
 "resume の書き方が合っているのか分かりません。",
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
]
FACTS = [f.replace("resume の書き方","履歴書の書き方") for f in FACTS]

def send(user, query, conv):
    body={"inputs":{},"query":query,"response_mode":"streaming","user":user}
    if conv: body["conversation_id"]=conv
    cmd=["curl","-sS","-N","--max-time","600","-X","POST","https://api.dify.ai/v1/chat-messages",
         "-H","Content-Type: application/json","-d",json.dumps(body,ensure_ascii=False)]
    t0=time.time(); titles=[]; outs=[]; ans=""; cid=conv; created=None
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
    return {"query":query,"answer":ans,"titles":titles,"outs":outs,
            "elapsed":round(time.time()-t0,1),"created_at":created,"conversation_id":cid}

user="t-34-L"; conv=None; rows=[]; fi=0; prev=""
for turn in range(1,27):
    if turn==26:
        q="もう少しだけ話してもいいですか。"
    elif "ずれ" in prev or "近い感じ" in prev:
        q="近いです。"
    elif ("相談員" in prev) and any(k in prev for k in ("いかがでしょうか","よろしいでしょうか","できますが","ご連絡")):
        q="もう少し話を聞いてほしいです。"
    else:
        q=FACTS[fi % len(FACTS)]; fi+=1
    r=send(user,q,conv); conv=r["conversation_id"]; r["turn"]=turn; rows.append(r); prev=r["answer"]
    ex=[o["outputs"] for o in r["outs"] if "期限切れ" in o["title"] and o["outputs"]]
    pa=[o["outputs"] for o in r["outs"] if o["title"]=="パラメータ抽出" and o["outputs"]]
    la=(ex[0].get("length_alerted") if ex else "?")
    print(f"--- {turn}通目 送={q} / {r['elapsed']}秒 / {len(r['answer'])}字 / node{len(r['titles'])} / length_alerted={la!r} / need={(pa[0].get('support_need') if pa else '-')}",flush=True)
    print(r["answer"][:400],flush=True); print(flush=True)
    if "次にお話しできるのは" in r["answer"] and turn<25:
        print(f"★ {turn}通目で区切りに入りました。26通目まで送らずに止めます。",flush=True)
        if turn<25: break
    time.sleep(1)
os.makedirs("docs/loop/v34/L",exist_ok=True)
json.dump({"script":"L","user":user,"conversation_id":conv,"turns":rows},
          open("docs/loop/v34/L/raw_L_1.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("会話ID:",conv)
