# 台本L 生出力（第36版）

- 利用者ID: `t-36-L`
- 会話ID: `37ec7798-c6ce-4ae3-8c02-1ed3e8cdf67d`
- 版の目印: `定数生成（true文字列）／版 2026-09-20b`

本文は一字も直していません。

---

## 1通目

- 送った文: `仕事を辞めてから、これからのことが不安です。`
- Dify側の時刻(JST): 2026-09-20 13:45:38
- 所要: 15.6秒 ／ 返事 192字 ／ ノード 32個

**返ってきた本文（そのまま）**

```
ご連絡ありがとうございます。
お仕事を辞められて、これからどうしようかと、心細い気持ちでいらっしゃるのですね。

「これからのことが不安です」というお気持ち、お話しくださってありがとうございます。

もしよろしければ、その不安がどのようなことか、もう少し詳しく教えていただけますか。例えば、お金のこと、次の仕事のこと、あるいは何か別のことでしょうか。もちろん、話せる範囲で構いません。
```

**判定・分岐ノードの出力**

```
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "受付", "session_turns": 1, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "5", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 5, "phase": "傾聴", "closing_reason": ""}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "related_issue": "", "urgency": "", "consent": "", "phone_removed": "", "forced_close": ""}
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
- 定数生成（true文字列）／版 2026-09-20b
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
- Dify側の時刻(JST): 2026-09-20 13:45:54
- 所要: 13.3秒 ／ 返事 166字 ／ ノード 29個

**返ってきた本文（そのまま）**

```
そうだったのですね。先月までお勤めだったのですね。
「上司との折り合いが悪かった」とのこと、お仕事を辞める決断をされるまで、大変な思いをされたこととお察しします。つらい状況の中、よくここまで持ちこたえてこられましたね。

お仕事を辞められてから今日まで、どのようなお気持ちで過ごしてこられたか、もしよろしければ教えていただけますか。
```

**判定・分岐ノードの出力**

```
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 2, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "5", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 5, "phase": "傾聴", "closing_reason": ""}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "related_issue": "", "urgency": "", "consent": "", "phone_removed": "", "forced_close": ""}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-20b
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
- Dify側の時刻(JST): 2026-09-20 13:46:09
- 所要: 15.5秒 ／ 返事 175字 ／ ノード 29個

**返ってきた本文（そのまま）**

```
そうだったのですね。「同じ業界で探している」けれど、「求人が少ない」という状況なのですね。

ご自身の経験を活かせる場所を探しているのに、選択肢が少ないと、焦るお気持ちや、この先どうなるんだろうという不安も大きくなりますよね。

差し支えなければお聞きしたいのですが、お仕事を探されている間、日々の生活費など、暮らしの面でのご心配はいかがでしょうか。
```

**判定・分岐ノードの出力**

```
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 3, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "5", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 5, "phase": "傾聴", "closing_reason": ""}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "related_issue": "", "urgency": "", "consent": "", "phone_removed": "", "forced_close": ""}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-20b
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
- Dify側の時刻(JST): 2026-09-20 13:46:25
- 所要: 17.5秒 ／ 返事 206字 ／ ノード 29個

**返ってきた本文（そのまま）**

```
お返事ありがとうございます。
「貯金は3か月分くらいしかありません」とのこと、打ち明けてくださってありがとうございます。

お仕事を探している間にも、貯金が少しずつ減っていくのを見ると、本当に心細くなりますよね。求人が少ない状況も重なって、焦るお気持ちや将来への不安が、日に日に大きくなっているのではないかと感じました。

このようなご状況について、ご家族やご友人など、身近な方にお話しすることはできていますか。
```

**判定・分岐ノードの出力**

```
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 4, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "5", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 5, "phase": "傾聴", "closing_reason": ""}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "related_issue": "", "urgency": "", "consent": "", "phone_removed": "", "forced_close": ""}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-20b
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

- 送った文: `家賃は月に5万5千円です。`
- Dify側の時刻(JST): 2026-09-20 13:46:44
- 所要: 17.6秒 ／ 返事 215字 ／ ノード 29個

**返ってきた本文（そのまま）**

