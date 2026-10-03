# 台本D 生出力（第34版）

- 利用者ID: `t-34-D`
- 会話ID: `a98572d6-6085-46a6-b06d-8b7bb95e46b4`
- 版の目印: `定数生成（true文字列）／版 2026-09-19z3`

本文は一字も直していません。

---

## 1通目

- 送った文: `夫からひどいことを言われます。怖いです。`
- Dify側の時刻(JST): 2026-09-20 05:09:40
- 所要: 19.3秒 ／ 返事 151字 ／ ノード 32個

**返ってきた本文（そのまま）**

```
ご連絡ありがとうございます。
夫からひどいことを言われるとのこと、それはとても怖くて、つらい思いをされていますね。

「ひどいこと」を言われ、恐怖を感じていらっしゃるのですね。
もしお話しできるようならで構いませんので、どのような状況で、どんな言葉をかけられるのか、少し教えていただくことはできますか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789848584", "jst_text": "9月20日（日）5時09分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "受付", "session_turns": 1, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "5", "need_basis": "夫からの暴言などにより恐怖を感じており、家庭内での人間関係・精神的な安全の危機に瀕しているが、現時点で暴力や監視などの詳細な状況や他の相談先の有無が未確認のため、支援がないと好転しない状態として判定しました。", "contact_safety_risk": "3", "crisis_category": "DV・虐待", "support_type": "こころ", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 3, "max_support_need": 5, "phase": "傾聴", "closing_reason": ""}
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

- 送った文: `携帯も時々見られています。`
- Dify側の時刻(JST): 2026-09-20 05:10:00
- 所要: 18.0秒 ／ 返事 209字 ／ ノード 31個

**返ってきた本文（そのまま）**

```
携帯電話まで見られているのですね。自分の知らないところで中を見られているかもしれないと思うと、とても不安で、気が休まらないですよね。

「ひどいことを言われる」恐怖に加えて、「携帯も時々見られている」とのこと。常に誰かに見張られているような感覚で、安心して過ごすことが難しい状況なのだとお察しします。

携帯を見られているかもしれないと感じることで、何か生活の中で困っていることや、しづらくなっていることはありますか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789848600", "jst_text": "9月20日（日）5時10分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 2, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "8", "need_basis": "夫からの言動に恐怖を感じており、携帯電話をチェックされているなど行動や連絡の監視が疑われる状況であり、逃げ場や安全が脅かされる恐れがあるため。", "contact_safety_risk": "4", "crisis_category": "DV・虐待", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 4, "max_support_need": 8, "phase": "傾聴", "closing_reason": ""}
IF/ELSE 11（危機の速報判定）
  → {"selected_case_id": "true"}
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
- HTTP リクエスト（危機速報Slack通知）
- 変数代入（危機速報済み）
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

- 送った文: `お金も自由に使わせてもらえません。`
- Dify側の時刻(JST): 2026-09-20 05:10:20
- 所要: 15.0秒 ／ 返事 215字 ／ ノード 29個

**返ってきた本文（そのまま）**

```
お金のこともご自身で自由にできないのですね。それは、まるで自分の行動をすべて縛られているようで、とても息苦しい思いをされていることと思います。

夫からひどいことを言われる恐怖に加えて、携帯を見られたり、「お金も自由に使わせてもらえ」なかったりする状況なのですね。安心して生活することが、とても難しい状況なのだと感じました。

お金が自由に使えないことで、毎日の食事や日用品の買い物など、生活の中で何か困っていることはありますか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789848620", "jst_text": "9月20日（日）5時10分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 3, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "8", "need_basis": "夫から言動による恐怖を与えられているだけでなく、携帯電話の監視やお金の不自由を強いられるなど、配偶者による過度な支配・経済的DVの状況下に置かれており、安全な生活基盤および助けを得られる環境が損なわれているため。", "contact_safety_risk": "4", "crisis_category": "DV・虐待", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 4, "max_support_need": 8, "phase": "傾聴", "closing_reason": ""}
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

- 送った文: `実家には頼れません。友だちにも言えていません。`
- Dify側の時刻(JST): 2026-09-20 05:10:37
- 所要: 21.1秒 ／ 返事 179字 ／ ノード 29個

**返ってきた本文（そのまま）**

```
ご実家にも、お友だちにも言えないのですね。一番つらいときに頼れる人がいないと感じるのは、本当に孤独で、息が詰まるような思いですよね。

夫からのひどい言葉や行動に耐えながら、「実家には頼れ」ず、親しいご友人にも打ち明けられない。そんな状況で、これまでおひとりで抱えてこられたのですね。

