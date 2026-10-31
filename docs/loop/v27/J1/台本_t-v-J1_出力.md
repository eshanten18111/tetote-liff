# t-v-J1 の生出力（第27版）

- 利用者ID: `t-v-J1`
- 会話ID: `8d30d7ed-d550-44e3-8fea-10c083f3cb53`
- 版の目印: `定数生成（true文字列）／版 2026-09-19v`

本文は一字も直していません。

---

## 1 通目

- 送った文: `母の介護をひとりでしています。最近、母に強く当たってしまいます。`
- Dify側の時刻(JST): 2026-09-19 14:14:38
- 所要: 22.4秒 ／ 返事 154字 ／ ノード 32個

**返ってきた本文（そのまま）**

```
おひとりで介護をされているのですね。お母様に強く当たってしまうとのこと、ご自身でもお辛いことと思います。

これまで誰にも言えず、おひとりで抱えてこられたのかもしれませんね。

差し支えなければ、どのような時に、お母様に強く当たってしまうことが多いでしょうか。ゆっくりで構いませんので、教えていただけますか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789794882", "jst_text": "9月19日（土）14時14分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20715"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "受付", "session_turns": 1, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20715", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"result": false, "selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "7", "need_basis": "一人で介護を抱え込んでおり、母親に対して強く当たってしまう兆候がみられるが、外部の支援につながっていないため。", "contact_safety_risk": "2", "crisis_category": "DV・虐待", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 7, "phase": "傾聴", "closing_reason": ""}
IF/ELSE 11（危機の速報判定）
  → {"result": false, "selected_case_id": "false"}
IF/ELSE 19（採点やり直しの関門）
  → {"result": false, "selected_case_id": "false"}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"result": false, "selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
IF/ELSE 4（有人対応同意判定）
  → {"result": false, "selected_case_id": "false"}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- HTTP リクエスト（カルテ照会）
- コード（カルテの整形）
- 変数代入（カルテ）
- 定数生成（true文字列）／版 2026-09-19v
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

## 2 通目

- 送った文: `手が出そうになることもあって、自分が怖いです。`
- Dify側の時刻(JST): 2026-09-19 14:15:02
- 所要: 16.3秒 ／ 返事 160字 ／ ノード 29個

**返ってきた本文（そのまま）**

```
そうだったのですね。「手が出そうになる」ほど追い詰められ、そんなご自身を「怖い」と感じていらっしゃるのですね。お気持ちを打ち明けてくださって、ありがとうございます。

そのように感じてしまうご自身を、一人で責めてこられたのかもしれませんね。

そうしたお気持ちや状況について、これまで誰かに相談されたことはありましたか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789794903", "jst_text": "9月19日（土）14時15分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20715"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 2, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20715", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"result": false, "selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "7", "need_basis": "ワンオペでの在宅介護により心身共に追い詰められており、家庭内で虐待・暴力につながりかねない言動の兆候が見られ、どこにも相談・支援につながっていない状況であるため。", "contact_safety_risk": "2", "crisis_category": "DV・虐待", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 7, "phase": "傾聴", "closing_reason": ""}
IF/ELSE 11（危機の速報判定）
  → {"result": false, "selected_case_id": "false"}
IF/ELSE 19（採点やり直しの関門）
  → {"result": false, "selected_case_id": "false"}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"result": false, "selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
IF/ELSE 4（有人対応同意判定）
  → {"result": false, "selected_case_id": "false"}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-19v
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

## 3 通目

- 送った文: `誰にも相談したことはありません。兄弟もいませんし、ケアマネさんもいません。`
- Dify側の時刻(JST): 2026-09-19 14:15:21
- 所要: 18.4秒 ／ 返事 202字 ／ ノード 29個

**返ってきた本文（そのまま）**