```
家賃が月に5万5千円とのこと、具体的な金額を教えてくださってありがとうございます。
お仕事を探している間も、毎月決まった額の支払いがあるというのは、大きなご負担ですよね。「貯金は3か月分くらい」というお話もありましたので、その中で家賃を払い続けることに、強いプレッシャーを感じていらっしゃるのではないかと思います。

差し支えなければ、もう少し教えてください。家賃の支払いが続く中で、今一番気がかりなのはどのようなことでしょうか。
```

**判定・分岐ノードの出力**

```
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 5, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 6, "phase": "傾聴", "closing_reason": ""}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "related_issue": "", "urgency": "", "consent": "", "phone_removed": "", "forced_close": ""}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-20b
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
- Dify側の時刻(JST): 2026-09-20 13:47:02
- 所要: 16.4秒 ／ 返事 296字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
10社も履歴書を送られたのですね。たくさん行動されているのに、面接まで進めたのが1社だけだったというのは、気持ちが折れそうになりますよね。ご自身の経歴を否定されたように感じて、とてもおつらいのではないかと思います。

これまでのことを整理させてください。先月お仕事を辞められ、求人が少ない業界で懸命に活動されている。その一方で、家賃の支払いは続き、「貯金は3か月分くらい」という現実的な不安も抱えていらっしゃる。本当に、心休まらない日々を過ごされていることと思います。

このような大変な状況について、ハローワークの相談員さんや、ご家族、ご友人など、どなたかにお話しすることはできていますか？
```

**判定・分岐ノードの出力**

```
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 6, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 6, "phase": "傾聴", "closing_reason": ""}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "related_issue": "", "urgency": "", "consent": "", "phone_removed": "", "forced_close": ""}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-20b
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
- Dify側の時刻(JST): 2026-09-20 13:47:20
- 所要: 18.4秒 ／ 返事 275字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
やっとの思いで進んだ面接で、年齢のことを言われて断られてしまったのですね。
それは本当に悔しくて、やりきれない気持ちになりますよね。ご自身の力ではどうにもならないことで判断されてしまうのは、ひどく傷つきますし、これまでの頑張りを否定されたように感じてしまいますよね。

10社も応募されて、やっとたどり着いた一社でそのような対応をされると、心が折れそうになるのも無理はないと思います。

これだけ大変なことを、もしお一人で抱えていらっしゃるとしたら、本当に心細いだろうと思います。ご家族やご友人など、誰かに話したり、頼ったりすることはできていますか？
```

**判定・分岐ノードの出力**

```
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 7, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 6, "phase": "傾聴", "closing_reason": ""}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "related_issue": "", "urgency": "", "consent": "", "phone_removed": "", "forced_close": ""}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-20b
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
- Dify側の時刻(JST): 2026-09-20 13:47:39
- 所要: 17.1秒 ／ 返事 283字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
42歳でいらっしゃるのですね。教えてくださってありがとうございます。
働き盛りで、まだまだこれからというときに、「年齢のことを言われて」断られてしまうのは、本当に理不尽で悔しい思いをされたこととお察しします。

先月から必死でお仕事を探し、やっと進んだ面接でそのような対応をされると、これまでの頑張りまで否定されたように感じて、心が折れそうになりますよね。貯金が減っていく不安の中で、もしこの状況とたった一人で向き合っているとしたら、本当に心細いと思います。

差し支えなければ、このどうしようもないお気持ちを、誰かに話したい、聞いてほしいと感じることはありますか？
```

**判定・分岐ノードの出力**

```
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 8, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 6, "phase": "傾聴", "closing_reason": ""}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "related_issue": "", "urgency": "", "consent": "", "phone_removed": "", "forced_close": ""}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-20b
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

- 送った文: `履歴書の書き方が合っているのか分かりません。`
- Dify側の時刻(JST): 2026-09-20 13:47:57
- 所要: 16.3秒 ／ 返事 245字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
面接でつらい思いをされた後だと、「履歴書の書き方が合っているのか分からない」とご自身のやり方に自信が持てなくなってしまうのも、無理はないと思います。何度も書類を準備する中で、これでいいのだろうかと不安になりますよね。

面接で年齢のことを言われてしまった経験から、ご自身の書類の書き方にまで原因があるのではないかと、お一人で悩んでいらっしゃるのかもしれないと感じました。

その履歴書の書き方について、例えばハローワークの職員さんなど、誰かに相談したり、見てもらったりしたことはありますか？
```

