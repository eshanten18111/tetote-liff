# 台本L 生出力（第34版）

- 利用者ID: `t-35-L`
- 会話ID: `9c66aafd-89ab-49ac-9cbe-9d4b2701dc70`
- 版の目印: `定数生成（true文字列）／版 2026-09-20a`

本文は一字も直していません。

---

## 1通目

- 送った文: `仕事を辞めてから、これからのことが不安です。`
- Dify側の時刻(JST): 2026-09-20 06:07:02
- 所要: 22.4秒 ／ 返事 131字 ／ ノード 32個

**返ってきた本文（そのまま）**

```
ご連絡ありがとうございます。
お仕事を辞められて、これからのことを考えると、とても不安な気持ちになりますよね。

その「これからのことが不安」というお気持ちについて、もし差し支えなければ、もう少しお聞かせいただけますか。特にどのようなことが気にかかっていますか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789852030", "jst_text": "9月20日（日）6時07分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "受付", "session_turns": 1, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "5", "need_basis": "仕事を退職し、今後の生活の見通しが立たなくなっており、周囲に相談できるつながりがない状況であるため。", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 5, "phase": "傾聴", "closing_reason": ""}
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
- 定数生成（true文字列）／版 2026-09-20a
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

- 送った文: `辞めたのは先月で、上司との折り合いが悪かったからです。`
- Dify側の時刻(JST): 2026-09-20 06:07:24
- 所要: 12.2秒 ／ 返事 183字 ／ ノード 32個

**返ってきた本文（そのまま）**

```
そうだったのですね。上司の方とのことで、おつらい思いをされたのですね。先月まで、大変な中でよく頑張ってこられたと思います。

お仕事を辞めて1ヶ月ほど経つ中で、これから先のことを考えると不安が募ってしまう状況なのですね。

その不安な気持ちは、例えば、次のお仕事のことでしょうか。それとも、日々の生活のことでしょうか。差し支えなければ、もう少し教えていただけますか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789852047", "jst_text": "9月20日（日）6時07分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 2, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "5", "need_basis": "先月離職しており、今後の見通しが立っておらず生活基盤や今後の就労に関する支援が必要な状態にあるため。", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 5, "phase": "傾聴", "closing_reason": ""}
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
- 定数生成（true文字列）／版 2026-09-20a
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

- 送った文: `同じ業界で探していますが、求人が少ないです。`
- Dify側の時刻(JST): 2026-09-20 06:07:37
- 所要: 16.4秒 ／ 返事 230字 ／ ノード 29個

**返ってきた本文（そのまま）**

```
そうだったのですね。ご自身の経験を活かせる同じ業界で探していても、「求人が少ない」状況だと、これからどうしたらいいのかと、さらに不安が大きくなりますよね。

上司の方とのことがあって先月お仕事を辞められ、次へ向けて動こうとされている中で、なかなか先が見通せないことにお気持ちが落ち着かない状況なのですね。

求人が少ない状況が続くと、どのようなことが一番の心配事になってきますか。たとえば、日々の生活費のことでしょうか、それとも今後のキャリアのことでしょうか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789852058", "jst_text": "9月20日（日）6時07分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 3, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "5", "need_basis": "先月離職し失業中であり、同業界での求人が少なく再就職・生活の見通しが立っていない状況であるため。", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 5, "phase": "傾聴", "closing_reason": ""}
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
- 定数生成（true文字列）／版 2026-09-20a
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

## 4通目

- 送った文: `貯金は3か月分くらいしかありません。`
- Dify側の時刻(JST): 2026-09-20 06:07:55
- 所要: 15.4秒 ／ 返事 226字 ／ ノード 29個

**返ってきた本文（そのまま）**

```
お話いただきありがとうございます。
「貯金は3か月分くらい」しかない状況で、求人が少ないとなると、これからどうなってしまうのだろうと、本当に不安になりますよね。時間が経つほどに、焦るお気持ちも強くなると思います。

上司の方とのことでお仕事を辞めざるを得なかった中で、次の仕事を探していてもなかなか見通しが立たず、生活費の心配が日に日に大きくなっているのですね。

その「3か月」という期間を考えると、どのようなことが一番の焦りにつながると感じますか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789852075", "jst_text": "9月20日（日）6時07分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 4, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "5", "need_basis": "先月離職して現在は求人が少ない状況にあり、貯金も残り3か月分ほどで今後の生活の見通しが立っていないため。", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 5, "phase": "傾聴", "closing_reason": ""}
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
- 定数生成（true文字列）／版 2026-09-20a
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

