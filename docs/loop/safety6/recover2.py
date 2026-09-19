import re, glob, json, subprocess
# 出力ファイルから、失敗した往復を**機械的に**拾う（手で書き写さない）
miss=[]
for f in sorted(glob.glob("safety6_出力_*.md")):
    stamp=re.search(r"_(\d{6})\.md$",f).group(1)
    txt=open(f,encoding="utf-8").read()
    for blk in re.split(r"(?=^## 台本)", txt, flags=re.M):
        m=re.match(r"## 台本(\d)([^\n]*)", blk)
        if not m: continue
        num, rest = m.group(1), m.group(2)
        user = f"t-s5-{stamp}-{num}"
        for t in re.finditer(r"### (\d+通目)（([\d.]+)秒）\n\n\*\*送った文\*\*\n\n```\n(.*?)\n```\n\n\*\*返ってきた全文\*\*\n\n```\n(.*?)\n```", blk, re.S):
            turn,sec,q,a=t.groups()
            if "応答を読めませんでした" in a:
                miss.append((user, f"台本{num}{rest}", turn, sec, q))
print(f"失敗した往復 {len(miss)} 件を出力ファイルから抽出")

def convs(u):
    r=subprocess.run(["curl","-sS","--max-time","60",
      f"https://api.dify.ai/v1/conversations?user={u}&limit=20&sort_by=-updated_at"],
      capture_output=True,text=True)
    return [c["id"] for c in json.loads(r.stdout).get("data",[])]

out=["# 補足：POSTの応答が返らなかった5往復を、Difyの履歴から取り直したもの","",
 "**これは判定ではありません。人が読んで○×を付けるための材料です。**","",
 "## なぜ必要になったか","","```",
 "5往復とも、ちょうど30.1〜30.3秒で `upstream request failed` が返り、",
 "safety6.py は「(応答を読めませんでした)」と記録した。**Dify の失敗ではない。**",
 "ループを動かしているこの実行環境のプロキシが、30秒で接続を切っているため。",
 "**作業側の手元では起きない。**",
 "",
 "今日の測定で、このエラーが返っても Dify 側では生成が完走していることを",
 "確認済み（program.md §9「ループが実機で確かめた前提」）。",
 "送り直すと二重課金と台帳の行が増えるので、**送り直さずに**",
 "GET /v1/messages から、そのときの返事をそのまま取り出した。",
 "","対応づけは手で書き写さず、出力ファイルから機械的に拾っている。","```",""]
ok=0
for user,script,turn,sec,q in miss:
    found=None
    for cid in convs(user):
        r=subprocess.run(["curl","-sS","--max-time","60",
          f"https://api.dify.ai/v1/messages?conversation_id={cid}&user={user}&limit=20"],
          capture_output=True,text=True)
        for m in json.loads(r.stdout).get("data",[]):
            if str(m.get("query","")).strip()==q.strip():
                found=(m.get("answer") or "").strip(); break
        if found: break
    ok += 1 if found else 0
    print(f"  {script} {turn} : {'取得' if found else '取得できず'} / 送った文={q[:28]!r}")
    out += ["---","",f"## {script} {turn}（{sec}秒でPOSTが切れた回）","",
            "**送った文**","","```",q,"```","",
            "**返ってきた全文**（Difyの履歴から取得）","","```",
            found if found else "(履歴にも見つかりませんでした)","```",""]
open("safety6_補足_取り直し.md","w",encoding="utf-8").write("\n".join(out)+"\n")
print(f"\n{ok}/{len(miss)} 件を取得。書き出しました: safety6_補足_取り直し.md")