**判定・分岐ノードの出力**

```
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 9, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 6, "phase": "傾聴", "closing_reason": ""}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "related_issue": "", "urgency": "", "consent": "", "phone_removed": "", "forced_close": ""}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-20b
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

- 送った文: `ハローワークには一度だけ行きました。`
- Dify側の時刻(JST): 2026-09-20 13:48:14
- 所要: 16.6秒 ／ 返事 232字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
ハローワークに一度、足を運ばれたのですね。行動されたこと、教えてくださってありがとうございます。

お一人で10社も応募書類を準備され、ハローワークにも足を運ばれた。先の見えない不安の中で、ご自身でできることを懸命に探してこられたのですね。

「一度だけ」行かれたとのことですが、もし差し支えなければ、その時のご様子を少し教えていただけますか。例えば、履歴書の書き方について相談できそうだったか、あるいは何か話しにくい雰囲気だったかなど、どんなことでも構いません。
```

**判定・分岐ノードの出力**

```
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 10, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 6, "phase": "傾聴", "closing_reason": ""}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "related_issue": "", "urgency": "", "consent": "", "phone_removed": "", "forced_close": ""}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-20b
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

- 送った文: `担当の方は親切でしたが、また行くのが気まずいです。`
- Dify側の時刻(JST): 2026-09-20 13:48:32
- 所要: 17.3秒 ／ 返事 228字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
担当の方は親切だったのですね。それにもかかわらず、「また行くのが気まずい」と感じていらっしゃるのですね。
一度相談に乗ってもらった手前、何か良い報告ができないと顔を合わせにくいと感じたり、不採用が続いていることを改めて話すのがつらいと感じたりすることもあるかもしれませんね。

その「気まずい」というお気持ちは、もう少し具体的にお聞きすると、どのような感覚に近いでしょうか。もちろん、もし言葉にしづらいようでしたら、無理にお話しいただかなくても大丈夫です。
```

**判定・分岐ノードの出力**

```
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 11, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 6, "phase": "傾聴", "closing_reason": ""}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "related_issue": "", "urgency": "", "consent": "", "phone_removed": "", "forced_close": ""}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-20b
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

- 送った文: `親には辞めたことをまだ言えていません。`
- Dify側の時刻(JST): 2026-09-20 13:48:50
- 所要: 17.9秒 ／ 返事 245字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
ご両親に、お仕事を辞められたことをまだお話しできていないのですね。
大切なことを打ち明けてくださって、ありがとうございます。

ハローワークの方にも気まずさを感じ、ご両親にもまだ言えないとなると、この大きな不安を本当にたったお一人で抱えてこられたのですね。それは、とても心細かったことと思います。

「親には辞めたことをまだ言えていない」とのことですが、もし差し支えなければ、言えない背景にあるお気持ちを少しだけ教えていただけますか。例えば、心配をかけたくない、といったお気持ちでしょうか。
```

**判定・分岐ノードの出力**

```
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 12, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "生活・制度", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 6, "phase": "傾聴", "closing_reason": ""}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "related_issue": "", "urgency": "", "consent": "", "phone_removed": "", "forced_close": ""}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-20b
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

- 送った文: `実家は県外で、年に一度しか帰っていません。`
- Dify側の時刻(JST): 2026-09-20 13:49:09
- 所要: 21.5秒 ／ 返事 273字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
ご実家は県外なのですね。年に一度しか帰られていないとのこと、教えてくださってありがとうございます。

ハローワークの方には気まずさを感じ、遠く離れたご両親には心配をかけたくて打ち明けられない。そうすると、今抱えていらっしゃる大きな不安を、本当に誰にも話せず、お一人で向き合ってこられたのですね。

たった一人でこの状況を乗り越えようとされているのは、本当に大変なことだと思います。差し支えなければ、今一番、誰かに「こうしてほしい」と感じることはありますか。例えば、ただ話を聞いてほしい、具体的なアドバイスがほしい、など、どんなことでも構いません。
```

**判定・分岐ノードの出力**