- 送った文: `家賃は月に5万5千円です。`
- Dify側の時刻(JST): 2026-09-20 06:08:11
- 所要: 17.1秒 ／ 返事 246字 ／ ノード 29個

**返ってきた本文（そのまま）**

```
お話しいただきありがとうございます。
毎月5万5千円の家賃は、お仕事が決まっていない状況では本当に大きな負担ですよね。貯金が減っていく中で、この支払いが続くことを考えると、気持ちが焦ってしまうお気持ち、とてもよく分かります。

次のお仕事が見つからない中で、「家賃は月に5万5千円です」という決まった出費があることが、貯金が減っていく不安を一層大きくさせているのですね。

このような状況について、これまでにご家族やご友人、あるいはハローワークなどの公的な窓口で相談されたことはありましたか？
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789852091", "jst_text": "9月20日（日）6時08分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 5, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "need_basis": "退職後に同業界での求人が乏しく再就職の見通しが立たない中、貯金が3ヶ月分程度しかなく毎月5万5千円の家賃負担があり、生活基盤の維持が困窮するおそれがあるため。", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
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
- 定数生成（true文字列）／版 2026-09-20a
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

- 送った文: `履歴書を10社くらい出しましたが、面接まで進んだのは1社だけです。`
- Dify側の時刻(JST): 2026-09-20 06:08:29
- 所要: 19.0秒 ／ 返事 278字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
10社も履歴書を送られたのですね。ご自身で一生懸命に行動されている中で、面接まで進めたのが1社だけというのは、本当に気持ちが折れそうになりますよね。先が見えない不安が、さらに強くなってしまったのではないでしょうか。

貯金が減っていく中で家賃の支払いが迫るという焦りを感じながら、なんとかしようと行動しているのに、なかなか結果に繋がらない。その状況は、本当におつらいと思います。

これだけ頑張ってもうまくいかないと、一人で抱え続けるのはとてもしんどいことだと思います。このような今の状況や不安な気持ちを、誰かにお話しできる相手は周りにいらっしゃいますか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789852110", "jst_text": "9月20日（日）6時08分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 6, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "need_basis": "先月失職し、貯金が約3ヶ月分しかなく家賃支払い（月5万5千円）の継続に強い不安がある中で、10社応募して面接1社と再就職の難航が続いており、生活基盤の維持が見通せない状態であるため。", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
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
- 定数生成（true文字列）／版 2026-09-20a
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

- 送った文: `その1社も、年齢のことを言われて断られました。`
- Dify側の時刻(JST): 2026-09-20 06:08:49
- 所要: 19.7秒 ／ 返事 298字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
面接まで進めたのに、ご自身の努力とは関係のない「年齢のことを言われて断られた」とのこと、それは本当に悔しくて、やりきれない気持ちになりますよね。頑張ってきたことまで否定されたように感じて、心が折れてしまいそうになるお気持ち、お察しします。

貯金が減っていく焦りの中で、10社も応募してやっとたどり着いた面接でそのような対応をされるのは、本当におつらいことだと思います。

一人でこの状況を乗り越えようと必死に頑張っておられるのですね。こうした経済的に苦しいときに、家賃の負担を一時的に軽くしてくれる公的な制度などもあります。これまで、そういった支援についてどこかへ相談されたことはありましたか？
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789852130", "jst_text": "9月20日（日）6時08分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 7, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "need_basis": "失業中で貯金が残り約3か月分しかなく、月5万5千円の家賃負担がある中で、再就職に向けた応募も難航しており生活基盤が崩れ始めているため。", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
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
- 定数生成（true文字列）／版 2026-09-20a
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

- 送った文: `私はいま42歳です。`
- Dify側の時刻(JST): 2026-09-20 06:09:10
- 所要: 21.3秒 ／ 返事 326字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
42歳でいらっしゃるのですね。教えてくださってありがとうございます。
ご自身の力ではどうにもならない年齢のことを理由に不採用となってしまうと、これまでの努力や経験まで否定されたように感じて、本当に悔しく、やりきれないお気持ちだったと思います。

ここまでお話しいただいたことを、一度整理させてください。
1ヶ月前に上司とのことでお仕事を辞め、約3ヶ月分の貯金で月5万5千円の家賃を支払わなければならない不安のなか、必死で10社も応募された。それなのに、やっと進んだ面接で「年齢のことを言われて断られました」。こうした状況が重なって、今はどうしていいか分からなくなっている、というふうに受け取りました。

この受け止め方で、ずれているところはありますか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789852150", "jst_text": "9月20日（日）6時09分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 8, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "need_basis": "前職を離職し失業中で、貯金が約3か月分（家賃5.5万円）しかなく生活基盤が崩れ始めている。再就職活動を行うも不採用が続き、相談できる相手や支援先にもつながっていない状況であるため。", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
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
- 定数生成（true文字列）／版 2026-09-20a
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

- 送った文: `近いです。`
- Dify側の時刻(JST): 2026-09-20 06:09:32
- 所要: 14.1秒 ／ 返事 250字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
教えてくださって、ありがとうございます。お気持ちを共有させていただけて、少しでもお力になれたらと思っています。

お話を伺っていて、経済的な不安ももちろん大きいと思いますが、それ以上に、ご自身の努力ではどうにもならない「年齢のことを言われて断られました」という経験が、心を一番重くさせているのではないかと感じました。

頑張っても報われないという無力感や、社会から必要とされていないような孤独感が、今の不安を一番大きくしているのではないでしょうか。この点について、ご自身ではどのように感じられますか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789852173", "jst_text": "9月20日（日）6時09分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 9, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "need_basis": "失職中で貯金が約3ヶ月分しかなく、月5万5千円の家賃負担がある中で再就職先が決まらず、相談できる相手や支援機関につながっていないため。", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "提案"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 6, "phase": "提案", "closing_reason": ""}
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
- 定数生成（true文字列）／版 2026-09-20a
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

- 送った文: `履歴書の書き方が合っているのか分かりません。`
- Dify側の時刻(JST): 2026-09-20 06:09:47
- 所要: 17.8秒 ／ 返事 301字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
そうですよね。10社も応募してうまくいかないと、「履歴書の書き方が合っているのか分からない」と、ご自身のやり方に自信が持てなくなってしまいますよね。誰にも相談できない中では、本当に不安だと思います。

ここまでお話を伺って、これは私の推測なので、もし違っていたら教えてほしいのですが、不採用が続いたことで、ご自身のやり方が正しいのか分からなくなり、「誰かに客観的なアドバイスをもらって、これで大丈夫だという確信を持って進みたい」というお気持ちがあるのではないでしょうか。

一人で暗中模索で進めるのではなく、専門的な視点から「これで合っている」と背中を押してもらいたい、というお気持ちに近いでしょうか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789852188", "jst_text": "9月20日（日）6時09分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "提案", "session_turns": 10, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "need_basis": "失業中で貯金が約3ヶ月分しかなく家賃負担も大きい中、10社応募して採用に至らず、周囲に相談できる相手もいないため生活基盤の維持が見通せない状態である。", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 6, "phase": "整理", "closing_reason": ""}
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
- 定数生成（true文字列）／版 2026-09-20a
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

- 送った文: `ハローワークには一度だけ行きました。`
- Dify側の時刻(JST): 2026-09-20 06:10:06
- 所要: 18.1秒 ／ 返事 121字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
ハローワークにも足を運ばれたのですね。ご自身でなんとかしようと、色々と行動されてきたのですね。

「ハローワークには一度だけ行きました」とのことですが、もし差し支えなければ、その時のことを少し教えていただけますか。行ってみて、いかがでしたか？
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789852206", "jst_text": "9月20日（日）6時10分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "整理", "session_turns": 11, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "need_basis": "失業中で残りの貯金が約3ヶ月分しかなく、求人が少ないうえに応募が難航しており、生活基盤の維持が危ぶまれる中で頼れる相談相手がいないため。", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
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
- 定数生成（true文字列）／版 2026-09-20a
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

- 送った文: `担当の方は親切でしたが、また行くのが気まずいです。`
- Dify側の時刻(JST): 2026-09-20 06:10:25
- 所要: 17.0秒 ／ 返事 204字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
ハローワークに足を運ばれたのですね。ご自身でなんとかしようと行動されていて、本当にすごいです。

それなのに、「また行くのが気まずい」と感じていらっしゃるのですね。担当の方が親切だったからこそ、かえって行きづらくなってしまうお気持ち、とてもよく分かります。

その「気まずい」というお気持ちは、例えば、一度相談したのに特に進展がないまま、また顔を合わせるのが申し訳ない、というようなお気持ちに近いでしょうか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789852226", "jst_text": "9月20日（日）6時10分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 12, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "need_basis": "前月離職し残貯金約3ヶ月分で家賃5.5万円の支払いがあり、求人が少ない同業界で10社応募するも年齢を理由に不採用が続き、ハローワークへの再訪にも気まずさを感じており生活基盤の維持と支援接続に課題があるため。", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
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
- 定数生成（true文字列）／版 2026-09-20a
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

- 送った文: `親には辞めたことをまだ言えていません。`
- Dify側の時刻(JST): 2026-09-20 06:10:43
- 所要: 16.2秒 ／ 返事 233字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
おつらい状況の中、打ち明けてくださってありがとうございます。
ご両親に「辞めたことをまだ言えていません」とのこと、お一人で抱えられているのですね。心配をかけたくない、がっかりさせたくない、など、様々な思いがあって言い出せない状況なのではないかとお察しします。

ハローワークにも行きづらく、ご家族にも打ち明けられないとなると、本当に一人きりでこの大きな不安と向き合っていらっしゃるのですね。

もし差し支えなければ、ご両親に言えない一番の理由は何だと感じていますか？
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789852244", "jst_text": "9月20日（日）6時10分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 13, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "need_basis": "先月離職し、残りの貯金が約3ヶ月分で毎月5万5千円の家賃負担があり、再就職の難航により生活基盤が揺らぎ始めているが、周りに頼れる人がいない。", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
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
- 定数生成（true文字列）／版 2026-09-20a
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

## 14通目

- 送った文: `実家は県外で、年に一度しか帰っていません。`
- Dify側の時刻(JST): 2026-09-20 06:11:00
- 所要: 20.3秒 ／ 返事 422字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
お話しいただきありがとうございます。
ご実家が県外で、年に一度しか会わないご関係だと、電話などで今のつらい状況を伝えるのは、とても勇気がいることですよね。心配をかけたくないというお気持ちもあって、ますます言い出しにくくなっているのかもしれません。

ここまでお話しいただいたことを、一度整理させてくださいね。
1ヶ月前にお仕事を辞められ、約3ヶ月分の貯金で月5万5千円の家賃を支払わなければならないという大きな不安があること。なんとかしようと10社も応募したけれど、面接に進めたのは1社だけで、そこでも年齢を理由に断られてしまったこと。
その経験から「履歴書の書き方が合っているのか分からない」と自信をなくし、ハローワークにも「気まずい」と感じて再訪できず、ご実家にも「辞めたことをまだ言えていません」。
誰にも頼れないまま、お一人でこの状況を抱えていらっしゃる、というふうに受け取りました。

この受け止め方で、ずれているところはありますか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789852261", "jst_text": "9月20日（日）6時11分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 14, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "need_basis": "失業中で貯金が約3ヶ月分しかなく家賃の負担も重い一方、再就職が難航しており、ハローワークへの再訪や実家への相談もできず孤立しているため。", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
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
- 定数生成（true文字列）／版 2026-09-20a
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

## 15通目

- 送った文: `近いです。`
- Dify側の時刻(JST): 2026-09-20 06:11:22
- 所要: 15.9秒 ／ 返事 216字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
お気持ちを共有させていただき、ありがとうございます。

お話を伺っていて、貯金が減っていく経済的な不安ももちろん大きいと思いますが、それ以上に、頼れるはずのハローワークにも「気まずい」と感じ、ご家族にも「辞めたことをまだ言えていません」という状況で、たった一人でこの八方塞がりのような不安を抱えなければならない。その『孤立感』が、今一番おつらいことなのではないかと感じました。

この点について、ご自身ではどのように感じられますか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789852282", "jst_text": "9月20日（日）6時11分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 15, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "need_basis": "失業中で貯金が約3ヶ月分しかなく家賃負担もある中、ハローワークへの再訪や親への相談ができず孤立しているため。", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "提案"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 6, "phase": "提案", "closing_reason": ""}
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
- 定数生成（true文字列）／版 2026-09-20a
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

## 16通目

- 送った文: `妻には話しましたが、あまり反応がありませんでした。`
- Dify側の時刻(JST): 2026-09-20 06:11:39
- 所要: 20.1秒 ／ 返事 346字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
奥様に勇気を出してお話しされたのですね。それなのに「あまり反応がありませんでした」というのは、本当に寂しく、おつらい気持ちだったと思います。一番分かってほしい相手だからこそ、余計に孤独を感じてしまいますよね。

ハローワークにも行きづらく、ご両親にも言えない。そして、一番身近な奥様に話しても、気持ちを受け止めてもらえなかった。誰にもこの苦しさを分かってもらえないという状況は、本当に息が詰まる思いだと思います。

これは私の推測なので、違っていたら教えてほしいのですが、奥様の反応が薄かったことで、「この苦しみを誰にも理解してもらえない」という絶望感と同時に、「家族を支えなければいけないのに、心配をかけてしまった」というような、ご自身を責める気持ちも生まれてきているのではないでしょうか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789852299", "jst_text": "9月20日（日）6時11分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "提案", "session_turns": 16, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "need_basis": "失職中で貯金も約3ヶ月分しかなく、求人が少ないため生活基盤が崩れ始めている。ハローワークへの再訪や親への相談ができず、妻に話しても反応がないため、外部の適切な支援につながらないまま孤立している状況である。", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "整理"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 6, "phase": "整理", "closing_reason": ""}
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
- 定数生成（true文字列）／版 2026-09-20a
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

## 17通目

- 送った文: `子どもが小学生で、習い事をやめさせようか迷っています。`
- Dify側の時刻(JST): 2026-09-20 06:12:00
- 所要: 22.3秒 ／ 返事 319字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
お子さんのことまで考えなければならない状況、本当に胸が痛みますよね。大切なお子さんの将来を思うと、ご自身の状況がさらに辛く感じられると思います。ご自身のせいだと責めてしまっているのではないでしょうか。

これまでお話しいただいたお悩みは、経済的なことだけでなく、就職活動の進め方、そしてご家族とのことなど、色々なことが複雑に絡み合っているように感じます。そして何より、それを誰にも相談できず、お一人で抱えていらっしゃることが、一番おつらい状況なのだとお察しします。

文字だけだと、伝えきれないこともあると思います。よろしければ一度、当法人の相談員（人）が直接お話を伺い、これからのことを一緒に考えていく、ということはできそうでしょうか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789852320", "jst_text": "9月20日（日）6時12分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "整理", "session_turns": 17, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "3", "need_basis": "", "contact_safety_risk": "1", "crisis_category": "", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
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
- 定数生成（true文字列）／版 2026-09-20a
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

## 18通目

- 送った文: `朝起きるのがだんだんつらくなってきました。`
- Dify側の時刻(JST): 2026-09-20 06:12:23
- 所要: 18.6秒 ／ 返事 333字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
そうだったのですね。「朝起きるのがだんだんつらくなってきました」というお気持ち、打ち明けてくださってありがとうございます。それは、これまでの不安や心労が、心と体に重くのしかかっているサインなのかもしれませんね。

経済的な不安、うまくいかない就職活動、そして誰にも分かってもらえない孤立感。これだけのことをお一人で抱えていらっしゃれば、心も体も疲れてしまうのは当然のことです。ご自身をどうか責めないでくださいね。

このようなおつらい状況だからこそ、一人で抱え込まずに誰かに話すことが大切だと思います。前回お伝えしたことと重なりますが、もしよろしければ、当法人の相談員が直接お話を伺い、今のお気持ちやこれからのことを一緒に考えていく、ということはできそうでしょうか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789852343", "jst_text": "9月20日（日）6時12分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 18, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "need_basis": "先月失職して残りの貯金が約3ヶ月分であり、再就職先が決まらない中で小学生の子どもの習い事をやめさせるか悩むなど生活基盤が揺らいでいる。またハローワークや家族・妻との関係でも頼れる先がなく孤立している。", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "提案"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 6, "phase": "提案", "closing_reason": ""}
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
- 定数生成（true文字列）／版 2026-09-20a
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

## 19通目

- 送った文: `昼間もぼんやりして、何もしない日があります。`
- Dify側の時刻(JST): 2026-09-20 06:12:42
- 所要: 20.8秒 ／ 返事 692字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
おつらい中、お話しいただきありがとうございます。
「昼間もぼんやりして、何もしない日がある」のですね。これまで本当に一人で頑張ってこられたので、心と体が休息を求めているのかもしれません。ご自身を責めないでくださいね。

ここまでお話しいただいたことを、改めて整理させてください。

1ヶ月前に上司とのことでお仕事を辞め、約3ヶ月分の貯金で家賃を支払う不安の中、必死で就職活動をしても年齢を理由に断られるなど、先が見えない状況が続いていること。
誰にも頼れず、奥様に話しても気持ちを分かってもらえない孤立感の中で、お子さんのことまで考えなければならず、ついに「朝起きるのがつらく」「昼間もぼんやり」してしまうほど、心と体が疲れ果ててしまっている。

このようにお見受けしましたが、いかがでしょうか。

---

お話を伺っていて、経済的な不安ももちろんですが、それ以上に、このどうしようもない状況を誰にも理解してもらえず、一人で抱え込み続けた結果、心と体のエネルギーが尽きかけていることが、今一番おつらいことなのではないかと感じました。

これは、ご自身が弱いからではなく、あまりにも多くの重荷を一人で背負ってこられた結果だと思います。

このまま一人で抱え続けるのは、心と体にとって本当につらい状況です。経済的なこと、お仕事のこと、そして今のお体のこと、すべて含めて専門の相談員が直接お話を伺い、具体的な解決策を一緒に探していくことができます。

今日お話しいただいたこの内容を、当法人の相談員に直接伝え、今後の具体的なサポートを一緒に考えていきたいと思いますが、よろしいでしょうか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789852363", "jst_text": "9月20日（日）6時12分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "提案", "session_turns": 19, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "need_basis": "失業中で貯金が約3ヶ月分しかなく、求人が少ない中で再就職が決まらない。周囲に頼れる人がおらず孤立しており、体調・精神面での不調も表れ始めているため。", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "提案"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 6, "phase": "提案", "closing_reason": ""}
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
- 定数生成（true文字列）／版 2026-09-20a
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

## 20通目

- 送った文: `もう少し話を聞いてほしいです。`
- Dify側の時刻(JST): 2026-09-20 06:13:04
- 所要: 16.3秒 ／ 返事 153字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
もちろんです。お気持ちを急かしてしまったかもしれませんね。大変申し訳ありませんでした。

あなたのペースでお話しいただくことが一番大切です。安心してお聞かせください。

今、もう少し話したいと感じていらっしゃるのは、どのようなことでしょうか。どんなことでも構いませんので、お気持ちをお聞かせいただけますか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789852385", "jst_text": "9月20日（日）6時13分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "提案", "session_turns": 20, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "need_basis": "離職中で貯金残高が約3ヶ月分しかなく、求人が少ないうえに不採用が続き、ハローワークへの再訪や親・妻との関係において孤立し、朝起きられないなどの心身の不調が出ているため。", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 6, "phase": "整理", "closing_reason": ""}
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
- 定数生成（true文字列）／版 2026-09-20a
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

## 21通目

- 送った文: `以前は休みの日に走っていましたが、最近はしていません。`
- Dify側の時刻(JST): 2026-09-20 06:13:21
- 所要: 17.0秒 ／ 返事 252字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
お話しいただきありがとうございます。
以前は休みの日に走ることを習慣にされていたのですね。それが「最近はしていません」とのこと、これまで気分転換やご自身を支える時間になっていたかもしれない大切な習慣さえも、今は手につかない状況なのですね。

朝起きるのがつらかったり、昼間ぼんやりしてしまったりするのと同じように、走るための気力やエネルギーも、今は使い果たしてしまっているような感覚でしょうか。

好きだったことや、これまで当たり前にできていたことができなくなるのは、ご自身にとってどんな感じがしますか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789852402", "jst_text": "9月20日（日）6時13分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "整理", "session_turns": 21, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "need_basis": "1ヶ月前に失業し、残りの貯金が約3ヶ月分で家賃5万5千円の負担がある中、就職活動が難航して精神的・体調面（朝起きられない、ぼんやり過ごす）にも影響が出ている。周囲に頼れる相談先がない状況が続いている。", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
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
- 定数生成（true文字列）／版 2026-09-20a
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

## 22通目

- 送った文: `体重が3キロ減りました。`
- Dify側の時刻(JST): 2026-09-20 06:13:40
- 所要: 20.4秒 ／ 返事 295字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
お話しいただきありがとうございます。
体重が3キロも減ってしまったのですね。ご自身の知らないうちに、それだけお体に変化が出ていることに、ご自身でも驚かれたでしょうし、とても心配になりますよね。

朝起きるのがつらい、昼間ぼんやりしてしまう、好きだったランニングも手につかない、そして体重まで減ってしまうというのは、心と体が限界に近いというサインなのかもしれません。それだけ大きなストレスを、ずっと一人で抱えてこられたのだと思います。

もし差し支えなければ教えていただきたいのですが、お食事はきちんととれていますか。食欲がなかったり、食事を準備する気力もわかなかったりすることもありますか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789852420", "jst_text": "9月20日（日）6時13分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 22, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "need_basis": "1ヶ月前に離職し、約3ヶ月分の貯金で家賃5万5千円を払う中で就業できず、生活基盤が崩れ始めている。さらに妻や親、ハローワークなど頼れる支援先がなく孤立しており、心身の不調や体重減少も生じている。", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
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
- 定数生成（true文字列）／版 2026-09-20a
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

## 23通目

- 送った文: `健康保険の切り替えの手続きがまだ途中です。`
- Dify側の時刻(JST): 2026-09-20 06:14:01
- 所要: 17.8秒 ／ 返事 382字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
お話しいただきありがとうございます。
健康保険の切り替え、大切な手続きだと分かっていても、なかなか手がつけられない状況なのですね。これまでお話しいただいたように、心と体が疲れ切っている中では、そうした手続きを進める気力がわかなくても無理はありません。ご自身を責めないでくださいね。

ここまでお話しいただいたことを、一度整理させてください。

1ヶ月前に退職されてから、経済的な不安や就職活動の難航、ご家族にも理解してもらえない孤立感を、ずっとお一人で抱えてこられたのですね。
その結果、朝起きるのがつらくなったり、体重が3キロ減ってしまったりと、心身ともに疲れ果ててしまい、ついに「健康保険の切り替えの手続きがまだ途中です」というように、日常生活に必要なことさえ手につかないほど追い詰められている。

このようにお見受けしましたが、ずれているところはありますか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789852441", "jst_text": "9月20日（日）6時14分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 23, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "need_basis": "無職で貯金が僅かな中、再就職が難航しており、意欲低下や体重減少（3kg）など心身の不調が現れている。家族や公的機関など頼れる支援先につながらず孤立した状態で、生活基盤が崩れ始めているため。", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
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
- 定数生成（true文字列）／版 2026-09-20a
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

## 24通目

- 送った文: `近いです。`
- Dify側の時刻(JST): 2026-09-20 06:14:20
- 所要: 18.7秒 ／ 返事 242字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
お気持ちを共有させていただき、ありがとうございます。ここまでお話しいただいたことで、少しでもあなたの心が軽くなるお手伝いができればと思っています。

お話を伺っていて、お金のことや手続きのことなど、目の前の課題ももちろん大きいですが、それ以上に、このどうしようもない状況を誰にも頼れず、たった一人で抱え込み続けた結果、心と体のエネルギーがほとんど尽きかけてしまっていること。それが、今一番おつらいことなのではないかと感じました。

この点について、ご自身ではどのように感じられますか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789852460", "jst_text": "9月20日（日）6時14分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 24, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "need_basis": "1ヶ月前に退職し、約3ヶ月分の貯金も底をつきつつある中で就職活動が難航しており、頼れる相手や支援先もないまま意欲の低下や体重減少（3kg減）など心身に不調をきたし、手続き（健康保険の切り替え）も滞っているため。", "contact_safety_risk": "2", "crisis_category": "生活困窮・ライフライン", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "整理"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 6, "phase": "整理", "closing_reason": ""}
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
- 定数生成（true文字列）／版 2026-09-20a
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

## 25通目

- 送った文: `失業保険の手続きは済ませました。`
- Dify側の時刻(JST): 2026-09-20 06:14:39
- 所要: 24.2秒 ／ 返事 622字 ／ ノード 26個

**返ってきた本文（そのまま）**

```
おつらい中、失業保険の手続きは済まされたのですね。心も体も大変な状況で、本当に大変だったと思います。よく頑張られましたね。

