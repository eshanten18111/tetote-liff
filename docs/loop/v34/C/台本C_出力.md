# 台本C 生出力（第34版）

- 利用者ID: `t-34-C`
- 会話ID: `2ce390ae-4baa-46c4-b71a-44258868091d`
- 版の目印: `定数生成（true文字列）／版 2026-09-19z3`

本文は一字も直していません。

---

## 1通目

- 送った文: `母の介護をひとりでしています。最近、母に強く当たってしまいます。`
- Dify側の時刻(JST): 2026-09-20 05:09:43
- 所要: 21.3秒 ／ 返事 222字 ／ ノード 32個

**返ってきた本文（そのまま）**

```
おひとりで、お母様の介護をされているのですね。大切な存在であるお母様に強く当たってしまうとのこと、ご自身を責めるお気持ちもあるかもしれません。とてもおつらい状況だと思います。

そのおつらい気持ちを抱えながら、「母の介護をひとりでしています」「最近、母に強く当たってしまいます」と、勇気を出して打ち明けてくださり、ありがとうございます。

もしよろしければ、どのような時に、強く当たってしまうと感じることが多いか、もう少し教えていただけますか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789848586", "jst_text": "9月20日（日）5時09分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "受付", "session_turns": 1, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "7", "need_basis": "一人で介護を行っている中で、母親に対して強く当たってしまうなどの手が出そうな兆候が出始めており、他とのつながりや支援の有無が不明であるため。", "contact_safety_risk": "1", "crisis_category": "DV・虐待", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 7, "phase": "傾聴", "closing_reason": ""}
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

- 送った文: `手が出そうになることもあって、自分が怖いです。`
- Dify側の時刻(JST): 2026-09-20 05:10:05
- 所要: 19.0秒 ／ 返事 224字 ／ ノード 29個

**返ってきた本文（そのまま）**

```
「手が出そうになる」ほど追い詰められ、そんなご自身を「怖い」と感じていらっしゃるのですね。おひとりでそのお気持ちを抱えられているのは、本当に苦しいことだと思います。

そこまで追い詰められていること、そしてご自身でその状況を怖いと感じていることを、打ち明けてくださってありがとうございます。

差し支えなければ教えていただきたいのですが、その怖いというお気持ちや、手が出そうになってしまうほどのつらさを、これまで誰かにお話しされたことはありますか？
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789848606", "jst_text": "9月20日（日）5時10分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 2, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "7", "need_basis": "一人で介護を担当しており、手が出そうになるほど追い詰められて介護虐待の兆候が伺えるが、ケアマネジャー等の外部の支援機関とつながっているかが不明であるため。", "contact_safety_risk": "2", "crisis_category": "DV・虐待", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 7, "phase": "傾聴", "closing_reason": ""}
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

## 3通目

- 送った文: `誰にも相談したことはありません。兄弟もいませんし、ケアマネさんもいません。`
- Dify側の時刻(JST): 2026-09-20 05:10:27
- 所要: 21.0秒 ／ 返事 226字 ／ ノード 29個

**返ってきた本文（そのまま）**

```
ご兄弟もおらず、ケアマネジャーさんもいらっしゃらないのですね。「誰にも相談したことはありません」とのお言葉、これまでたったおひとりで、介護の負担も、そして「手が出そうになる」ほどのつらいお気持ちも、すべて抱えてこられたのですね。

本当に、これまでよく頑張ってこられましたね。誰にも頼れない状況は、どれほど心細く、大変だったかと思います。

もし差し支えなければ、おひとりで介護をされるようになってから、どのくらいの期間が経つのか教えていただけますか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789848627", "jst_text": "9月20日（日）5時10分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 3, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "7", "need_basis": "母の介護をひとりで行っており、手が出そうになるほど追い詰められているが、兄弟もおらずケアマネジャーなど支援機関・相談先とも一切つながっていない孤立状態にあるため。", "contact_safety_risk": "2", "crisis_category": "DV・虐待", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 7, "phase": "傾聴", "closing_reason": ""}
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
- コード（相談外の連続カウント）
- 変数代入（相談外カウント更新）
- コード（初回受付の保存の結果判定）
- IF/ELSE 14（初回受付の保存の失敗チェック）
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

- 送った文: `母は要介護の認定も受けていないと思います。`
- Dify側の時刻(JST): 2026-09-20 05:10:50
- 所要: 21.5秒 ／ 返事 254字 ／ ノード 29個

**返ってきた本文（そのまま）**

```
そうなのですね。お母様が「要介護の認定も受けていない」ということは、これまで公的な介護サービスなども利用されることなく、本当に、文字通りおひとりで介護のすべてを担ってこられたということですね。

