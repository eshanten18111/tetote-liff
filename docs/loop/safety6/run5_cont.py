"""台本5だけ、会話が切れないように流す。
台本の文は safety6.py から読み込む（書き写さない・変えない）。
30秒でPOSTが切られたら、会話IDを履歴から拾って続きを送る。"""
import json, subprocess, time, sys, importlib.util
spec=importlib.util.spec_from_file_location("s6","safety6.py"); s6=importlib.util.module_from_spec(spec); spec.loader.exec_module_from = None
import types
src=open("safety6.py",encoding="utf-8").read()
ns={}
exec(compile(src.split("def say(")[0],"safety6","exec"),ns)   # SCRIPTS 定義まで
title,turns,checks = ns["SCRIPTS"][4]
API="https://api.dify.ai/v1/chat-messages"
U="t-s5-"+time.strftime("%H%M%S")+"-5"
def post(q,conv):
    p={"inputs":{},"query":q,"response_mode":"blocking","user":U}
    if conv: p["conversation_id"]=conv
    t0=time.time()
    r=subprocess.run(["curl","-sS","--max-time","360","-X","POST",API,
      "-H","Content-Type: application/json","-d",json.dumps(p,ensure_ascii=False)],
      capture_output=True,text=True)
    el=time.time()-t0
    try:
        d=json.loads(r.stdout); return (d.get("answer") or "").strip(), d.get("conversation_id"), el, ""
    except Exception:
        return None, None, el, r.stdout[:80]
def find_conv():
    r=subprocess.run(["curl","-sS","--max-time","60",
      f"https://api.dify.ai/v1/conversations?user={U}&limit=1&sort_by=-updated_at"],capture_output=True,text=True)
    d=json.loads(r.stdout).get("data",[]); return d[0]["id"] if d else None
def find_answer(conv,q):
    r=subprocess.run(["curl","-sS","--max-time","60",
      f"https://api.dify.ai/v1/messages?conversation_id={conv}&user={U}&limit=20"],capture_output=True,text=True)
    for m in json.loads(r.stdout).get("data",[]):
        if str(m.get("query","")).strip()==q.strip(): return (m.get("answer") or "").strip()
    return None
out=["# §5 安全確認の出力（"+time.strftime("%Y-%m-%d %H:%M")+"）— 台本5の流し直し","",
 "**これは判定ではありません。人が読んで○×を付けるための材料です。**","",
 "```",
 "この環境ではプロキシが30秒でPOSTを切るため、台本5の1通目（入口フォーム）が",
 "2回とも切れ、2通目以降が別の会話になっていた（＝10代という情報が入らない）。",
 "台本の文は safety6.py から読み込んでいて、1文字も変えていない。",
 "違うのは、切れた回の会話IDを GET /conversations から拾って",
 "続きとして送っている点だけ。**作業側の手元では、この細工は要らない。**",
 "```","","---","","## "+title,"","見るところ（人が判定する）",""]
out += ["- [ ] "+c for c in checks]; out.append("")
conv=None
for i,q in enumerate(turns,1):
    a,c,el,raw = post(q,conv)
    if c: conv=c
    if a is None:
        if not conv:
            time.sleep(3); conv=find_conv()
        a = find_answer(conv,q) if conv else None
        note=f"（POSTは{el:.1f}秒で切れたため、Difyの履歴から取得）"
    else:
        note=""
    print(f"  {i}通目 {el:.1f}秒 {'履歴から取得' if note else 'そのまま取得'} conv={str(conv)[:8]}")
    out += [f"### {i}通目（{el:.1f}秒）{note}","","**送った文**","","```",q,"```","",
            "**返ってきた全文**","","```", a if a else "(取得できませんでした)","```",""]
out += ["---","","## 台帳に増えた行","","**相談記録に 1 行**（会話IDは `t-s5-` で始まる）。**消すのは人。**"]
name="safety6_出力_台本5流し直し_"+time.strftime("%H%M%S")+".md"
open(name,"w",encoding="utf-8").write("\n".join(out)+"\n")
print("\n利用者:",U,"／ 会話:",conv)
print("書き出しました:",name)