ここまでお話しいただいたことを、最後に整理させてください。

1ヶ月前に退職されてから、約3ヶ月分の貯金で家賃を支払う経済的な不安や、10社応募しても決まらない就職活動の難しさ、そしてご家族にも頼れない孤立感を、ずっとお一人で抱えてこられました。
その結果、朝起きられない、体重が3kg減るなど心身の不調が現れ、健康保険の手続きも手につかないほど追い詰められている。それでも「失業保険の手続きは済ませました」と、必死で状況を立て直そうとされているのですね。

お話を伺っていて、目の前の課題も大きいですが、何より、このどうしようもない状況を誰にも頼れず、たった一人で抱え込み続けた結果、心と体のエネルギーが尽きかけていることが、今一番おつらいことなのだと感じました。

失業保険の手続きを済まされたのは、「なんとかしなければ」という強い責任感の表れだと思います。ですが、その責任感が、かえってご自身を追い詰めているのかもしれません。今はまず、誰かの助けを借りて、心と体を休めることが必要なのではないでしょうか。

もしよろしければ、今日お話しいただいたこの内容を当法人の相談員にお伝えして、今後の具体的なサポート（公的な支援制度の利用や、お仕事探しのお手伝いなど）を一緒に考えていきたいと思いますが、いかがでしょうか。
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789852480", "jst_text": "9月20日（日）6時14分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "整理", "session_turns": 25, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "need_basis": "1ヶ月前に退職し失業中で、約3ヶ月分の貯金で家賃を支払わなければならない状況の中、再就職活動が難航している。頼れる相談相手もおらず孤立しており、朝起きるのがつらい、体重が3kg減少するなど心身の不調や手続きの滞りが生じている。", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（相談外の連続カウント）
  → {"new_streak": 0, "pattern": "通常", "rum_streak": 0}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "true", "alerted_at": "1789852480", "closing": "true", "max_safety_risk": 2, "max_support_need": 6, "phase": "終了", "closing_reason": "往復上限"}