誰にも話せずにいることで、今、一番つらいと感じるのはどんなことですか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789848637", "jst_text": "9月20日（日）5時10分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 4, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "8", "need_basis": "夫から暴言や携帯の監視、経済的制限を受けているDV・モラハラ状況にあり、さらに実家や友人など周囲に頼れる人がおらず孤立しているため。", "contact_safety_risk": "4", "crisis_category": "DV・虐待", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 4, "max_support_need": 8, "phase": "傾聴", "closing_reason": ""}
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

## 5通目

- 送った文: `夫は夜の8時ごろに帰ってきます。`
- Dify側の時刻(JST): 2026-09-20 05:11:00
- 所要: 8.3秒 ／ 返事 173字 ／ ノード 29個

**返ってきた本文（そのまま）**

```
申し訳ありません、ただいま混み合っております。 少し時間をおいて、もう一度お話しかけていただけますか。  お急ぎの場合は、こちらもご利用いただけます。 ・いのちSOS：0120-061-338（24時間365日） ・よりそいホットライン：0120-279-338（24時間対応）  命に関わる危険がある場合は110（警察）・119（消防救急）へ。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789848661", "jst_text": "9月20日（日）5時11分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 5, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "8", "need_basis": "夫から暴言や携帯の監視、経済的支配を受けており、実家や友人に頼れず周囲から孤立している状況であるため。", "contact_safety_risk": "4", "crisis_category": "DV・虐待", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 4, "max_support_need": 8, "phase": "傾聴", "closing_reason": ""}
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

- 送った文: `夫は夜の8時ごろに帰ってきます。`
- Dify側の時刻(JST): 2026-09-20 05:13:01
- 所要: 17.9秒 ／ 返事 227字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
先ほどは定型文の返信となり、大変失礼いたしました。改めてお話をうかがいますね。

「夫は夜の8時ごろに帰ってきます」とのこと、その時間が近づくにつれて、どんどん緊張が高まり、怖い気持ちになっていらっしゃるのではないでしょうか。

誰にも頼れない状況のなかで、ひどい言葉を言われる相手がもうすぐ帰ってくるというのは、本当に心休まらない時間だと思います。

差し支えなければ教えてください。今夜、ご自身が安全に過ごせるかどうか、不安に感じることはありますか？
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789848781", "jst_text": "9月20日（日）5時13分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 6, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "8", "need_basis": "夫からの言葉の暴力に加え、携帯の監視や経済的支配を受けており、実家や友人に相談できず孤立している。今夜も8時に夫が帰宅するため、危害や抑圧に晒される状況が迫っている。", "contact_safety_risk": "4", "crisis_category": "DV・虐待", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 4, "max_support_need": 8, "phase": "傾聴", "closing_reason": ""}
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

- 送った文: `今夜も怒鳴られるかもしれないと思うと怖いです。`
- Dify側の時刻(JST): 2026-09-20 05:13:46
- 所要: 20.1秒 ／ 返事 485字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
「今夜も怒鳴られるかもしれない」と思うと、本当に怖いですよね。その時間が近づいてくると思うだけで、心臓が締め付けられるような、息が詰まるような思いだと思います。

誰にも頼れない中で、これからまた「怒鳴られるかもしれない」という恐怖に一人で耐えなければいけない。それは、あまりにもつらすぎる状況です。

あなたの安全が、何よりも大切です。もしものときのために、今夜のことだけでもすぐに相談できる場所があることをお伝えさせてください。

*   **DV相談＋（プラス）**
    電話：0120-279-889（24時間対応）
    メールやチャットでの相談もできます。

*   **DV相談ナビ**
    電話：#8008（はれれば）
    最寄りの相談窓口に自動でつながります。

これらの窓口では、専門の相談員が今夜どうすれば安全に過ごせるか、一緒に考えてくれます。必要であれば、一時的に避難できる安全な場所（シェルター）の情報も持っています。

今、お電話をかけることが難しい状況かもしれませんが、このような場所があることを知っておいていただけますか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789848826", "jst_text": "9月20日（日）5時13分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 7, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "8", "need_basis": "夫からのモラハラ（酷い暴言）、携帯監視、経済的支配があり、頼れる実家や友人もなく孤立している。加害可能性のある同居夫が夜8時に帰宅するため、今夜の安全確保や暴力等への恐怖があり、自力で対処できない状況である。", "contact_safety_risk": "4", "crisis_category": "DV・虐待", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 4, "max_support_need": 8, "phase": "傾聴", "closing_reason": ""}
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

- 送った文: `はい、覚えておきます。でも電話はかけづらいです。`
- Dify側の時刻(JST): 2026-09-20 05:14:21
- 所要: 18.1秒 ／ 返事 345字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
お電話をかけるのは、とても勇気がいることですよね。誰かに聞かれるかもしれない不安もありますし、何から話せばいいか分からなくなってしまうこともあります。そう感じられるのは、とても自然なことだと思います。

夫が帰ってくる恐怖を感じながらも、「電話はかけづらい」と感じていらっしゃるのですね。

もし文字でのやりとりであれば少し話しやすい、ということであれば、先ほどお伝えした「DV相談＋」は、24時間対応のチャット相談も行っています。専門の相談員が、今どうしたらいいか、文字のやりとりで一緒に考えてくれます。

もちろん、今すぐどこかに相談するのが難しいと感じるようでしたら、もう少しここで私にお話をお聞かせいただくこともできます。今、あなたにとって、どちらが少しでも安心できそうでしょうか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789848862", "jst_text": "9月20日（日）5時14分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 8, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "8", "need_basis": "夫から罵倒され、携帯チェックや金銭的支配を受けており、今夜も怒鳴られる恐怖がある一方で、実家や友人に頼れず社会的に孤立している。今夜の安全確保や避難の必要性があるにもかかわらず他者との直接連絡に躊躇している状況である。", "contact_safety_risk": "4", "crisis_category": "DV・虐待", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 4, "max_support_need": 8, "phase": "傾聴", "closing_reason": ""}
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

- 送った文: `もう少しここで話を聞いてほしいです。`
- Dify側の時刻(JST): 2026-09-20 05:14:58
- 所要: 18.0秒 ／ 返事 217字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
もちろんです。ここで引き続きお話をうかがいますね。話したいと思ってくださって、ありがとうございます。

夫からのひどい言葉や行動にひとりで耐え、今夜も「怒鳴られるかもしれない」という恐怖の中にいらっしゃるのですね。誰にも言えず、本当に心細いですよね。

差し支えなければ、もう少し教えていただけますか。夫が帰ってきてから、特に「怖い」と感じるのは、どのようなときでしょうか。もし話すのがつらければ、無理に答えなくても大丈夫ですからね。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789848898", "jst_text": "9月20日（日）5時14分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 9, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "8", "need_basis": "夫から暴言や怒鳴りを受け、携帯の監視や経済的支配（お金を使わせてもらえない）を受けており、今夜も怒鳴られる恐怖がある。頼れる実家や友人もおらず、暴力や支配のある家に帰らざるを得ない危険な状況である。", "contact_safety_risk": "4", "crisis_category": "DV・虐待", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 4, "max_support_need": 8, "phase": "傾聴", "closing_reason": ""}
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

- 送った文: `機嫌が悪いときに、物に当たられるときです。`
- Dify側の時刻(JST): 2026-09-20 05:16:02
- 所要: 19.5秒 ／ 返事 299字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
物に当たられるのですね。大きな音を立てたり、物が壊れたりするのを目の当たりにするのは、本当に恐ろしいことだと思います。いつか自分にその矛先が向くのではないかと、生きた心地がしないですよね。

夫の「機嫌が悪いときに、物に当たられる」こと、それがあなたにとって、怒鳴られること以上の恐怖になっているのですね。それは、あなたの心を深く傷つけ、身の危険を感じさせる、決して許されない行為です。

もしお話しするのがつらかったら、無理に答えなくても大丈夫です。差し支えなければ教えていただきたいのですが、これまで、物に当たるだけでなく、直接あなたに手をあげられたり、体を強く押されたりしたことはありますか？
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789848962", "jst_text": "9月20日（日）5時16分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 10, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "8", "need_basis": "夫から怒鳴られ暴力を振るわれる恐れがあり、携帯の監視や経済的支配を受けており、実家や友人など頼れる先が身近に存在せず今夜の安全確保が困難なため。", "contact_safety_risk": "4", "crisis_category": "DV・虐待", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 4, "max_support_need": 8, "phase": "傾聴", "closing_reason": ""}
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

- 送った文: `一度だけ、腕を強くつかまれたことがあります。`
- Dify側の時刻(JST): 2026-09-20 05:16:33
- 所要: 18.0秒 ／ 返事 330字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
そうだったのですね。お話しいただき、ありがとうございます。
「一度だけ」であっても、腕を強くつかまれたことは、とても痛くて、本当に怖かったことと思います。それは決して許されることではない、心と体への暴力です。あなたが我慢しなければならないことでは、決してありません。

これまでのひどい言葉や物に当たる行為に加えて、実際に体に危害を加えられた経験があるのですね。そうなると、「今夜もまた何かあるかもしれない」という恐怖は、計り知れないものだと思います。

あなたの安全が何よりも心配です。差し支えなければ、一つだけ教えてください。もし今夜、夫が物に当たり始めたり、身の危険を感じたりしたときに、すぐに逃げ込めるような別の部屋や、家の外の安全な場所はありますか？
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789848994", "jst_text": "9月20日（日）5時16分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 11, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "8", "need_basis": "夫から怒鳴られ暴言を吐かれるほか、携帯チェックや経済的制限を受けており、今夜も機嫌が悪くなると物に当たられる恐怖に晒されている。実家や友人に頼れず独立した相談先もないため絶体絶命の孤立状態にあり、過去には腕を強く掴まれる等の暴力を受けているため今夜の身の危険が高い。", "contact_safety_risk": "4", "crisis_category": "DV・虐待", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 4, "max_support_need": 8, "phase": "傾聴", "closing_reason": ""}
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

- 送った文: `隣の部屋には行けますが、鍵はかかりません。`
- Dify側の時刻(JST): 2026-09-20 05:17:09
- 所要: 22.4秒 ／ 返事 612字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
「隣の部屋には行けますが、鍵はかかりません」とのこと、教えてくださってありがとうございます。
いざという時に逃げ込める場所があっても、鍵がかからないのでは完全に安心することはできず、本当に心細いですよね。

ここまでお話をうかがって、あなたの置かれている状況が、心身ともに非常に危険な状態にあると感じています。少し長くなりますが、一度お気持ちを整理させてください。

夫からひどい言葉を言われ、携帯を監視され、お金も自由にできず、機嫌が悪いときには「物に当たられる」という恐怖があり、過去には「腕を強くつかまれた」という直接的な暴力も受けている。誰にも頼れない中で、今夜もまたそれが繰り返されるかもしれないという恐怖に、たった一人で耐えていらっしゃるのですね。

何よりもおつらいのは、いつまた暴力が始まるかわからない恐怖の中で、完全に安全とは言えない場所に、たった一人でいなければならないという、逃げ場のない状況そのものではないでしょうか。

これは私の推測ですが、今起きていることは、決してあなたが悪いからではなく、心と体を支配するための暴力（DV）です。このまま一人で耐え続けるのは、あまりにも危険です。

このとても危険な状況から抜け出し、あなたが安心して過ごせる方法を一緒に見つけるために、このお話を当法人の相談員（人）に直接お伝えして、今後の具体的なサポートを一緒に考えていきたいと思いますが、いかがでしょうか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789849029", "jst_text": "9月20日（日）5時17分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 12, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "8", "need_basis": "夫からのモラハラ・暴言に加えて、携帯の監視、経済的支配、物への損壊行為、および身体的暴力（腕を強く掴まれる）があり、今夜も暴力を振るわれる恐怖の中にあって、頼れる身内や友人もおらず他機関にもつながっていないため。", "contact_safety_risk": "4", "crisis_category": "DV・虐待", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 4, "max_support_need": 8, "phase": "傾聴", "closing_reason": ""}
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
- Dify側の時刻(JST): 2026-09-20 05:17:45
- 所要: 19.8秒 ／ 返事 438字 ／ ノード 33個

**返ってきた本文（そのまま）**

```
おつらい状況の中、お話しいただき本当にありがとうございます。そして、私たちを頼ってくださって、ありがとうございます。相談員に引き継ぐというご決断、とても勇気がいることだったと思います。