```
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 13, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 6, "phase": "傾聴", "closing_reason": ""}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "related_issue": "", "urgency": "", "consent": "", "phone_removed": "", "forced_close": ""}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-20b
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

- 送った文: `妻には話しましたが、あまり反応がありませんでした。`
- Dify側の時刻(JST): 2026-09-20 13:49:32
- 所要: 16.9秒 ／ 返事 269字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
奥様にはお話しされたのですね。
勇気を出して打ち明けたのに、「あまり反応がありませんでした」というのは、とても寂しく、おつらい気持ちになりますよね。一番身近な方に分かってもらえないと、まるで世界でたった一人になってしまったような心細さを感じてしまいますよね。

ご両親にも言えず、ハローワークにも行きづらい中で、奥様にも気持ちを受け止めてもらえなかった。本当に、誰にも頼れないというお気持ちでいらっしゃるのではないでしょうか。

もし差し支えなければ、奥様の反応がなかったとき、どのようなお気持ちになったか、もう少し教えていただけますか。
```

**判定・分岐ノードの出力**

```
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 14, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 6, "phase": "傾聴", "closing_reason": ""}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "related_issue": "", "urgency": "", "consent": "", "phone_removed": "", "forced_close": ""}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-20b
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

- 送った文: `子どもが小学生で、習い事をやめさせようか迷っています。`
- Dify側の時刻(JST): 2026-09-20 13:49:50
- 所要: 19.3秒 ／ 返事 308字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
お子さんの習い事のことまで考えなければならない状況なのですね。
ご自身のことで精一杯な中で、「習い事をやめさせようか迷っている」というのは、親として本当に苦しい決断だと思います。お子さんの楽しみを自分のせいで奪ってしまうかもしれないと、ご自身を責めるようなお気持ちになっていないでしょうか。

お仕事が見つからない焦り、貯金が減っていく不安、そして誰にもこの苦しさを分かってもらえない孤独感。そのすべてを一人で抱えながら、お子さんのことまで考えなければならないのは、本当に胸が張り裂けるような思いだと思います。

差し支えなければ教えてください。お子さんのことを考えたとき、今一番、何が気がかりでいらっしゃいますか。
```

**判定・分岐ノードの出力**

```
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 15, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "5", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 6, "phase": "傾聴", "closing_reason": ""}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "related_issue": "", "urgency": "", "consent": "", "phone_removed": "", "forced_close": ""}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-20b
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

- 送った文: `朝起きるのがだんだんつらくなってきました。`
- Dify側の時刻(JST): 2026-09-20 13:50:10
- 所要: 18.0秒 ／ 返事 406字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
お仕事を失った不安や、誰にも分かってもらえない孤独感を抱えながら、お子さんのことまで考えてこられたのですね。「朝起きるのがだんだんつらくなってきました」というお言葉に、これまでお一人で抱えてこられたお気持ちの重さが、心だけでなく、お体にも表れているようで、とても心配です。

これまでのことを、少しだけ一緒に整理させていただけますか。

先月お仕事を辞められ、貯金が減っていく不安の中、懸命に就職活動を続けてこられました。しかし、面接では年齢を理由に断られ、ハローワークにも行きづらさを感じていらっしゃる。ご家族にも打ち明けられず、奥様に話しても気持ちを受け止めてもらえなかった。そして、お子さんの習い事のことまで悩み、心身ともに疲れ果ててしまっている。

もし、この受け止め方が少しでも近いと感じるところがあれば、教えていただけますか。もちろん、違うと感じる部分があれば、それも遠慮なくおっしゃってくださいね。
```

**判定・分岐ノードの出力**

```
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 16, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 6, "phase": "傾聴", "closing_reason": ""}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "related_issue": "", "urgency": "", "consent": "", "phone_removed": "", "forced_close": ""}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-20b
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

- 送った文: `昼間もぼんやりして、何もしない日があります。`
- Dify側の時刻(JST): 2026-09-20 13:50:29
- 所要: 20.4秒 ／ 返事 277字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
お昼の間もぼんやりと過ごされ、何も手につかない日があるのですね。
朝起きるのがつらいだけでなく、日中も気力が湧かないというのは、これまで張り詰めてこられた心と体が、もう限界だよとサインを出しているのかもしれません。本当に、おつらい状況だと思います。

お話を伺っていて、私が一番重いと感じたのは、再就職への焦りやお金の心配といった大きなプレッシャーをたったお一人で抱え、誰にも頼れない孤独の中で、心と体が「もう動けないよ」と悲鳴をあげていることではないか、ということです。

このようにお伝えしましたが、近い感じがしますか。それとも、少し違うでしょうか。
```