IF/ELSE 11（危機の速報判定）
  → {"selected_case_id": "false"}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "true"}
IF/ELSE 19（採点やり直しの関門）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "経済的な困窮", "next_action": "まずは心身の休息を確保しつつ、生活の安定を図ることが急務。相談員が直接話を伺い、①利用可能な公的支援制度（住居確保給付金など）の情報提供と申請支援、②ハローワークの専門相談（キャリアコンサルティング等）への同行支援や履歴書の添削サポート、③心身の不調について医療機関への受診勧奨と、必要であれば同行支援を検討する。本人の孤立感が強いため、定期的なコミュニケーションを通じて伴走支援を行い、社会的つながりを再構築していく。", "related_issue": "失業、再就職の困難、孤立・孤独、心身の不調", "summary": "1ヶ月前に上司との人間関係が原因で退職し、失業中。貯金は約3ヶ月分しかなく、家賃の支払いに強い不安を感じている。42歳という年齢もあり、10社に応募しても面接は1社のみで不採用となり、再就職活動が難航している。親には退職を言えず、妻に相談しても理解を得られず孤立。朝起きられない、体重3kg減、好きだったランニングができないなど心身の不調が悪化しており、健康保険の切り替え手続き
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": "いいえ"}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-20a
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
- 変数代入（長時間アラートタイムスタンプ）
- IF/ELSE 19（採点やり直しの関門）
- LLM
- 返信整形（サマリー除去）
- 回答
- IF/ELSE 6（引き継ぎサマリー有無）
- パラメータ抽出3（有人対応同意）
- IF/ELSE 4（有人対応同意判定）

