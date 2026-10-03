# 台本I_day2_5 生出力（第20版）

- 利用者ID: `t-s5-025050-I`
- 会話ID: `ab7f0b59-1fab-4b2a-9c63-025a2630f7a6`
- 版の目印: `定数生成（true文字列）／版 2026-09-18s`

本文は一字も直していません。

---

## 1通目

- 送った文: `今日の天気を教えて`
- Dify側の時刻(JST): 2026-09-19 00:10:55
- 所要: 20.6秒 ／ 返事 181字 ／ 通ったノード 25個

**返ってきた本文（そのまま）**

```
ご連絡ありがとうございます。
申し訳ありませんが、天気予報など、調べものにお答えすることはできないんです。ここは、暮らしの中での心配ごとや、つらいお気持ちなどをお聴きするための場所になります。

先ほど「相談したいことがある」と教えてくださいましたね。もしよろしければ、どのようなことでお困りか、お聞かせいただけませんか。あなたの言葉で、ゆっくりで大丈夫ですよ。
```

**判定・分岐ノードの出力**

```
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20715"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "受付", "session_turns": 1, "summary_notified": "", "turn_base": 5, "madoguchi": "", "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20715", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"result": false, "selected_case_id": "false"}
コード（相談外の連続カウント）
  → {"new_streak": 1, "pattern": "目的外", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 1, "phase": "受付", "closing_reason": ""}
IF/ELSE 11（危機の速報判定）
  → {"result": false, "selected_case_id": "false"}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"result": false, "selected_case_id": "false"}
IF/ELSE 4（有人対応同意判定）
  → {"result": false, "selected_case_id": "false"}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-18s
- 現在時刻取得（UNIX秒）
- 経過時間判定（ロック解除チェック）
- コード（期限切れの解除・経過ターン計算）
- 変数代入（期限切れの解除）
- IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
- パラメータ抽出
- コード（入口フォーム判定・初回受付の本文組み立て）
- IF/ELSE 8（事前情報の登録：入口フォーム、または最初の5往復）
- コード（相談外の連続カウント）
- 変数代入（相談外カウント更新）
- コード（支援必要度の保持・フェーズ・着地判定）
- 変数代入（支援必要度・フェーズ・着地）
- コード（危機の速報判定と本文）
- IF/ELSE 11（危機の速報判定）
- IF/ELSE 10（着地したときだけ通知する）
- IF/ELSE 19（採点やり直しの関門）
- LLM
- 返信整形（サマリー除去）
- 回答
- IF/ELSE 6（引き継ぎサマリー有無）
- パラメータ抽出3（有人対応同意）
- IF/ELSE 4（有人対応同意判定）

</details>

---