**判定・分岐ノードの出力**

```
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 17, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "整理"}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 1, "max_support_need": 6, "phase": "整理", "closing_reason": ""}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "related_issue": "", "urgency": "", "consent": "", "phone_removed": "", "forced_close": ""}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-20b
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

- 送った文: `近いです。`
- Dify側の時刻(JST): 2026-09-20 13:50:51
- 所要: 17.8秒 ／ 返事 342字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
「近いです」とお答えいただき、ありがとうございます。
これまでのお気持ちを、少しでも分かち合えたようで、少しだけ安心しました。

これは私の推測なので、もし違っていたら遠慮なく教えてほしいのですが、もしかすると、「早く次の仕事を見つけなければ」「家族を支えなければ」という強い責任感から、ご自身の心と体が限界を迎えていることに、気づかないふりをされているのではないでしょうか。

「朝起きられない」ことや「昼間もぼんやりして」しまうのは、決して気持ちが弱いからではなく、これまでの大きなストレスと誰にも頼れない孤独によって、心のエネルギーが尽きかけているサインなのかもしれません。

このようにお伝えしましたが、いかがでしょうか。もし、少しでも思い当たるところがあれば教えてください。
```

**判定・分岐ノードの出力**

```
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "整理", "session_turns": 18, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "contact_safety_risk": "2", "crisis_category": "生活困窮・ライフライン", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "提案"}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 6, "phase": "提案", "closing_reason": ""}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "related_issue": "", "urgency": "", "consent": "", "phone_removed": "", "forced_close": ""}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-20b
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

- 送った文: `以前は休みの日に走っていましたが、最近はしていません。`
- Dify側の時刻(JST): 2026-09-20 13:51:09
- 所要: 19.0秒 ／ 返事 428字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
お好きだったランニングもできないほど、心と体がお疲れ果てていらっしゃるのですね。これまで当たり前にできていたこと、楽しめていたことさえ手につかなくなってしまうのは、本当におつらいことだと思います。

これまでお話しいただいた、お仕事の不安、ご家族のこと、そして心と体のつらさ。これらはすべて複雑に絡み合っていて、お一人で抱えるにはあまりにも重すぎると感じています。

文字だけのやり取りでは、支えきれない部分もあると思います。
もしよろしければ、ここでお話しいただいた内容を当法人の相談員にお伝えして、今後の具体的なサポートを一緒に考えていく、というのはいかがでしょうか。専門の相談員が直接お話をうかがい、まずはお気持ちの整理をしながら、生活を立て直す方法を一緒に探していくことができます。

このままお話を相談員にお伝えして、こちらからご連絡を差し上げてもよろしいでしょうか。もちろん、もし修正したい点や付け加えたいことがあれば、遠慮なく教えてください。
```

**判定・分岐ノードの出力**

```
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "提案", "session_turns": 19, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "提案"}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 6, "phase": "提案", "closing_reason": ""}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "related_issue": "", "urgency": "", "consent": "", "phone_removed": "", "forced_close": ""}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-20b
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
- Dify側の時刻(JST): 2026-09-20 13:51:29
- 所要: 16.3秒 ／ 返事 223字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
もちろんです。お話しくださってありがとうございます。
先ほどは少し急いでしまいましたね。申し訳ありません。あなたのペースでお話しいただくことが一番大切ですので、どうぞ安心してお聞かせください。

「もう少し話を聞いてほしい」というお気持ち、よく分かりました。
まだ言葉にできていないことや、整理しきれていない思いがたくさんあるのだと思います。

どのようなことについて、もう少しお話ししたいと感じていらっしゃいますか。どんなことでも大丈夫ですよ。
```

**判定・分岐ノードの出力**