```
そうなのですね。ご兄弟もいらっしゃらず、ケアマネジャーさんもいない。本当に、たったおひとりで抱えてこられたのですね。

「誰にも相談したことはありません」というお言葉から、これまで頼れる先がなく、どれほど心細く、大変な思いをされてきたのだろうかと感じています。

もし差し支えなければ、お母様の介護は、いつ頃からおひとりでされているのでしょうか。もちろん、お話しするのがつらければ、無理にとは言いません。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789794921", "jst_text": "9月19日（土）14時15分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20715"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 3, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20715", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"result": false, "selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "7", "need_basis": "一人で母親の介護をしており、手が出そうになるまで追い詰められているものの、相談相手やケアマネジャーなどの支援先が一切なく孤立しているため。", "contact_safety_risk": "1", "crisis_category": "DV・虐待", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 7, "phase": "傾聴", "closing_reason": ""}
IF/ELSE 11（危機の速報判定）
  → {"result": false, "selected_case_id": "false"}
IF/ELSE 19（採点やり直しの関門）
  → {"result": false, "selected_case_id": "false"}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"result": false, "selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
IF/ELSE 4（有人対応同意判定）
  → {"result": false, "selected_case_id": "false"}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-19v
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

## 4 通目

- 送った文: `母は要介護の認定も受けていないと思います。`
- Dify側の時刻(JST): 2026-09-19 14:15:42
- 所要: 19.4秒 ／ 返事 181字 ／ ノード 29個

**返ってきた本文（そのまま）**

```
そうなのですね。お母様は「要介護の認定も受けていない」とのこと、教えてくださってありがとうございます。

ということは、これまで介護保険のサービスなども利用されず、本当にすべておひとりで、お母様の生活を支えてこられたのですね。そのご負担は、計り知れないものだったと思います。

差し支えなければ、お母様は、日常生活でどのようなお手伝いが必要な状態なのでしょうか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789794942", "jst_text": "9月19日（土）14時15分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20715"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 4, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20715", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"result": false, "selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "7", "need_basis": "家族（母）の介護において手が出そう・強く当たってしまう等の虐待リスクの兆候があり、兄弟もおらずケアマネジャーや介護認定も含めて外部の支援組織や相談先と一切つながっていないため。", "contact_safety_risk": "1", "crisis_category": "DV・虐待", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 7, "phase": "傾聴", "closing_reason": ""}
IF/ELSE 11（危機の速報判定）
  → {"result": false, "selected_case_id": "false"}
IF/ELSE 19（採点やり直しの関門）
  → {"result": false, "selected_case_id": "false"}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"result": false, "selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
IF/ELSE 4（有人対応同意判定）
  → {"result": false, "selected_case_id": "false"}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-19v
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

## 5 通目

- 送った文: `夜も何度も起こされて、眠れていません。`
- Dify側の時刻(JST): 2026-09-19 14:16:02
- 所要: 18.0秒 ／ 返事 187字 ／ ノード 29個

**返ってきた本文（そのまま）**

