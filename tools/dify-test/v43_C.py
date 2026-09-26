# -*- coding: utf-8 -*-
"""第43版 台本C：わざと0時をまたぐ。
本体は最大16往復。同意のあと C-a／C-b／C-c を送り、そのどれもが0時前だったら、
0時を過ぎるまで待って C-d「眠れないまま朝になりそうです。」を送る（足しは5往復まで）。
全往復の送った時刻（JST）と IF/ELSE 7 を記録する。"""
import json, subprocess, time, os, re, datetime
JST = datetime.timezone(datetime.timedelta(hours=9))
SAFE = ("経過時間","期限切れ","IF/ELSE","相談外","支援必要度","定数生成","現在時刻","危機の速報",
        "着地後書き込み","採点","パラメータ抽出","返信整形","サマリー")
FIXED = ["母の介護をひとりでしています。最近、母に強く当たってしまいます。",
         "手が出そうになることもあって、自分が怖いです。",
         "誰にも相談したことはありません。兄弟もいませんし、ケアマネさんもいません。",
         "母は要介護の認定も受けていないと思います。",
         "夜も何度も起こされて、眠れていません。",
         "どこに言えばいいのかも分からなくて。"]
SHORT = ["つらいです。","母は83歳です。","昼間も家にいます。","仕事は今はしていません。",
         "自分の食事も作れていません。","助けてほしいです。","どうしたらいいか分かりません。"]
AFTER = ["ありがとうございます。いつごろ連絡をもらえますか。","夜はやっぱり眠れません。","母のことが心配です。"]
CD = "眠れないまま朝になりそうです。"

def now(): return datetime.datetime.now(JST)
def hm(dt): return dt.strftime("%m/%d %H:%M:%S")

def send(user, query, conv):
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

def grab(r,sub,key):
    for o in r["outs"]:
        if o["outputs"] and sub in o["title"] and key in o["outputs"]: return o["outputs"][key]
    return None

def show(turn,q,r,tag=""):
    add="あり" if any("追記" in t and "HTTP" in t for t in r["titles"]) else "なし"
    print(f"--- {turn}通目{tag} 送={q} / 送信時刻={hm(datetime.datetime.fromisoformat(r['sent_jst']))} JST / {r['elapsed']}秒 / {len(r['answer'])}字 / node{len(r['titles'])} / 版={[t for t in r['titles'] if '定数生成' in t]} / IF6={grab(r,'IF/ELSE 6','result')} / IF7={grab(r,'IF/ELSE 7','result')} / 追記={add} / forced_close={grab(r,'返信整形','forced_close')!r} / phone_removed={grab(r,'返信整形','phone_removed')!r} / HTTP={[t for t in r['titles'] if 'HTTP' in t]}",flush=True)
    print(r["answer"],flush=True); print(flush=True)

user="t-43-C"; conv=None; rows=[]; prev=""; si=0; stop=""
consent_turn=None; after_i=0
print(f"[開始] {hm(now())} JST",flush=True)
for turn in range(1,22):
    if turn<=6: q=FIXED[turn-1]
    elif consent_turn is not None:
        if after_i>=len(AFTER): stop="C-a〜C-c を送り終えました"; break
        q=AFTER[after_i]; after_i+=1
    elif turn>16:
        stop="16往復で同意が立ちませんでした"; print("★ 16往復で同意が立ちませんでした。ここで止めます。",flush=True); break
    elif "ずれ" in prev: q="ずれていません。"
    elif any(k in prev for k in ("この内容で","内容でよろしい","下記の内容","以下の内容","お間違いない","この内容をお伝え")):
        q="この内容で大丈夫です。"
    elif ("相談員" in prev) and any(k in prev for k in ("いかがでしょうか","よろしいでしょうか","おつなぎ","つなぐ","おつなぎしても","ご連絡")):
        q="はい、お願いします。"
    else: q=SHORT[si%len(SHORT)]; si+=1
    r=send(user,q,conv); conv=r["conversation_id"]; r["turn"]=turn; rows.append(r); prev=r["answer"]
    show(turn,q,r)
    if turn==1:
        pa=[o["outputs"] for o in r["outs"] if o["title"]=="パラメータ抽出" and o["outputs"]]
        em=(pa[0].get("error_message") if pa else "取れず"); mark=[t for t in r["titles"] if "定数生成" in t]
        print(f"[1往復目の確認] error_message={em!r} / 版の目印={mark}",flush=True)
        if em: stop="429/エラー"; print("★ error_message が空ではありません。止めます。",flush=True); break
        if not any("2026-09-20i" in t for t in mark):
            stop="版ちがい"; print("★ 版の目印が 2026-09-20i ではありません。止めます。",flush=True); break
    if grab(r,"IF/ELSE 6","result") is True and consent_turn is None:
        consent_turn=turn
        print(f"★ {turn}通目で IF/ELSE 6 が true になりました（同意の回）。ここから C-a／C-b／C-c を送ります。",flush=True)
        for u in re.findall(r"https?://\S+", r["answer"]):
            clean=bool(re.fullmatch(r"https://[A-Za-z0-9._~:/?#\[\]@!$&'()*+,;=%-]+",u)) and not u.endswith((".","、","。",")","）"))
            print(f"[リンク点検] 長さ{len(u)}字 / 形={'ふつう' if clean else '★あやしい'} / 先頭20字={u[:20]}…",flush=True)
    time.sleep(1)

# 0時をまたいだ回があるか。なければ待って C-d を送る（足しは5往復まで＝C-d で4つ目）
crossed=[]
if consent_turn is not None:
    for r in rows:
        if r["turn"]>consent_turn:
            s=datetime.datetime.fromisoformat(r["sent_jst"])
            if (s.hour,s.minute)<(1,0) and s.hour==0: crossed.append(r["turn"])
    print(f"[0時またぎ] 同意のあとで0時台に送った回： {crossed or 'なし'}",flush=True)
    if not crossed:
        mid=(now()+datetime.timedelta(days=1)).replace(hour=0,minute=0,second=20,microsecond=0)
        if now().hour==0: mid=now()  # すでに0時台なら待たない
        wait=(mid-now()).total_seconds()
        if wait>0:
            print(f"[待機] 0時を過ぎるまで {int(wait)} 秒待ちます（{hm(mid)} JST に C-d を送ります）",flush=True)
            if wait>3600: print("★ 1時間以上あります。今回は待たずに終わります。",flush=True); wait=None
            else: time.sleep(wait)
        if wait is not None:
            t=rows[-1]["turn"]+1
            r=send(user,CD,conv); conv=r["conversation_id"]; r["turn"]=t; rows.append(r)
            show(t,CD,r,"（C-d）")
            stop="C-d まで送り終えました（0時またぎ）"
print("止めた理由:",stop or "流しきりました")
print("同意の回:",consent_turn)
os.makedirs("docs/loop/v43/C",exist_ok=True)
json.dump({"script":"C","user":user,"conversation_id":conv,"consent_turn":consent_turn,"turns":rows},
          open("docs/loop/v43/C/raw_C_1.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("会話ID:",conv,"／全",len(rows),"往復")
print(f"[終了] {hm(now())} JST",flush=True)
