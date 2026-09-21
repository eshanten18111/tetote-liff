# -*- coding: utf-8 -*-
"""第46版 台本C：同意のあと、0時をまたいで25往復まで（最大29往復）。
1〜6通目は決まった文。7通目以降は返事を見て返す。
同意のあとは25往復目まで当たりさわりのない書き込みを毎回ちがう内容で続け、26通目で締めを見る。"""
import json, subprocess, time, os, re, datetime
JST=datetime.timezone(datetime.timedelta(hours=9))
SAFE=("経過時間","期限切れ","IF/ELSE","相談外","支援必要度","定数生成","現在時刻","危機の速報",
      "着地後書き込み","採点","パラメータ抽出","返信整形","サマリー","まとめ","お知らせ")
FIXED=["母の介護をひとりでしています。最近、母に強く当たってしまいます。",
       "手が出そうになることもあって、自分が怖いです。",
       "誰にも相談したことはありません。兄弟もいませんし、ケアマネさんもいません。",
       "母は要介護の認定も受けていないと思います。",
       "夜も何度も起こされて、眠れていません。",
       "どこに言えばいいのかも分からなくて。"]
SHORT=["つらいです。","母は83歳です。","昼間も家にいます。","仕事は今はしていません。",
       "自分の食事も作れていません。","助けてほしいです。","どうしたらいいか分かりません。"]
# 同意のあと：当たりさわりのない書き込み（毎回ちがう内容）
AFTER=["ありがとうございます。いつごろ連絡をもらえますか。",
 "夜はやっぱり眠れません。",
 "母のことが心配です。",
 "今日は少し食べられました。",
 "デイサービスのことが気になります。",
 "書類の書き方が分かりません。",
 "近所のスーパーまで歩いて10分です。",
 "母は朝の薬を飲みました。",
 "洗濯物がたまっています。",
 "昨日は雨が降っていました。",
 "テレビはあまり見なくなりました。",
 "母が好きだった花が咲いています。",
 "台所の電球が切れました。",
 "郵便物の整理ができていません。",
 "布団を干したいと思っています。",
 "お茶を一杯だけ飲みました。",
 "窓の外が少し明るくなってきました。",
 "母の靴下を新しくしました。",
 "ゴミ出しの日を間違えそうになりました。",
 "カレンダーに印をつけました。"]

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

user="t-46-C"; conv=None; rows=[]; prev=""; si=0; ai=0; stop=""; consent=None
print(f"[開始] {hm(now())} JST",flush=True)
for turn in range(1,30):
    if turn<=6: q=FIXED[turn-1]
    elif turn==26: q="もう少しだけ話してもいいですか。"
    elif consent is not None:
        q=AFTER[ai%len(AFTER)]; ai+=1
    elif "ずれ" in prev: q="ずれていません。"
    elif any(k in prev for k in ("この内容で","内容でよろしい","下記の内容","以下の内容","お間違いない","この内容をお伝え")):
        q="この内容で大丈夫です。"
    elif ("相談員" in prev) and any(k in prev for k in ("いかがでしょうか","よろしいでしょうか","おつなぎ","つなぐ","ご連絡")):
        q="はい、お願いします。"
    else: q=SHORT[si%len(SHORT)]; si+=1
    r=send(user,q,conv); conv=r["conversation_id"]; r["turn"]=turn; rows.append(r); prev=r["answer"]
    cl=grab(r,"支援必要度","closing") or grab(r,"期限切れ","closing")
    cr=grab(r,"支援必要度","closing_reason"); lf=grab(r,"支援必要度","left") or grab(r,"期限切れ","left")
    ph=grab(r,"支援必要度","phase"); tn=grab(r,"返信整形","turn_notice"); fc=grab(r,"返信整形","forced_close")
    i6=grab(r,"IF/ELSE 6","result"); i7=grab(r,"IF/ELSE 7","result")
    sn=grab(r,"パラメータ抽出","support_need",True); sr=grab(r,"パラメータ抽出","contact_safety_risk",True)
    mark=[t for t in r["titles"] if "定数生成" in t]; http=[t for t in r["titles"] if "HTTP" in t]
    add="あり" if any("追記" in t and "HTTP" in t for t in r["titles"]) else "なし"
    print(f"--- {turn}通目 送={q} / {hm(datetime.datetime.fromisoformat(r['sent_jst']))} / {r['elapsed']}秒 / {len(r['answer'])}字 / node{len(r['titles'])} / 版={mark} / IF6={i6} / IF7={i7} / 追記={add} / closing={cl!r} / reason={cr!r} / left={lf!r} / phase={ph!r} / turn_notice={tn!r} / forced_close={fc!r} / need={sn} / risk={sr} / HTTP={http}",flush=True)
    print(r["answer"],flush=True); print(flush=True)
    if turn==1:
        pa=[o["outputs"] for o in r["outs"] if o["title"]=="パラメータ抽出" and o["outputs"]]
        em=(pa[0].get("error_message") if pa else "取れず")
        print(f"[1往復目の確認] error_message={em!r} / 版の目印={mark}",flush=True)
        if em: stop="429/エラー"; print("★ error_message が空ではありません。止めます。",flush=True); break
        if not any("2026-09-21d" in t for t in mark):
            stop="版ちがい"; print("★ 版の目印が 2026-09-21d ではありません。止めます。",flush=True); break
    if i6 is True and consent is None:
        consent=turn
        print(f"★ {turn}通目で IF/ELSE 6 が true になりました（同意の回）。",flush=True)
        for u in re.findall(r"https?://\S+", r["answer"]):
            clean=bool(re.fullmatch(r"https://[A-Za-z0-9._~:/?#\[\]@!$&'()*+,;=%-]+",u)) and not u.endswith((".","、","。",")","）"))
            print(f"[リンク点検] 長さ{len(u)}字 / 形={'ふつう' if clean else '★あやしい'} / 先頭20字={u[:20]}…",flush=True)
    elif i6 is True and turn==25:
        print("★★ 25通目で IF/ELSE 6 が true になりました（C-4 の緊急条件）。",flush=True)
    if turn>=26 and (cl is True or cl=="true"): stop=f"26通目まで送り終えました（closing true）"; break
    if turn==26: stop="26通目まで送り終えました"; break
    time.sleep(1)
print("止めた理由:",stop or "流しきりました")
print("同意の回:",consent)
os.makedirs("docs/loop/v46/C",exist_ok=True)
json.dump({"script":"C","user":user,"conversation_id":conv,"consent_turn":consent,"turns":rows},
          open("docs/loop/v46/C/raw_C_1.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("会話ID:",conv,"／全",len(rows),"往復")
print(f"[終了] {hm(now())} JST",flush=True)
