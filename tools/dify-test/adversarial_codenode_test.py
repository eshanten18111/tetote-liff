# -*- coding: utf-8 -*-
"""いただいたコードに対する独立の敵対的テスト。壊しにいく。"""
import json, importlib.util

def load(p, n):
    sp = importlib.util.spec_from_file_location(n, p)
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m

B = load('build.py', 'B'); A = load('addendum.py', 'A'); I = load('intake.py', 'I')
ng = 0
def check(name, cond, extra=""):
    global ng
    print(("  OK  " if cond else "  NG  ") + name + (("  → " + str(extra)) if (not cond and extra) else ""))
    if not cond: ng += 1

# HTTPノードのBodyを再現する（合言葉を先頭に足して1つのJSONにする形）
def body(fields, token='tok"en\\x'):
    return json.loads('{"token": ' + json.dumps(token) + ', ' + fields + '}')

print("\n■ 悪意ある/事故的な文字列を値に入れる")
NASTY = [
    ('JSONの断片', '"}, "token": "のっとり", "x": "'),
    ('波括弧と角括弧', '{"a": [1,2]} }} ]] {{'),
    ('バックスラッシュ連続', 'C:\\\\書類\\\\提出\\n\\t'),
    ('生の制御文字', 'あ\x00い\x1fう\x7f'),
    ('絵文字と結合文字', '🚨👨‍👩‍👧‍👦 が\u3099'),
    ('サロゲートペア', '𠮷野家'),
    ('改行と引用符の混在', 'A\r\nB"C\'D\n\n"E"'),
    ('長文', 'あ' * 5000),
]
for label, v in NASTY:
    try:
        d = body(B.main("c1", 1, "分類", v, v, v, "5", v, "こころ", "通常", "提案", "はい", 8)["fields"])
        check("サマリー：" + label + " が一字一句復元される", d["summary"] == v and d["needBasis"] == v, repr(d["summary"])[:60])
        check("サマリー：" + label + " で token が乗っ取られない", d["token"] == 'tok"en\\x', d.get("token"))
    except Exception as e:
        check("サマリー：" + label, False, type(e).__name__ + ": " + str(e)[:80])
    try:
        d = body(A.main("追記フォーム回答：" + v, "c1", 2)["fields"])
        check("追記：" + label + " が一字一句復元される", d["addendumText"] == v.strip(), repr(d["addendumText"])[:60])
    except Exception as e:
        check("追記：" + label, False, type(e).__name__ + ": " + str(e)[:80])

print("\n■ fields に生の改行が残っていないか（残ると後段で壊れる）")
for label, v in NASTY:
    f = B.main("c1", 1, "分", v, v, v, "5", v, "こ", "通", "提", "はい", 8)["fields"]
    check("サマリー：" + label, not any(c in f for c in "\r\n\t"), repr(f[:60]))

print("\n■ 最高必要度の計算")
cases = [("5", 8, "8"), ("9", 3, "9"), ("", "", ""), (None, None, ""), ("0", 0, ""),
         ("10", "10", "10"), ("7.9", 0, "7"), ("あ", 4, "4"), ("-3", 0, ""), ("  6  ", 0, "6")]
for sn, mx, want in cases:
    got = body(B.main("c1", 1, "", "", "", "", sn, "", "", "", "", "", mx)["fields"])["maxSupportNeed"]
    check("support_need=%r max_need=%r → %r" % (sn, mx, want), got == want, got)

print("\n■ 入口フォーム判定（stage）")
from_index = "呼び名：さやか／年代：30代／性別：女性／都道府県：秋田県／一番の悩み：仕事"
stage_cases = [
    (from_index, "intake", "index.html が実際に送る形"),
    ("呼び名：さやか", "chat", "呼び名だけ"),
    ("都道府県：秋田県に住んでいます", "chat", "都道府県だけ"),
    ("友人が「呼び名：ポチ」で「都道府県：東京都」と言っていた", "intake", "会話文に両方が含まれる場合"),
    ("", "chat", "空"),
    ("相談を再開します", "chat", "再開の合図"),
]
for q, want, label in stage_cases:
    got = I.main(q, "c1", 1, *[""]*11, 0)["stage"]
    check("%s → %s" % (label, want), got == want, got)

print("\n■ 追記の前置き外し")
add_cases = [
    ("追記フォーム回答：受付しました", "受付しました", "form2.html が実際に送る合図"),
    ("追記フォーム回答：\n本文です", "本文です", "改行のあとに本文"),
    ("追記フォーム回答:半角コロン", "追記フォーム回答:半角コロン", "半角コロンは外れない"),
    (" 追記フォーム回答：前に空白", " 追記フォーム回答：前に空白".strip(), "前に空白があると外れない"),
]
for q, want, label in add_cases:
    got = A.main(q, "c1", 1)["addendum_text"]
    check("%s → %r" % (label, want), got == want, repr(got))

print("\n■ すべて None / 欠損")
for name, fn in [("サマリー", lambda: B.main(*(None,)*13)),
                 ("追記", lambda: A.main(None, None, None)),
                 ("初回受付", lambda: I.main(*(None,)*15))]:
    try:
        r = fn(); body(r["fields"]); check(name + "：Noneでも落ちずJSONとして成立", True)
    except Exception as e:
        check(name + "：Noneでも落ちない", False, type(e).__name__ + ": " + str(e)[:80])

print("\n■ 退避用Slack本文（rescue）")
for name, r in [("サマリー", B.main("c1", 1, "分", "課題", 'A"B\nC', "対応", "9", "根拠\n改行", "こ", "通", "提", "はい", 9)),
                ("追記", A.main('追記フォーム回答：本文"引用"\n改行', "c1", 2))]:
    try:
        t = json.loads(r["rescue"])["text"]
        check(name + "：rescue が JSON として成立", True)
        check(name + "：rescue に生の改行が無い", "\n" not in r["rescue"] and "\r" not in r["rescue"])
        check(name + "：本文が含まれる", ('A"B' in t) or ('本文"引用"' in t), t[:80])
    except Exception as e:
        check(name + "：rescue", False, type(e).__name__ + ": " + str(e)[:80])

print("\n" + "-"*50)
print("不合格 %d 件" % ng)