</details>

---

## 26通目

- 送った文: `もう少しだけ話してもいいですか。`
- Dify側の時刻(JST): 2026-09-20 06:15:05
- 所要: 1.8秒 ／ 返事 301字 ／ ノード 16個

**返ってきた本文（そのまま）**

```
お知らせいただき、ありがとうございます。
いただいた内容は、記録として残ります。

今日はここで一度お休みとさせてください。お気持ちが落ち着いてお話しできる時をお待ちしております。

いま伝えておきたいことがあれば、下記からご記入ください。
こちらも記録として残ります。

▼ お伝えしたいこと・状況の変化
https://liff.line.me/2010836980-ms5nFPQE?mode=note

お急ぎでどなたかとお話ししたいときは、下記もご利用いただけます。
・#いのちSOS　0120-061-338（24時間365日）
・よりそいホットライン　0120-279-338（24時間）
```

**判定・分岐ノードの出力**

```
現在時刻取得（UNIX秒・日本時間・窓口の開閉）
  → {"value": "1789852505", "jst_text": "9月20日（日）6時15分", "office_open": "false", "next_open": "9月24日（木）の朝8時30分", "holiday_known": "true"}
経過時間判定（ロック解除チェック）
  → {"length_expired": "false", "summary_expired": "false", "today": "20716"}
コード（期限切れの解除・経過ターン計算）
  → {"closing": "true", "length_alerted": "true", "phase": "終了", "session_turns": 26, "summary_notified": "", "turn_base": 0, "post_landing_note": "true", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "post-landing-note"}
コード（着地後書き込みの速報判定と本文）
  → {"should_alert": "", "payload": "", "day": ""}
IF/ELSE 15（着地後書き込みの速報判定）
  → {"selected_case_id": "false"}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-20a
- 現在時刻取得（UNIX秒・日本時間・窓口の開閉）
- 経過時間判定（ロック解除チェック）
- コード（期限切れの解除・経過ターン計算）
- 変数代入（期限切れの解除）
- IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
- 追記本文抽出
- HTTP リクエスト（相談記録登録：追記）
- コード（着地後書き込みの速報判定と本文）
- IF/ELSE 18（区切りのあと・緊急でなく採点やり直しでもない）
- IF/ELSE 15（着地後書き込みの速報判定）
- 回答（長時間相談区切り）
- コード（追記保存の結果判定）
- IF/ELSE 13（追記保存の失敗チェック）

</details>

---
