# -*- coding: utf-8 -*-
"""第39版 台本C の記録を読める形に。C-3（記号）・C-4（電話）・C-8（いつでも）も機械で当たる。"""
import json, re, datetime
d=json.load(open("docs/loop/v39/C/raw_C_1.json",encoding="utf-8"))
rows=d["turns"]
def get(r,sub,key,exact=False):
    for o in r["outs"]:
        if not o["outputs"]: continue
        if (o["title"]==sub) if exact else (sub in o["title"]):
            if key in o["outputs"]: return o["outputs"][key]
    return None
def jst(ts): return datetime.datetime.fromtimestamp(ts,datetime.timezone(datetime.timedelta(hours=9))).strftime("%H:%M")
out=["# 第39版 台本C 出力（t-39-C・13往復）","",
     f"同意の回：{d['consent_turn']}通目／開始 {jst(rows[0]['created_at'])}〜終了 {jst(rows[-1]['created_at'])} JST","",
     "| 通 | 秒 | 字 | node | IF6 | forced_close | phone_removed | need | HTTPノード |","|---|---|---|---|---|---|---|---|---|"]
for r in rows:
    out.append("| {} | {} | {} | {} | {} | `{}` | `{}` | {} | {} |".format(
        r["turn"],r["elapsed"],len(r["answer"]),len(r["titles"]),
        get(r,"IF/ELSE 6","result"),get(r,"返信整形","forced_close"),get(r,"返信整形","phone_removed"),
        get(r,"パラメータ抽出","support_need",True),
        ("／".join(t for t in r["titles"] if "HTTP" in t) or "なし")))

out+=["","## C-3　行の頭の記号・強調",""]
bad3=[]
for r in rows:
    for i,line in enumerate(r["answer"].split("\n"),1):
        s=line.strip()
        if re.match(r"^(\*|-|\+)\s", s) or re.match(r"^#{1,6}\s", s): bad3.append((r["turn"],i,"行の頭",s[:60]))
    for m in re.finditer(r"\*\*", r["answer"]): bad3.append((r["turn"],"-","**",r["answer"][max(0,m.start()-25):m.start()+25].replace("\n","／")))
out.append(f"- 行の頭が「*」「-」「+」「#見出し」／「**」がある箇所： **{len(bad3)}件**")
for b in bad3: out.append(f"  - {b[0]}通目 {b[1]}行目 {b[2]}： `{b[3]}`")
star=[(r["turn"],ln.strip()[:60]) for r in rows for ln in r["answer"].split("\n") if "*" in ln]
out.append(f"- 「*」の文字が本文のどこかにある行： {len(star)}件")
for t,s in star: out.append(f"  - {t}通目： `{s}`")
bullets=sorted({ln.strip()[0] for r in rows for ln in r["answer"].split("\n") if ln.strip() and ln.strip()[0] in "・*-+1234567890▼"})
out.append(f"- 箇条書きに使われていた先頭文字： {bullets}")

out+=["","## C-4　電話番号",""]
for w in ("#いのちSOS","#8008","いのちSOS","8008","0120-061-338","0120-279-338","よりそいホットライン"):
    hits=[r["turn"] for r in rows if w in r["answer"]]
    out.append(f"- 「{w}」が出た回： {hits or '0件'}")
naked=[(r["turn"]) for r in rows if re.search(r"(?<!#)いのちSOS", r["answer"]) or re.search(r"(?<!#)8008", r["answer"])]
out.append(f"- 「#」が落ちた形（いのちSOS／8008 の直前に # がない）： {sorted(set(naked)) or 'なし'}")

out+=["","## C-8　このチャットについての「いつでも」",""]
for w in ("いつでもお声がけください","いつでもご連絡ください","いつでもお待ちしています","いつでもお話","いつでもご相談","いつでも"):
    hits=[(r["turn"], [l.strip()[:70] for l in r["answer"].split("\n") if w in l]) for r in rows if w in r["answer"]]
    out.append(f"- 「{w}」： {[h[0] for h in hits] or '0件'}")
    for t,ls in hits:
        for l in ls: out.append(f"  - {t}通目： `{l}`")

out+=["","## C-6　日数の目安・名前・時刻の約束（C-a の返事）",""]
ca=[r for r in rows if r["turn"]==(d["consent_turn"]+1)]
if ca:
    a=ca[0]["answer"]
    for w in ("日以内","営業日","時間以内","週間","時ごろ","時頃","時まで","午前","午後","明日","本日中","担当","さん","名前"):
        if w in a: out.append(f"- 「{w}」あり：`{[l.strip()[:70] for l in a.split(chr(10)) if w in l]}`")
    out.append("- （上に出ていない語は0件）")

out+=["","## リンク（C-2）",""]
for r in rows:
    for u in re.findall(r"https?://\S+", r["answer"]):
        clean=bool(re.fullmatch(r"https://[A-Za-z0-9._~:/?#\[\]@!$&'()*+,;=%-]+",u)) and not u.endswith((".","、","。",")","）"))
        out.append(f"- {r['turn']}通目：長さ{len(u)}字／形={'ふつう' if clean else '★あやしい'}／先頭20字 `{u[:20]}…`（アドレスは書き写していません）")

out+=["","## 全文",""]
for r in rows:
    a=re.sub(r"https://\S+","（LINEのフォームへのリンク：アドレスは書き写していません）",r["answer"])
    out+= [f"### {r['turn']}通目"+("（同意の回）" if r["turn"]==d["consent_turn"] else ""),
           f"**送った文**：{r['query']}","","**返事：**","```",a,"```",""]
open("docs/loop/v39/C/台本C_出力.md","w",encoding="utf-8").write("\n".join(out)+"\n")
print("\n".join(out[:80]))