今後のご相談について、いくつかご案内させてください。

まず、相談員と直接お話しするために、お住まいの市区町村やご希望の日時などをうかがうための、専用の入力フォームをご用意しています。3分ほどで終わる簡単なものですので、ご自身のタイミングでご入力ください。

↓こちらのリンクからご入力いただけます。
https://liff.line.me/2010836980-ms5nFPQE?mode=call

大切なことなのでお伝えしますが、**フォームにご入力いただいた内容は、このトーク画面には表示されず、担当の相談員にだけ届きます**ので、どうぞご安心ください。

また、相談員からご連絡する際、どのようにお呼びするのがよろしいでしょうか。もしよろしければ、お呼び名をお聞かせください。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789849066", "jst_text": "9月20日（日）5時17分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 13, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "8", "need_basis": "夫から暴言、スマホ監視、経済的制限、物に当たる行為を受け、過去に身体的暴力（腕を掴まれる）の経験もある。今夜も暴力を振るわれる恐怖があるが頼れる先がなく、自宅内に鍵のかかる避難部屋もないため安全が確保できない状況である。", "contact_safety_risk": "4", "crisis_category": "DV・虐待", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "提案"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 4, "max_support_need": 8, "phase": "提案", "closing_reason": ""}
IF/ELSE 11（危機の速報判定）
  → {"selected_case_id": "false"}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