```
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "提案", "session_turns": 20, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 6, "phase": "整理", "closing_reason": ""}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "related_issue": "", "urgency": "", "consent": "", "phone_removed": "", "forced_close": ""}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-20b
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

- 送った文: `体重が3キロ減りました。`
- Dify側の時刻(JST): 2026-09-20 13:51:47
- 所要: 20.7秒 ／ 返事 229字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
体重が3キロも減ってしまったのですね。それはとても心配です。
朝起きるのがつらい、日中ぼんやりしてしまうといったことに加え、お体の具体的な変化として現れているのですね。

これまで抱えてこられたストレスや不安が、気づかないうちに心だけでなく、お体にも大きな負担をかけていたのかもしれません。ご自身でも、お体の変化に戸.惑いや不安を感じていらっしゃるのではないでしょうか。

もし差し支えなければ、お食事はとれていますか？食欲がないなど、何か変化はありますか。
```

**判定・分岐ノードの出力**

```
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "整理", "session_turns": 21, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 6, "phase": "傾聴", "closing_reason": ""}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "related_issue": "", "urgency": "", "consent": "", "phone_removed": "", "forced_close": ""}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-20b
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

- 送った文: `健康保険の切り替えの手続きがまだ途中です。`
- Dify側の時刻(JST): 2026-09-20 13:52:08
- 所要: 19.2秒 ／ 返事 260字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
お体のつらい状況に加えて、健康保険の切り替え手続きも途中になっているのですね。教えてくださってありがとうございます。

心も体も疲れているときに、役所の手続きなどを進めるのは本当に大変なことだと思います。頭では「やらなければ」と分かっていても、気力が湧かずに体が動かない、というおつらい状況なのではないかと感じました。

もし差し支えなければ、その手続きのどのあたりで難しさを感じていらっしゃるか、もう少し教えていただけますか。例えば、書類の準備が大変、どこに相談すればいいか分からない、など、どんなことでも構いません。
```

**判定・分岐ノードの出力**

```
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 22, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "contact_safety_risk": "1", "crisis_category": "心身の不調", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 6, "phase": "傾聴", "closing_reason": ""}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "related_issue": "", "urgency": "", "consent": "", "phone_removed": "", "forced_close": ""}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-20b
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

- 送った文: `失業保険の手続きは済ませました。`
- Dify側の時刻(JST): 2026-09-20 13:52:28
- 所要: 20.2秒 ／ 返事 206字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
おつらい中、失業保険の手続きを済ませられたのですね。
心も体も思うように動かない中で、必要な手続きをやり遂げるのは、本当に大変なことだったと思います。生活を立て直すために、ご自身でできることを一つ一つ進めていらっしゃるのですね。

失業保険の手続きを終えられたことで、お金の面の心配は少しだけ軽くなったでしょうか。それとも、それ以上に、お体のつらさや、次のお仕事への不安のほうが大きいと感じていらっしゃいますか。
```

**判定・分岐ノードの出力**

```
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 23, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 6, "phase": "傾聴", "closing_reason": ""}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "related_issue": "", "urgency": "", "consent": "", "phone_removed": "", "forced_close": ""}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-20b
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

- 送った文: `来月から給付が始まる予定です。`
- Dify側の時刻(JST): 2026-09-20 13:52:50
- 所要: 36.4秒 ／ 返事 474字 ／ ノード 25個

**返ってきた本文（そのまま）**

```
来月から給付が始まるのですね。おつらい中、手続きをやり遂げられたこと、本当に大変だったと思います。当面の生活の見通しが少し立ったこと、ひとまず安心材料ですね。

今日うかがったお話から、「『来月から給付が始まる予定です』」という少し先の見通しが立った一方で、「朝起きるのがだんだんつらくなってきました」というお体の不調や、誰にも頼れない孤独感は続いている、と受け止めました。

この重荷を、これ以上お一人で背負う必要はありません。もしご希望でしたら、当法人の相談員が直接お話をうかがい、継続的に寄り添いながら一緒に考えていくことができます。

今日はたくさんのことを話してくださり、本当にありがとうございました。これ以上はかえってお疲れになるかもしれませんので、一度ここで区切らせてください。もし相談員との対話をご希望でしたら、明日以降その旨をお知らせくださいね。

もし今夜、不安で眠れないなどありましたら、24時間つながる窓口もあります。
・よりそいホットライン：0120-279-338

次にお話しできるのは、日付が変わってからになります。
```

**判定・分岐ノードの出力**

```
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 24, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "", "alerted_at": "", "closing": "", "max_safety_risk": 2, "max_support_need": 6, "phase": "傾聴", "closing_reason": ""}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "false"}
返信整形（サマリー除去）
  → {"main_category": "", "related_issue": "", "urgency": "", "consent": "", "phone_removed": "", "forced_close": ""}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-20b
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

