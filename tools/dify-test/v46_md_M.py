# -*- coding: utf-8 -*-
import json, re, datetime
d=json.load(open("docs/loop/v46/M/raw_M_1.json",encoding="utf-8"))
rows=d["turns"]
def g(r,sub,key,exact=False):
    for o in r["outs"]:
        if not o["outputs"]: continue
        if (o["title"]==sub) if exact else (sub in o["title"]):
            if key in o["outputs"]: return o["outputs"][key]
    return None
def jt(r): return datetime.datetime.fromisoformat(r["sent_jst"]).strftime("%H:%M:%S")
o=["# 第46版 台本M 出力（t-46-M・31往復）","",
   f"会話 `{d['conversation_id']}`／{jt(rows[0])}〜{jt(rows[-1])} JST（2026年9月21日）","",
   "| 通 | 送信 | 秒 | 字 | node | IF6 | closing | reason | left | phase | turn_notice | forced_close | need | risk | HTTP |",
   "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
for r in rows:
    o.append("| {} | {} | {} | {} | {} | {} | `{}` | `{}` | `{}` | `{}` | `{}` | `{}` | {} | {} | {} |".format(
        r["turn"],jt(r),r["elapsed"],len(r["answer"]),len(r["titles"]),
        g(r,"IF/ELSE 6","result"),
        g(r,"支援必要度","closing") or g(r,"期限切れ","closing"),
        g(r,"支援必要度","closing_reason"),
        g(r,"支援必要度","left") or g(r,"期限切れ","left"),
        g(r,"支援必要度","phase"), g(r,"返信整形","turn_notice"), g(r,"返信整形","forced_close"),
        g(r,"パラメータ抽出","support_need",True), g(r,"パラメータ抽出","contact_safety_risk",True),
        ("／".join(t for t in r["titles"] if "HTTP" in t) or "なし")))
o+=["","## 機械での突き合わせ",""]
o.append(f"- 返事が0字の回： **{[r['turn'] for r in rows if not r['answer'].strip()] or 'なし'}**")
o.append(f"- 「いつでも」： {[r['turn'] for r in rows if 'いつでも' in r['answer']] or '0件'}")
BULLET=re.compile(r"^(\\*|-|\\+)\\s")
bullets=[r["turn"] for r in rows for l in r["answer"].split("\n") if BULLET.match(l.strip())]
o.append(f"- 行頭の「*」「-」「+」： {bullets or '0件'}")
o.append(f"- 「**」： {[r['turn'] for r in rows if '**' in r['answer']] or '0件'}")
o.append(f"- `turn_notice` が出た回： {[(r['turn'],g(r,'返信整形','turn_notice')) for r in rows if g(r,'返信整形','turn_notice')]}")
for w in ("あと何回","残り回数","上限","何往復","制限","回数"):
    hits=[(r["turn"],[l.strip()[:90] for l in r["answer"].split("\n") if w in l]) for r in rows if w in r["answer"]]
    o.append(f"- 「{w}」が出た回： {[h[0] for h in hits] or '0件'}")
    for t,ls in hits:
        for l in ls: o.append(f"  - {t}通目： `{l}`")
o.append(f"- 「#いのちSOS」： {[r['turn'] for r in rows if '#いのちSOS' in r['answer']] or '0件'}")
o.append(f"- 「よりそいホットライン」： {[r['turn'] for r in rows if 'よりそい' in r['answer']] or '0件'}")
o.append(f"- 最後の1文字： "+" ".join(f"{r['turn']}:{(r['answer'].strip()[-1] if r['answer'].strip() else '（空）')}" for r in rows))
o+=["","## その日のまとめ（30通目・`day_text` をそのまま）","","```"]
o.append(g(rows[29],"その日のまとめの本文組み立て","day_text") or "（取れませんでした）")
o+=["```",""]
o+=["## 全文",""]
for r in rows:
    a=re.sub(r"https://\S+","（LINEのフォームへのリンク：アドレスは書き写していません）",r["answer"])
    o+=[f"### {r['turn']}通目（{jt(r)} JST）",f"**送った文**：{r['query']}","","**返事：**","```",
        (a if a.strip() else "（返事が返ってきませんでした。0字です）"),"```",""]
open("docs/loop/v46/M/台本M_出力.md","w",encoding="utf-8").write("\n".join(o)+"\n")
print("\n".join(o[:45]))
