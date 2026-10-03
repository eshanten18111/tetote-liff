# -*- coding: utf-8 -*-
"""第37版 台本L の記録を、そのまま読める形に書き出す。"""
import json, glob, datetime, re
KEY=("次にお話しできるのは","区切らせて","一度お休み","今日はここまで")
BAN=("いつでもお声がけください","いつでもご連絡ください","いつでもお待ちしています")
rows=[]
for f in sorted(glob.glob("docs/loop/v37/L/raw_L_*.json")):
    rows+= json.load(open(f,encoding="utf-8"))["turns"]
rows.sort(key=lambda r:r["turn"])
def get(r,sub,key,exact=False):
    for o in r["outs"]:
        if not o["outputs"]: continue
        if (o["title"]==sub) if exact else (sub in o["title"]):
            if key in o["outputs"]: return o["outputs"][key]
    return None
out=["# 第37版 台本L 出力（t-37-L・26往復）",""]
out.append("| 通 | 秒 | 字 | node | closing | closing_reason | length_alerted | forced_close | IF6 | need | Slackノード |")
out.append("|---|---|---|---|---|---|---|---|---|---|---|")
for r in rows:
    sl=[t for t in r["titles"] if "HTTP" in t or "Slack" in t or "速報" in t]
    out.append("| {} | {} | {} | {} | `{}` | `{}` | `{}` | `{}` | {} | {} | {} |".format(
        r["turn"],r["elapsed"],len(r["answer"]),len(r["titles"]),
        get(r,"期限切れ","closing"),get(r,"支援必要度","closing_reason"),
        get(r,"期限切れ","length_alerted"),get(r,"返信整形","forced_close"),
        get(r,"IF/ELSE 6","result"),get(r,"パラメータ抽出","support_need",True),
        ("／".join(sl) if sl else "なし")))
out+=["","## 機械での突き合わせ",""]
for w in KEY:
    hits=[r["turn"] for r in rows if w in r["answer"] and r["turn"]<=24]
    out.append(f"- 1〜24通目に「{w}」： {hits if hits else '0件'}")
for w in BAN:
    hits=[r["turn"] for r in rows if w in r["answer"]]
    out.append(f"- 禁止語「{w}」： {hits if hits else '0件'}")
fc=[(r["turn"],get(r,"返信整形","forced_close")) for r in rows if r["turn"]<=24 and get(r,"返信整形","forced_close")]
out.append(f"- 1〜24通目で forced_close が空でない回： {fc if fc else 'なし'}")
tel=[r["turn"] for r in rows if "いのちSOS" in r["answer"]]
out.append(f"- 「#いのちSOS」が出た回： {tel if tel else '0件'}")
out.append(f"- 「よりそいホットライン」が出た回： {[r['turn'] for r in rows if 'よりそい' in r['answer']] or '0件'}")
out.append(f"- 返事が0字の回： {[r['turn'] for r in rows if not r['answer'].strip()] or 'なし'}")
tail=[(r["turn"],r["answer"].strip()[-1]) for r in rows]
out.append("- 各回の最後の1文字： "+" ".join(f"{t}:{c}" for t,c in tail))
out+=["","## 全文",""]
for r in rows:
    out+= [f"### {r['turn']}通目",f"**送った文**：{r['query']}","","**返事：**","```",r["answer"],"```",""]
open("docs/loop/v37/L/台本L_出力.md","w",encoding="utf-8").write("\n".join(out)+"\n")
print("\n".join(out[:60]))