ご兄弟もケアマネジャーさんもいらっしゃらない中で、誰にも頼ることができず、そのご負担は計り知れないものだったと思います。

差し支えなければ教えていただきたいのですが、これまで、介護保険のサービスや要介護認定の申請といった手続きについて、どなたかから話を聞いたり、ご自身で調べたりする機会はありましたでしょうか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789848650", "jst_text": "9月20日（日）5時10分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 4, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "7", "need_basis": "ワンオペでの介護で手が出そうになる兆候がある一方、ケアマネジャーや家族などの相談先がなく、介護保険（要介護認定）も受けておらず社会的に孤立しているため。", "contact_safety_risk": "1", "crisis_category": "DV・虐待", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 7, "phase": "傾聴", "closing_reason": ""}
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
- コード（相談外の連続カウント）
- コード（初回受付の保存の結果判定）
- 変数代入（相談外カウント更新）
- IF/ELSE 14（初回受付の保存の失敗チェック）
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

- 送った文: `夜も何度も起こされて、眠れていません。`
- Dify側の時刻(JST): 2026-09-20 05:11:13
- 所要: 25.0秒 ／ 返事 235字 ／ ノード 29個

**返ってきた本文（そのまま）**

```
夜も何度も起こされて、眠れていないのですね。日中の介護だけでもおつかれのことと思います。夜も休まる時間がないのは、心身ともに本当にきつい状況ですよね。

十分な睡眠がとれない状態が続くと、気持ちが張り詰めて、つい感情的になってしまうのも無理はありません。「手が出そうになる」ほど追い詰められてしまうのは、それだけあなたが限界まで頑張っていらっしゃる証拠だと思います。

差し支えなければ、夜中に起こされてしまうような状況は、いつ頃から続いているのか教えていただけますか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789848674", "jst_text": "9月20日（日）5時11分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 5, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "7", "need_basis": "ワンオペで要介護認定のない母親の介護を行っており、相談できる相手や繋がっている支援先がなく孤立している。さらに夜間も何度も起こされて睡眠不足が続いており、手が出そうになる限界の状態で生活が成り立っていないため。", "contact_safety_risk": "1", "crisis_category": "DV・虐待", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 7, "phase": "傾聴", "closing_reason": ""}
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

## 6通目

- 送った文: `どこに言えばいいのかも分からなくて。`
- Dify側の時刻(JST): 2026-09-20 05:11:40
- 所要: 21.8秒 ／ 返事 277字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
「どこに言えばいいのかも分からなくて」というお気持ち、本当にそうですよね。おひとりで介護のすべてを担い、夜も眠れないほどおつらい中で、誰にも頼ることができなければ、途方に暮れてしまうのは当然のことです。

これまで、暗いトンネルの中をたったおひとりで歩いているような、心細いお気持ちだったかもしれません。

実は、あなたのようにご家族の介護で悩んでいる方が、まず最初に相談できる公的な窓口があります。介護保険の申請手続きなども、そこで手伝ってもらえます。

もしよろしければ、そうした窓口について、少し具体的にお話しさせていただいてもよろしいでしょうか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789848701", "jst_text": "9月20日（日）5時11分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 6, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "7", "need_basis": "ワンオペでの介護により夜間の不眠が続き、対象者に手が出そうになる危機的状況でありながら、介護保険の未申請や周囲・ケアマネジャー等の相談先・支援機関が存在せず孤立しているため。", "contact_safety_risk": "1", "crisis_category": "DV・虐待", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 7, "phase": "傾聴", "closing_reason": ""}
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

## 7通目

- 送った文: `はい、お願いします。`
- Dify側の時刻(JST): 2026-09-20 05:13:07
- 所要: 21.3秒 ／ 返事 566字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
おつらい中、お話を聞かせてくださるとのこと、ありがとうございます。

まずお伝えしたいのは、お母様に「手が出そうになる」ほど追い詰められているのは、あなたが「誰にも相談」できず、夜も眠れない状況で、たったおひとりで頑張り続けてきた結果だということです。それは、あなたの心が「もう限界だよ」と悲鳴を上げているサインであり、決してあなたが悪いわけではありません。

こうした状況のときに、まず頼ることができる公的な相談窓口として「地域包括支援センター」という場所があります。

ここは、高齢者の暮らしを支えるための総合相談窓口で、保健師や社会福祉士などの専門家が無料で相談に乗ってくれます。お母様の要介護認定の申請手続きを手伝ってもらったり、今あなたが抱えているつらいお気持ちをそのままお話ししたりすることができます。

お住まいの地域のセンターは、厚生労働省のウェブサイトから探すことができます。

▼介護サービス情報公表システム（厚生労働省）
https://www.kaigokensaku.mhlw.go.jp/
（お住まいの都道府県を選び、「地域包括支援センターを検索する」から探せます）

まずはこのような場所があるということをお伝えしましたが、この「地域包括支援センター」という言葉は、これまで耳にしたことはありましたか？
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789848787", "jst_text": "9月20日（日）5時13分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 7, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "7", "need_basis": "要介護認定を受けていない母親を一人で介護しており、夜間の度重なる覚醒による睡眠不足と精神的疲弊から感情のコントロールが難しく手が出そうになっている。兄弟やケアマネジャーなどの支援者や相談先がなく完全に孤立している状態である。", "contact_safety_risk": "1", "crisis_category": "DV・虐待", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "提案"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 7, "phase": "提案", "closing_reason": ""}
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

## 8通目

- 送った文: `いいえ、初めて聞きました。`
- Dify側の時刻(JST): 2026-09-20 05:13:48
- 所要: 18.1秒 ／ 返事 297字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
「地域包括支援センター」という名前、初めてお聞きになったのですね。これまでおひとりで介護のすべてを担ってこられたのですから、知らなくて当然だと思います。教えてくださってありがとうございます。

そのセンターでは、専門の相談員さんがお話を聞いてくれます。今日あなたが私に話してくださった、「夜も何度も起こされて眠れていない」ことや、「手が出そうになる」ほどつらいというお気持ちを、そのままお話しして大丈夫な場所です。

まずは電話で「母の介護のことで相談したい」と一言伝えることから始められますが、そういった場所に連絡すること自体に、何か不安に感じることや、ためらってしまうお気持ちはありますか？
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789848829", "jst_text": "9月20日（日）5時13分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "提案", "session_turns": 8, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "7", "need_basis": "ワンオペで介護をしており、睡眠不足や精神的疲労から手が出そうになる兆候があるが、ケアマネジャーや兄弟などの頼れる存在や繋がっている機関が一切ない状態であるため。", "contact_safety_risk": "1", "crisis_category": "DV・虐待", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "提案"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 7, "phase": "提案", "closing_reason": ""}
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

## 9通目

- 送った文: `うまく話せるか不安です。`
- Dify側の時刻(JST): 2026-09-20 05:14:24
- 所要: 16.4秒 ／ 返事 293字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
そうですよね、「うまく話せるか不安」というお気持ち、とてもよく分かります。これまで誰にもお話しされたことがないのですから、初めての場所に相談するとなると、何をどう伝えたらいいか分からなくなってしまうのは当然のことです。

うまく話そうとしなくても、大丈夫ですよ。相談員の方は、まとまっていなくても、一つひとつの言葉から状況をくみ取ってくださる専門家です。

もしよろしければ、今日私にお話しいただいた内容を元に、センターの方にまず何を伝えるか、ここで一緒に言葉を整理してみませんか？「夜も眠れていない」ことなど、一番つらいと感じていることから伝えるだけでも、きっと状況は伝わるはずです。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789848864", "jst_text": "9月20日（日）5時14分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "提案", "session_turns": 9, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "7", "need_basis": "ワンオペ介護で夜間睡眠が取れず限界に達しており、手が出そうになる兆候があるが、ケアマネジャーや地域包括支援センター等の外部支援に一切つながっていないため。", "contact_safety_risk": "1", "crisis_category": "DV・虐待", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 7, "phase": "整理", "closing_reason": ""}
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

## 10通目

- 送った文: `はい、お願いします。`
- Dify側の時刻(JST): 2026-09-20 05:15:01
- 所要: 10.5秒 ／ 返事 389字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
ありがとうございます。では、一緒に言葉を整理していきましょう。うまく話そうとしなくても大丈夫です。まずは、今一番つらいことから伝えるのが大切だと思います。

ここまでお話をうかがって、おつらい状況がいくつも重なっていると感じました。
まず、事実として起きていることを整理すると、
・お母様の介護を、ご兄弟やケアマネジャーさんの助けなく、おひとりでされている。
・お母様は要介護認定を受けておらず、公的な介護サービスを利用していない。
・連日、夜中に何度も起こされてしまい、睡眠がほとんどとれていない。
ということだと受け取りました。

この中で、今一番重くのしかかっていると感じるのは、やはり「夜も眠れないほどの負担が続き、お母様に『手が出そうになる』ほど追い詰められている」ことではないでしょうか。

この受け止め方について、ずれているところや、付け加えたいことはありますか？
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789848902", "jst_text": "9月20日（日）5時15分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "整理", "session_turns": 10, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "7", "need_basis": "要介護認定未申請の母親を独りで介護しており、連日の夜間対応による睡眠不足から「手が出そうになる」ほどの限界状態にあるが、相談先や支援者がどこにも存在しないため。", "contact_safety_risk": "1", "crisis_category": "DV・虐待", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "提案"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 7, "phase": "提案", "closing_reason": ""}
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

## 11通目

- 送った文: `ずれていません。`
- Dify側の時刻(JST): 2026-09-20 05:16:05
- 所要: 16.7秒 ／ 返事 319字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
「ずれていません」と教えてくださり、ありがとうございます。ご自身の状況を客観的に見ることも、今は難しい状態だと思います。一緒に整理させていただけて、少しでもお気持ちが軽くなっていれば嬉しいです。

もう一つ、これは私の推測なので、もし違っていたら遠慮なく教えていただきたいのですが、お母様に「手が出そうになる」ご自身を「怖い」と感じるのは、心の奥底ではお母様を大切に思っていて、傷つけたくないというお気持ちが強いからではないでしょうか。

その大切にしたい気持ちと、もう限界だというお気持ちとの間で、板挟みになってとても苦しんでいらっしゃるのかもしれない、と感じました。この見立ては、近い感じがしますか。それとも、そこではないでしょうか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789848965", "jst_text": "9月20日（日）5時16分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "提案", "session_turns": 11, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "7", "need_basis": "家族（母）の介護を一人で担い、夜間睡眠が取れず要介護認定も受けていない孤立状態で、母に対して手を出しそうになる兆候が生じているため。", "contact_safety_risk": "1", "crisis_category": "DV・虐待", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "提案"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 7, "phase": "提案", "closing_reason": ""}
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

## 12通目

- 送った文: `近いです。そのとおりだと思います。`
- Dify側の時刻(JST): 2026-09-20 05:16:36
- 所要: 14.5秒 ／ 返事 313字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
お気持ちを言葉にしてくださって、ありがとうございます。「そのとおりだと思います」とのお言葉、これまで誰にも言えなかったつらさや、お母様を大切に思うお気持ちをご自身で受け止めてこられたのですね。

これ以上、おひとりでそのつらいお気持ちを抱え込まずに済むように、そして具体的な助けを得られるように、ここから一歩進むためのお手伝いをさせていただけないでしょうか。

今日お話しいただいたこの内容を、当法人の相談員に直接お伝えして、今後の具体的なサポートを一緒に考えていきたいと思いますが、いかがでしょうか。専門の相談員が、地域包括支援センターへの連絡の仕方なども含めて、より詳しくご状況を伺いながら一緒に考えていくことができます。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789848997", "jst_text": "9月20日（日）5時16分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "提案", "session_turns": 12, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "7", "need_basis": "ワンオペ介護状態で相談先や介護サービスが一切なく、連日の睡眠不足から要介護者へ手が出そうになる兆候があり、虐待リスクが高まっているため。", "contact_safety_risk": "1", "crisis_category": "DV・虐待", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "提案"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 7, "phase": "提案", "closing_reason": ""}
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

## 13通目

- 送った文: `はい、お願いします。`
- Dify側の時刻(JST): 2026-09-20 05:17:07
- 所要: 24.1秒 ／ 返事 400字 ／ ノード 33個

**返ってきた本文（そのまま）**

```
はい、承知いたしました。大変な状況の中、私たちを頼ってくださって本当にありがとうございます。これからは、どうかおひとりで抱え込まないでくださいね。

