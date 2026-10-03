# -*- coding: utf-8 -*-
"""第51版 共通部。送信・記録・表示。"""
import json, subprocess, time, datetime
JST=datetime.timezone(datetime.timedelta(hours=9))
SAFE=("経過時間","期限切れ","IF/ELSE","相談外","支援必要度","定数生成","現在時刻","危機の速報",
      "着地後書き込み","採点","パラメータ抽出","返信整形","サマリー","まとめ","お知らせ")
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
def g(r,sub,key,exact=False):
    for o in r["outs"]:
        if not o["outputs"]: continue
        if (o["title"]==sub) if exact else (sub in o["title"]):
            if key in o["outputs"]: return o["outputs"][key]
    return None
def show(turn,q,r,tag=""):
    add="あり" if any("追記" in t and "HTTP" in t for t in r["titles"]) else "なし"
    print(f"--- {turn}通目{tag} 送={q} / {hm(datetime.datetime.fromisoformat(r['sent_jst']))} / {r['elapsed']}秒 / {len(r['answer'])}字 / node{len(r['titles'])} / 版={[t for t in r['titles'] if '定数生成' in t]} / IF6={g(r,'IF/ELSE 6','result')} / IF7={g(r,'IF/ELSE 7','result')} / IF11={g(r,'IF/ELSE 11','result')} / IF18={g(r,'IF/ELSE 18','result')} / IF19={g(r,'IF/ELSE 19','result')} / locked={g(r,'期限切れの解除','locked')!r} / crisis_hard={g(r,'期限切れの解除','crisis_hard')!r} / crisis_word={g(r,'期限切れの解除','crisis_word')!r} / rescore={g(r,'期限切れの解除','rescore')!r} / urgent={g(r,'期限切れの解除','urgent')!r} / closing={g(r,'支援必要度','closing')!r} / reason={g(r,'支援必要度','closing_reason')!r} / left={g(r,'支援必要度','left')!r} / near={g(r,'支援必要度','near')!r} / phase={g(r,'支援必要度','phase')!r} / turn_notice={g(r,'返信整形','turn_notice')!r} / forced_close={g(r,'返信整形','forced_close')!r} / need={g(r,'パラメータ抽出','support_need',True)} / risk={g(r,'パラメータ抽出','contact_safety_risk',True)} / cat={g(r,'パラメータ抽出','crisis_category',True)!r} / 追記={add} / HTTP={[t for t in r['titles'] if 'HTTP' in t]}",flush=True)
    print(r["answer"],flush=True); print(flush=True)
    if not r["answer"].strip():
        print(f"☆ {turn}通目の返事が0字でした（node{len(r['titles'])}）。error={r['error']!r}。あとで Dify の保存本文で確かめます。",flush=True)
def check_first(r,ver):
    mark=[t for t in r["titles"] if "定数生成" in t]
    print(f"[1往復目の確認] 版の目印={mark}",flush=True)
    if not any(ver in t for t in mark):
        print(f"★ 版の目印が {ver} ではありません（出たのは {mark}）。止めます。",flush=True); return "版ちがい"
    pa=[o["outputs"] for o in r["outs"] if o["title"]=="パラメータ抽出" and o["outputs"]]
    em=(pa[0].get("error_message") if pa else None)
    print(f"[AIの上限の確認] error_message={em!r}",flush=True)
    if em: print("★ error_message が空ではありません。止めます。",flush=True); return "429/エラー"
    return None