IF/ELSE 19（採点やり直しの関門）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "DV・暴力", "next_action": "最優先で相談員が連絡を取り、安全確保を行う。本人の意向を確認しつつ、一時保護シェルターの利用や、配偶者暴力相談支援センターへの同行支援を検討する。身の危険が差し迫っているため、警察への相談も選択肢として提示し、必要に応じて付き添う。中長期的には、接近禁止命令などの法的支援、生活再建のための公的制度の利用、心理的ケアへとつなげていく。", "related_issue": "経済的DV、精神的DV、身体的暴力、社会的孤立、監視・束縛", "summary": "夫から日常的に暴言を受け、スマートフォンの監視、経済的制限、物に当たる行為に恐怖を感じている。過去には腕を強く掴まれる身体的暴力も経験。実家や友人には頼れず孤立状態にある。今夜も夫の帰宅後に暴力を振るわれる恐怖があるが、自宅内に鍵のかかる安全な避難場所がない。心身の安全が脅かされている緊急性の高い状況。", "urgency": "8", "consent": "はい", "phone_removed": ""}
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
- パラメータ抽出3（有人対応同意）
- IF/ELSE 4（有人対応同意判定）
- HTTP リクエスト（相談記録登録：引き継ぎサマリー）
- 変数代入
- コード（サマリー保存の結果判定）
- IF/ELSE 12（サマリー保存の失敗チェック）
- HTTP リクエスト（引き継ぎサマリーSlack通知）
- 変数代入（要約通知済みフラグ）
- 変数代入（要約通知タイムスタンプ）