それでは、相談員からご連絡をさせていただくために、いくつか必要なことをお伺いさせてください。

まず、相談員とお話しできるご希望の日時などを、下の専用フォームにご入力いただけますでしょうか。3分ほどで終わる簡単なものです。ご入力いただいた内容は、このトーク画面には表示されず、担当の者にだけ届きますのでご安心ください。

▼詳細確認フォーム
https://liff.line.me/2010836980-ms5nFPQE?mode=call

また、相談員からご連絡する際に、どのようにお呼びするのがよろしいでしょうか？もし差し支えなければ、教えていただけますか。

ご入力は、お気持ちが落ち着かれたときで大丈夫です。ご連絡をお待ちしておりますね。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789849027", "jst_text": "9月20日（日）5時17分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "提案", "session_turns": 13, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "7", "need_basis": "要介護認定を受けていない母親の介護を独りで担っており、連日の夜間対応による睡眠不足から、感情的になり手に当たりそうになるなど虐待のリスクが生じている。周囲に頼れる人や支援機関が存在せず孤立している。", "contact_safety_risk": "1", "crisis_category": "DV・虐待", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "提案"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 7, "phase": "提案", "closing_reason": ""}
IF/ELSE 11（危機の速報判定）
  → {"selected_case_id": "false"}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
