# -*- coding: utf-8 -*-
import json,re,sys,datetime
s=sys.argv[1]; name=sys.argv[2]
d=json.load(open(f"docs/loop/v49/{s}/raw_{s}_1.json",encoding="utf-8"))
rows=d["turns"]
def g(r,sub,key,exact=False):
    for o in r["outs"]:
        if not o["outputs"]: continue
        if (o["title"]==sub) if exact else (sub in o["title"]):
            if key in o["outputs"]: return o["outputs"][key]
    return ""
def jt(r): return datetime.datetime.fromisoformat(r["sent_jst"]).strftime("%m/%d %H:%M:%S")
o=[f"# 第48版 {name} 出力","",
   f"会話 `{d['conversation_id']}`／{jt(rows[0])}〜{jt(rows[-1])} JST","",
   "| 通 | 送った時刻(JST) | 秒 | 字 | node | IF6 | IF7 | IF18 | locked | crisis_hard | crisis_word | rescore | urgent | IF11 | IF19 | cat | closing | reason | left | near | phase | turn_notice | forced_close | need | risk | HTTPノード |",
   "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
for r in rows:
    o.append("| {} | {} | {} | {} | {} | {} | {} | {} | `{}` | `{}` | `{}` | `{}` | `{}` | {} | {} | `{}` | `{}` | `{}` | `{}` | `{}` | `{}` | `{}` | `{}` | {} | {} | {} |".format(
        r["turn"],jt(r),r["elapsed"],len(r["answer"]),len(r["titles"]),
        g(r,"IF/ELSE 6","result"),g(r,"IF/ELSE 7","result"),g(r,"IF/ELSE 18","result"),
        g(r,"期限切れの解除","locked"),g(r,"期限切れの解除","crisis_hard"),
        g(r,"期限切れの解除","crisis_word"),g(r,"期限切れの解除","rescore"),g(r,"期限切れの解除","urgent"),
        g(r,"IF/ELSE 11","result"),g(r,"IF/ELSE 19","result"),g(r,"パラメータ抽出","crisis_category",True),
        g(r,"支援必要度","closing"),g(r,"支援必要度","closing_reason"),g(r,"支援必要度","left"),
        g(r,"支援必要度","near"),g(r,"支援必要度","phase"),
        g(r,"返信整形","turn_notice"),g(r,"返信整形","forced_close"),
        g(r,"パラメータ抽出","support_need",True),g(r,"パラメータ抽出","contact_safety_risk",True),
        ("／".join(t for t in r["titles"] if "HTTP" in t) or "なし")))
o+=["","## 全文",""]
for r in rows:
    a=re.sub(r"https://\S+","（LINEのフォームへのリンク：アドレスは書き写していません）",r["answer"])
    tag=""
    if s=="R2":
        if r["turn"]==d.get("consent_turn"): tag="（同意の回）"
        elif d.get("consent_turn") and r["turn"]==d["consent_turn"]+1: tag="（＋1通目）"
        elif d.get("consent_turn") and r["turn"]==d["consent_turn"]+2: tag="（＋2通目＝自傷のことば）"
        elif d.get("consent_turn") and r["turn"]==d["consent_turn"]+3: tag="（＋3通目）"
        elif d.get("consent_turn") and r["turn"]==d["consent_turn"]+4: tag="（＋4通目＝2回目の自傷のことば）"
        elif d.get("consent_turn") and r["turn"]==d["consent_turn"]+5: tag="（＋5通目）"
    o+=[f"### {r['turn']}通目{tag}（{jt(r)} JST）",f"**送った文**：{r['query']}","","**返事：**","```",
        (a if a.strip() else "（返事が返ってきませんでした。0字です）"),"```",""]
open(f"docs/loop/v49/{s}/{name}_出力.md","w",encoding="utf-8").write("\n".join(o)+"\n")
print(f"{s}: {len(rows)}往復 書き出しました")