</details>

---

## 14通目

- 送った文: `みどり、とお呼びください。ただ、電話は夫に見られるかもしれません。`
- Dify側の時刻(JST): 2026-09-20 05:18:32
- 所要: 18.2秒 ／ 返事 502字 ／ ノード 34個

**返ってきた本文（そのまま）**

```
みどりさん、とお呼びしますね。教えてくださってありがとうございます。
そして、「電話は夫に見られるかもしれません」という大切なことを伝えてくださって、本当にありがとうございます。見つかってしまうかもしれないと思うと、相談すること自体が怖くなりますよね。

どうぞ、ご安心ください。私たちからみどりさんにご連絡する際は、**お電話をかけることはありません。**LINEの無料通話を使いますので、電話番号をお聞きすることもありませんし、着信が鳴ったり、履歴が残ったりする心配もありません。

ご予約いただいたお時間になりましたら、このトーク画面に、こちらから通話ができるボタン付きのメッセージをお送りします。みどりさんのご都合のよいタイミングでそのボタンを押していただく形なので、もし夫が近くにいるなど、都合が悪ければ押さなければ大丈夫です。

これは、みどりさんのように、ご連絡することでかえって危険が及ぶ可能性のある方を守るための仕組みです。

先ほどお送りしたフォームに、この方法でお話しできるご都合のよい日時をご入力いただければと思います。入力された内容は担当者にだけ届きますので、ご安心くださいね。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789849113", "jst_text": "9月20日（日）5時18分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "提案", "session_turns": 14, "summary_notified": "true", "turn_base": 0, "post_landing_note": "true", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "true", "urgent_used": "true", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "post-landing-note"}
コード（着地後書き込みの速報判定と本文）
  → {"should_alert": "true", "payload": "{\"text\": \"🔔 引き継ぎ後に、相談者ご本人から書き込みがありました\\n支援必要度（最高）：8／10　二次被害リスク：4／4\\n――――― 書かれた内容 ―――――\\nみどり、とお呼びください。ただ、電話は夫に見られるかもしれません。\\n―――――――――――――――\\n会話ID：a98572d6-6085-46a6-b06d-8b7bb95e46b4\\n支援経過シートにも記録されています。\\n※この会話で今日これ以降の書き込みは、危機の言葉があるときだけお知らせします。ほかは支援経過シートをご確認ください。\"}", "day": "20716"}
IF/ELSE 15（着地後書き込みの速報判定）
  → {"selected_case_id": "true"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "8", "need_basis": "夫から怒鳴られ、携帯や金銭の管理・監視を受け、過去に身体的暴力を受けている。身の危険を感じるも逃げ込める鍵付きの部屋がなく、実家や友人等にも頼れない状況で今夜を過ごす必要があるため。", "contact_safety_risk": "4", "crisis_category": "DV・虐待", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "みどり", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "提案"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 4, "max_support_need": 8, "phase": "提案", "closing_reason": ""}
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