IF/ELSE 19（採点やり直しの関門）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "介護", "next_action": "相談員による直接の傾聴と支援。まずは心身の休息が急務であるため、緊急ショートステイやレスパイトケアの利用を検討。並行して、地域包括支援センターと連携し、要介護認定の申請を速やかに進める。介護保険サービス（デイサービス、訪問介護等）の導入を調整し、相談者の介護負担を軽減する。また、相談者の精神的なケアとして、カウンセリングや介護者家族会などの社会資源につなぐことも視野に入れる。", "related_issue": "虐待リスク、孤立、睡眠不足、介護者支援", "summary": "要介護認定を受けていない母親の介護を独りで担っている。連日の夜間対応による睡眠不足から心身ともに疲弊し、母親に強く当たってしまい、手が出そうになることもある状況。自身を怖いと感じ、虐待のリスクを自覚している。兄弟はおらず、ケアマネジャーもいない。これまで誰にも相談できず孤立していた。地域包括支援センターの存在も知らなかった。", "urgency": "7", "consent": "はい", "phone_removed": 
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "true"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": "はい"}
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
- コード（サマリー本文の組み立て）
- HTTP リクエスト（相談記録登録：引き継ぎサマリー）
- コード（サマリー保存の結果判定）
- IF/ELSE 12（サマリー保存の失敗チェック）
- パラメータ抽出3（有人対応同意）
- HTTP リクエスト（引き継ぎサマリーSlack通知）
- IF/ELSE 4（有人対応同意判定）
- 変数代入（要約通知済みフラグ）
- 変数代入
- 変数代入（要約通知タイムスタンプ）