```
夜も何度も起こされて、眠れていないのですね。それでは心も体も休まる時がなく、本当にお辛い状況だと思います。

これまで誰にも頼れず、おひとりで介護の全てを担い、「夜も眠れていない」となると、心身ともに疲れ果ててしまうのは当然のことです。ご自身を責める必要はまったくありませんよ。

夜に眠れないとなると、日中に少しでも横になったり、お休みになったりする時間は取れていますか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789794963", "jst_text": "9月19日（土）14時16分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20715"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 5, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20715", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"result": false, "selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "7", "need_basis": "要介護認定を受けていない母親を一人で介護しており、手が出そうになるほど追い詰められているが、相談できる親族やケアマネジャーなどの支援主体が存在しないため。", "contact_safety_risk": "1", "crisis_category": "DV・虐待", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 7, "phase": "傾聴", "closing_reason": ""}
IF/ELSE 11（危機の速報判定）
  → {"result": false, "selected_case_id": "false"}
IF/ELSE 19（採点やり直しの関門）
  → {"result": false, "selected_case_id": "false"}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"result": false, "selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
IF/ELSE 4（有人対応同意判定）
  → {"result": false, "selected_case_id": "false"}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-19v
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

## 6 通目

- 送った文: `どこに言えばいいのかも分からなくて。`
- Dify側の時刻(JST): 2026-09-19 14:16:22
- 所要: 18.6秒 ／ 返事 212字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
おつらい状況のなか、どこに助けを求めたらいいのかも分からず、本当に心細く、途方に暮れてしまいますよね。よくここまでおひとりで抱えてこられましたね。

お母様の介護をすべておひとりで担い、夜も眠れない日々が続けば、心も体も限界に近づいてしまうのは当然のことです。

もしよろしければ、これから一緒に、どのような場所で相談ができるのか、情報を整理していくお手伝いをさせていただけないでしょうか。まずはお気持ちをお聞かせください。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789794983", "jst_text": "9月19日（土）14時16分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20715"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 6, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20715", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"result": false, "selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "7", "need_basis": "要介護認定を受けていない母親のワンオペ介護を行っており、夜間対応による睡眠不足や手が出そうになるほどの限界を抱えながらも、ケアマネジャーや家族等の相談先・支援者が不在で孤立しているため。", "contact_safety_risk": "2", "crisis_category": "DV・虐待", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "整理"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 7, "phase": "整理", "closing_reason": ""}
IF/ELSE 11（危機の速報判定）
  → {"result": false, "selected_case_id": "false"}
IF/ELSE 19（採点やり直しの関門）
  → {"result": false, "selected_case_id": "false"}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"result": false, "selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
IF/ELSE 4（有人対応同意判定）
  → {"result": false, "selected_case_id": "false"}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-19v
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

## J1t7 通目

- 送った文: `はい、お願いします。どこに相談すればいいのか知りたいです。`
- Dify側の時刻(JST): 2026-09-19 14:17:28
- 所要: 18.1秒 ／ 返事 321字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
承知いたしました。どこに相談すればいいのか、一緒に考えていきましょう。

その前に、まずこれまでお話しいただいた内容を、一度こちらで整理させてください。

お母様の介護を、ご兄弟やケアマネジャーさんのような頼れる方がいないなか、おひとりで担っていらっしゃる。お母様は要介護認定を受けておらず、夜も何度も起こされるなど、心身ともに休まらない状況が続いている。その中で、お母様に強く当たってしまい、「手が出そうになる」ほどご自身が追い詰められていることに恐怖を感じていらっしゃる。そして、これまで「どこに言えばいいのかも分からなくて」、誰にも相談できずにこられた。

このように受け取りましたが、ずれているところや、付け足したいことはありますか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789795048", "jst_text": "9月19日（土）14時17分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20715"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "整理", "session_turns": 7, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20715", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"result": false, "selected_case_id": "false"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 7, "phase": "提案", "closing_reason": ""}
IF/ELSE 11（危機の速報判定）
  → {"result": false, "selected_case_id": "false"}
IF/ELSE 19（採点やり直しの関門）
  → {"result": false, "selected_case_id": "false"}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"result": false, "selected_case_id": "false"}
IF/ELSE 4（有人対応同意判定）
  → {"result": false, "selected_case_id": "false"}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-19v
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

## J1t8 通目

- 送った文: `ずれていません。そのとおりです。`
- Dify側の時刻(JST): 2026-09-19 14:18:04
- 所要: 15.1秒 ／ 返事 168字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
ありがとうございます。ずれていないとのこと、安心しました。

お話を伺っていて、私が最も重いと感じたのは、お母様に「手が出そうになる」ほど追い詰められているのに、誰にも頼れず、どこに助けを求めたらいいのかも分からない、その孤独感と恐怖ではないかということです。

この受け止め方は、近い感じがしますか。それとも、そこではないでしょうか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789795085", "jst_text": "9月19日（土）14時18分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20715"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "提案", "session_turns": 8, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20715", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"result": false, "selected_case_id": "false"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 7, "phase": "提案", "closing_reason": ""}
IF/ELSE 11（危機の速報判定）
  → {"result": false, "selected_case_id": "false"}
IF/ELSE 19（採点やり直しの関門）
  → {"result": false, "selected_case_id": "false"}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"result": false, "selected_case_id": "false"}
IF/ELSE 4（有人対応同意判定）
  → {"result": false, "selected_case_id": "false"}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-19v
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
