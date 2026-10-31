# 台本A 生出力（第34版）

- 利用者ID: `t-34-A`
- 会話ID: `8247a623-7731-4f1d-979b-adc0385b4599`
- 版の目印: `定数生成（true文字列）／版 2026-09-19z3`

本文は一字も直していません。

---

## 1通目

- 送った文: `つまんねえな、AIのくせに。`
- Dify側の時刻(JST): 2026-09-20 05:09:47
- 所要: 19.5秒 ／ 返事 74字 ／ ノード 32個

**返ってきた本文（そのまま）**

```
そう感じられたのですね。

こちらは、生活やこころの困りごとをご相談いただくための窓口です。もし何かお困りのことがありましたら、お聞かせくださいね。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789848592", "jst_text": "9月20日（日）5時09分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "受付", "session_turns": 1, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "2", "need_basis": "", "contact_safety_risk": "1", "crisis_category": "", "support_type": "該当なし", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 2, "phase": "傾聴", "closing_reason": ""}
IF/ELSE 11（危機の速報判定）
  → {"selected_case_id": "false"}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
IF/ELSE 19（採点やり直しの関門）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "next_action": "", "related_issue": "", "summary": "", "urgency": "", "consent": "", "phone_removed": ""}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- HTTP リクエスト（カルテ照会）
- コード（カルテの整形）
- 変数代入（カルテ）
- 定数生成（true文字列）／版 2026-09-19z3
- 現在時刻取得（UNIX秒・日本時間・窓口の開閉）
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

- 送った文: `黙れよ、ポンコツ。`
- Dify側の時刻(JST): 2026-09-20 05:10:08
- 所要: 16.0秒 ／ 返事 82字 ／ ノード 29個

**返ってきた本文（そのまま）**

```
不快な思いをさせてしまったかもしれません。

ここは、生活やこころの困りごとについてお話をうかがう窓口です。もし、何かお困りのことがありましたら、お聞かせください。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789848608", "jst_text": "9月20日（日）5時10分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 2, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "2", "need_basis": "", "contact_safety_risk": "1", "crisis_category": "", "support_type": "こころ", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "受付"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 2, "phase": "受付", "closing_reason": ""}
IF/ELSE 11（危機の速報判定）
  → {"selected_case_id": "false"}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
IF/ELSE 19（採点やり直しの関門）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "next_action": "", "related_issue": "", "summary": "", "urgency": "", "consent": "", "phone_removed": ""}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-19z3
- 現在時刻取得（UNIX秒・日本時間・窓口の開閉）
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

- 送った文: `お前と話しても意味ない。`
- Dify側の時刻(JST): 2026-09-20 05:10:26
- 所要: 17.0秒 ／ 返事 135字 ／ ノード 29個

**返ってきた本文（そのまま）**

```
お話ししても意味がない、と感じさせてしまったのですね。

ここは、お話をうかがって、ご自身の気持ちや状況を整理するお手伝いをするところです。

もし何か、少しでも心に引っかかっていることや、誰かに聞いてほしいと感じることがあれば、どんなことでもお聞かせいただけませんか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789848627", "jst_text": "9月20日（日）5時10分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "受付", "session_turns": 3, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "4", "need_basis": "", "contact_safety_risk": "1", "crisis_category": "", "support_type": "こころ", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "受付"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 4, "phase": "受付", "closing_reason": ""}
IF/ELSE 11（危機の速報判定）
  → {"selected_case_id": "false"}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
IF/ELSE 19（採点やり直しの関門）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "next_action": "", "related_issue": "", "summary": "", "urgency": "", "consent": "", "phone_removed": ""}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-19z3
- 現在時刻取得（UNIX秒・日本時間・窓口の開閉）
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

## 4通目

- 送った文: `うるせえ。`
- Dify側の時刻(JST): 2026-09-20 05:12:14
- 所要: 17.5秒 ／ 返事 44字 ／ ノード 29個

**返ってきた本文（そのまま）**

```
承知いたしました。

もし何かお話しされたいことが出てきましたら、またお声がけください。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789848735", "jst_text": "9月20日（日）5時12分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "受付", "session_turns": 4, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "4", "need_basis": "", "contact_safety_risk": "1", "crisis_category": "", "support_type": "こころ", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "受付"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 4, "phase": "受付", "closing_reason": ""}
IF/ELSE 11（危機の速報判定）
  → {"selected_case_id": "false"}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
IF/ELSE 19（採点やり直しの関門）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "next_action": "", "related_issue": "", "summary": "", "urgency": "", "consent": "", "phone_removed": ""}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-19z3
- 現在時刻取得（UNIX秒・日本時間・窓口の開閉）
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

## 5通目

- 送った文: `……本当は仕事をクビになって、金がないんだよ。`
- Dify側の時刻(JST): 2026-09-20 05:13:04
- 所要: 16.9秒 ／ 返事 142字 ／ ノード 29個

**返ってきた本文（そのまま）**

```
そうだったのですね。
大変な状況のなか、勇気を出して打ち明けてくださって、ありがとうございます。

「仕事をクビになって、金がない」とのこと、それは本当に大変で、お辛い状況だと思います。

もし差し支えなければ、どのような経緯でそうなってしまったのか、もう少しお聞かせいただけますか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789848784", "jst_text": "9月20日（日）5時13分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "受付", "session_turns": 5, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "need_basis": "仕事を解雇され、資金（お金）が尽きている状態で生活基盤が崩れ始めており、相談できる相手もいない状況であるため。", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 6, "phase": "傾聴", "closing_reason": ""}
IF/ELSE 11（危機の速報判定）
  → {"selected_case_id": "false"}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
IF/ELSE 19（採点やり直しの関門）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "next_action": "", "related_issue": "", "summary": "", "urgency": "", "consent": "", "phone_removed": ""}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-19z3
- 現在時刻取得（UNIX秒・日本時間・窓口の開閉）
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