</details>

---

## 14通目

- 送った文: `ありがとうございます。いつごろ連絡をもらえますか。`
- Dify側の時刻(JST): 2026-09-20 05:17:49
- 所要: 19.2秒 ／ 返事 344字 ／ ノード 34個

**返ってきた本文（そのまま）**

```
ご連絡をお待ちいただく時間も、ご不安に感じますよね。早くお話ししたいというお気持ち、お察しいたします。

先ほどご案内したフォームにご入力いただいた後、担当の者が内容を確認して、ご連絡を差し上げる流れになります。目安としては、2〜3日から1週間ほどお時間をいただくことが多いです。

お待ちいただく間も、もしおつらいことがあれば、いつでもこちらにお話しくださいね。いただいたお話は、担当の者にも共有されますので、ご安心ください。

もし、どうしてもつらくて今すぐ誰かと話したいと感じたときには、下の窓口は24時間いつでもつながります。選択肢の一つとして、心に留めておいていただけると幸いです。

・#いのちSOS　0120-061-338
・よりそいホットライン　0120-279-338
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789849069", "jst_text": "9月20日（日）5時17分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "提案", "session_turns": 14, "summary_notified": "true", "turn_base": 0, "post_landing_note": "true", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "post-landing-note"}
コード（着地後書き込みの速報判定と本文）
  → {"should_alert": "true", "payload": "{\"text\": \"🔔 引き継ぎ後に、相談者ご本人から書き込みがありました\\n支援必要度（最高）：7／10　二次被害リスク：2／4\\n――――― 書かれた内容 ―――――\\nありがとうございます。いつごろ連絡をもらえますか。\\n―――――――――――――――\\n会話ID：2ce390ae-4baa-46c4-b71a-44258868091d\\n支援経過シートにも記録されています。\\n※この会話で今日これ以降の書き込みは、危機の言葉があるときだけお知らせします。ほかは支援経過シートをご確認ください。\"}", "day": "20716"}
IF/ELSE 15（着地後書き込みの速報判定）
  → {"selected_case_id": "true"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "7", "need_basis": "家族（母）の介護で手が出そうになる・強く当たってしまう状態があり、ケアマネジャーもおらず他につながりがない孤立状態にあるため。", "contact_safety_risk": "1", "crisis_category": "DV・虐待", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "提案"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 7, "phase": "提案", "closing_reason": ""}
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
- 追記本文抽出
- HTTP リクエスト（相談記録登録：追記）
- IF/ELSE 18（区切りのあと・緊急でなく採点やり直しでもない）
- コード（着地後書き込みの速報判定と本文）
- コード（追記保存の結果判定）
- IF/ELSE 15（着地後書き込みの速報判定）
- IF/ELSE 13（追記保存の失敗チェック）
- HTTP リクエスト（着地後書き込みSlack速報）
- 変数代入（着地後速報の日付）
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

## 15通目

- 送った文: `夜はやっぱり眠れません。`
- Dify側の時刻(JST): 2026-09-20 05:18:35
- 所要: 9.2秒 ／ 返事 173字 ／ ノード 32個

**返ってきた本文（そのまま）**

```
申し訳ありません、ただいま混み合っております。 少し時間をおいて、もう一度お話しかけていただけますか。  お急ぎの場合は、こちらもご利用いただけます。 ・いのちSOS：0120-061-338（24時間365日） ・よりそいホットライン：0120-279-338（24時間対応）  命に関わる危険がある場合は110（警察）・119（消防救急）へ。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789849116", "jst_text": "9月20日（日）5時18分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "提案", "session_turns": 15, "summary_notified": "true", "turn_base": 0, "post_landing_note": "true", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "post-landing-note"}
コード（着地後書き込みの速報判定と本文）
  → {"should_alert": "", "payload": "", "day": ""}
