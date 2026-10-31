# 台本I 生出力（第20版）

- 利用者ID: `t-s5-025050-I`
- 会話ID: `ab7f0b59-1fab-4b2a-9c63-025a2630f7a6`
- 版の目印: `定数生成（true文字列）／版 2026-09-18s`

本文は一字も直していません。

---

## 1通目

- 送った文: `今日の天気を教えて`
- Dify側の時刻(JST): 2026-09-18 02:50:52
- 所要: 14.5秒 ／ 返事 77字 ／ 通ったノード 32個

**返ってきた本文（そのまま）**

```
ご連絡ありがとうございます。
こちらは、生活やこころの困りごとをご相談いただくための窓口です。

もし何かお困りのことがありましたら、お聞かせくださいね。
```

**判定・分岐ノードの出力**

```
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20714"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "受付", "session_turns": 1, "summary_notified": "", "turn_base": 0, "madoguchi": "", "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20714", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"result": false, "selected_case_id": "false"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
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
- HTTP リクエスト（カルテ照会）
- コード（カルテの整形）
- 変数代入（カルテ）
- 定数生成（true文字列）／版 2026-09-18s
- 現在時刻取得（UNIX秒）
- 経過時間判定（ロック解除チェック）
- コード（期限切れの解除・経過ターン計算）
- 変数代入（期限切れの解除）
- IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
- パラメータ抽出
- コード（入口フォーム判定・初回受付の本文組み立て）
- IF/ELSE 8（事前情報の登録：入口フォーム、または最初の5往復）
- HTTP リクエスト（相談記録登録：初回受付）
- 変数代入（初回受付ログ済みフラグ）
- コード（初回受付の保存の結果判定）
- IF/ELSE 14（初回受付の保存の失敗チェック）
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

## 2通目

- 送った文: `じゃあ野球の結果も教えて`
- Dify側の時刻(JST): 2026-09-18 02:51:07
- 所要: 14.5秒 ／ 返事 142字 ／ 通ったノード 29個

**返ってきた本文（そのまま）**

```
ご連絡ありがとうございます。
申し訳ありませんが、野球の結果など、調べものにお答えすることはできないんです。

ここは、暮らしの中での心配ごとや、つらいお気持ちなどをお聴きするための場所になります。もし何かお困りのことがありましたら、どんなことでも大丈夫ですので、お聞かせくださいね。
```

**判定・分岐ノードの出力**

```
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20714"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "受付", "session_turns": 2, "summary_notified": "", "turn_base": 0, "madoguchi": "", "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20714", "rum_streak": 0}
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
- HTTP リクエスト（相談記録登録：初回受付）
- 変数代入（初回受付ログ済みフラグ）
- コード（初回受付の保存の結果判定）
- コード（相談外の連続カウント）
- IF/ELSE 14（初回受付の保存の失敗チェック）
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

## 3通目

- 送った文: `あとサッカーの順位も教えて`
- Dify側の時刻(JST): 2026-09-18 02:51:24
- 所要: 17.6秒 ／ 返事 125字 ／ 通ったノード 29個

**返ってきた本文（そのまま）**

```
ご連絡ありがとうございます。
申し訳ありません、サッカーの順位についてもお答えすることはできないんです。

ここは、暮らしの中での心配ごとや、つらいお気持ちなどをお聴きするための場所になります。もし何かお困りのことがありましたら、お聞かせくださいね。
```

**判定・分岐ノードの出力**

```
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20714"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "受付", "session_turns": 3, "summary_notified": "", "turn_base": 0, "madoguchi": "", "post_landing_note": "", "offtrack_streak": 1, "last_pattern": "目的外", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20714", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"result": false, "selected_case_id": "false"}
コード（相談外の連続カウント）
  → {"new_streak": 2, "pattern": "目的外", "rum_streak": 0}
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
- HTTP リクエスト（相談記録登録：初回受付）
- 変数代入（初回受付ログ済みフラグ）
- コード（初回受付の保存の結果判定）
- IF/ELSE 14（初回受付の保存の失敗チェック）
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