- 送った文: `もう少し話を聞いてほしいです。`
- Dify側の時刻(JST): 2026-09-20 13:54:14
- 所要: 19.5秒 ／ 返事 432字 ／ ノード 26個

**返ってきた本文（そのまま）**

```
お気持ちを伝えてくださって、ありがとうございます。
先ほどはこちらの都合で話を終えようとしてしまい、大変失礼いたしました。あなたのペースでお話しいただくことが一番大切ですので、どうぞ安心してくださいね。

「もう少し話を聞いてほしい」とのこと、もちろんです。お話を続けましょう。

失業保険の給付という少し先の見通しが立っても、やはりお体のつらさや、誰にも頼れないというお気持ちはなくならないですよね。

どのようなことについて、もう少しお話ししたいと感じていらっしゃいますか。どんなことでも構いませんので、お聞かせください。

今日はたくさんお話しくださって、ありがとうございました。今日はここで一度お休みしましょう。

今夜、気持ちがつらくなったときは、24時間つながる電話があります。
・#いのちSOS　0120-061-338（24時間）
・よりそいホットライン　0120-279-338（24時間）

次にお話しできるのは、日付が変わってからになります。
```

**判定・分岐ノードの出力**

```
コード（期限切れの解除・経過ターン計算）
  → {"closing": "", "length_alerted": "", "phase": "傾聴", "session_turns": 25, "summary_notified": "", "turn_base": 0, "post_landing_note": "", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "false"}
パラメータ抽出
  → {"__is_success": 1, "__reason": null, "support_need": "6", "contact_safety_risk": "1", "crisis_category": "生活困窮・ライフライン", "support_type": "両方", "interaction_pattern": "通常", "extracted_user_name": "", "extracted_prefecture": "", "extracted_age_group": "", "extracted_gender": "", "extracted_main_issue": "", "next_phase": "傾聴"}
コード（支援必要度の保持・フェーズ・着地判定）
  → {"alerted": "true", "alerted_at": "1789880055", "closing": "true", "max_safety_risk": 2, "max_support_need": 6, "phase": "終了", "closing_reason": "往復上限"}
IF/ELSE 10（着地したときだけ通知する）
  → {"selected_case_id": "true"}
返信整形（サマリー除去）
  → {"main_category": "", "related_issue": "", "urgency": "", "consent": "", "phone_removed": "", "forced_close": "締めを追加"}
IF/ELSE 6（引き継ぎサマリー有無）
  → {"selected_case_id": "false"}
パラメータ抽出3（有人対応同意）
  → {"__is_success": 1, "__reason": null, "consent_status": ""}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-20b
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
- Dify側の時刻(JST): 2026-09-20 13:54:47
- 所要: 3.0秒 ／ 返事 301字 ／ ノード 16個

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
コード（期限切れの解除・経過ターン計算）
  → {"closing": "true", "length_alerted": "true", "phase": "終了", "session_turns": 26, "summary_notified": "", "turn_base": 0, "post_landing_note": "true", "offtrack_streak": 0, "last_pattern": "通常", "urgent": "", "urgent_used": "", "crisis_word": "", "rescore": "", "today": "20716", "rum_streak": 0}
IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
  → {"selected_case_id": "post-landing-note"}
```

<details><summary>通ったノード</summary>

- ユーザー入力
- IF/ELSE 16（カルテ照会はまだか）
- 定数生成（true文字列）／版 2026-09-20b
- 現在時刻取得（UNIX秒・日本時間・窓口の開閉）
- 経過時間判定（ロック解除チェック）
- コード（期限切れの解除・経過ターン計算）
- 変数代入（期限切れの解除）
- IF/ELSE 7（会話継続チェック：重複防止・長時間対策）
- 追記本文抽出
- HTTP リクエスト（相談記録登録：追記）
- IF/ELSE 18（区切りのあと・緊急でなく採点やり直しでもない）
- 回答（長時間相談区切り）
- コード（着地後書き込みの速報判定と本文）
- IF/ELSE 15（着地後書き込みの速報判定）
- コード（追記保存の結果判定）
- IF/ELSE 13（追記保存の失敗チェック）

</details>

---