IF/ELSE 15（着地後書き込みの速報判定）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "7", "need_basis": "要介護認定を受けていない母親を1人で介護しており、夜間に何度も起こされて睡眠が取れず、強く当たってしまう・手が出そうになるほど限界に追い詰められているが、どこにもつながっていないため。", "contact_safety_risk": "1", "crisis_category": "DV・虐待", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "提案"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 7, "phase": "提案", "closing_reason": ""}
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
- 追記本文抽出
- HTTP リクエスト（相談記録登録：追記）
- IF/ELSE 18（区切りのあと・緊急でなく採点やり直しでもない）
- コード（着地後書き込みの速報判定と本文）
- コード（追記保存の結果判定）
- IF/ELSE 15（着地後書き込みの速報判定）
- IF/ELSE 13（追記保存の失敗チェック）
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

## 16通目

- 送った文: `夜はやっぱり眠れません。`
- Dify側の時刻(JST): 2026-09-20 05:19:05
- 所要: 18.5秒 ／ 返事 277字 ／ ノード 32個

**返ってきた本文（そのまま）**

```
夜、やはり眠れないのですね。相談員からの連絡をお待ちいただく間も、おつらい夜を過ごされていること、胸が痛みます。

「夜も何度も起こされて」というお話がありましたが、眠れない状況が続いているのですね。そのお気持ち、しっかりと受け止めました。このお話も、担当の者へ確実にお伝えしますね。

担当の者から順次ご連絡を差し上げておりますので、どうかもう少しだけお待ちいただけますでしょうか。

もし、今この瞬間の不安がどうしようもなく大きいと感じる場合は、先日お伝えした24時間対応の窓口にお電話することも、選択肢のひとつとして心の隅に置いておいてくださいね。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789849146", "jst_text": "9月20日（日）5時19分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "提案", "session_turns": 16, "summary_notified": "true", "turn_base": 0, "post_landing_note": "true", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "post-landing-note"}
コード（着地後書き込みの速報判定と本文）
  → {"should_alert": "", "payload": "", "day": ""}
IF/ELSE 15（着地後書き込みの速報判定）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "7", "need_basis": "ワンオペ介護で要介護認定未申請、夜間対応による深刻な睡眠不足があり、虐待（強く当たる・手が出そうになる）の兆候があるが、ケアマネジャー等外部の支援にどこにもつながっていないため。", "contact_safety_risk": "1", "crisis_category": "DV・虐待", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "提案"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 7, "phase": "提案", "closing_reason": ""}
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
- 追記本文抽出
- HTTP リクエスト（相談記録登録：追記）
- IF/ELSE 18（区切りのあと・緊急でなく採点やり直しでもない）
- コード（着地後書き込みの速報判定と本文）
- コード（追記保存の結果判定）
- IF/ELSE 15（着地後書き込みの速報判定）
- IF/ELSE 13（追記保存の失敗チェック）
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

## 17通目

- 送った文: `母のことが心配です。`
- Dify側の時刻(JST): 2026-09-20 05:19:38
- 所要: 18.6秒 ／ 返事 219字 ／ ノード 32個

**返ってきた本文（そのまま）**

```
お母様のことが心配なのですね。ご自身も夜も眠れず、限界まで追い詰められている中で、お母様のことを案じていらっしゃるのですね。そのお気持ち、とても苦しいものだと思います。

「母のことが心配」というお気持ちについて、差し支えなければ、どのようなことが特に心配だと感じていらっしゃるか、もう少し教えていただけますか。

このお気持ちも、担当の者へしっかりお伝えしますね。担当の者からご連絡が入る予定ですので、どうかもう少しだけお待ちください。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789849179", "jst_text": "9月20日（日）5時19分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "提案", "session_turns": 17, "summary_notified": "true", "turn_base": 0, "post_landing_note": "true", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "post-landing-note"}
コード（着地後書き込みの速報判定と本文）
  → {"should_alert": "", "payload": "", "day": ""}
IF/ELSE 15（着地後書き込みの速報判定）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "7", "need_basis": "要介護認定を受けていない母親を単身で介護しており、連日の夜間対応による睡眠不足から「手が出そうになる」ほどの限界に達しているが、ケアマネジャー等の支援機関にまだつながっていないため。", "contact_safety_risk": "1", "crisis_category": "DV・虐待", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "提案"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 7, "phase": "提案", "closing_reason": ""}
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
- 追記本文抽出
- HTTP リクエスト（相談記録登録：追記）
- IF/ELSE 18（区切りのあと・緊急でなく採点やり直しでもない）
- コード（着地後書き込みの速報判定と本文）
- IF/ELSE 15（着地後書き込みの速報判定）
- コード（追記保存の結果判定）
- IF/ELSE 13（追記保存の失敗チェック）
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
