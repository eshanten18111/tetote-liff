# 修正手順：引き継ぎサマリーがスプレッドシートに保存されない

対象：Dify アプリ「カウンセリングくん」の
**「HTTP リクエスト（相談記録登録：引き継ぎサマリー）」** ノード

---

## 何が起きているか

このノードは、Body（raw text）に JSON を直接書き、その中に要約テキストを
`{{#...#}}` で埋め込んでいます。

```json
{"type":"summary", ... ,"summary":"{{#llm.text#}}"}
```

要約は複数行のテキストなので、**生の改行がそのまま JSON の文字列の中に入り**、
受け取り側（Google Apps Script）の `JSON.parse` が落ちます。

```
{"ok":false,"error":"SyntaxError: Bad control character in string literal in JSON at position 196"}
```

JSON の仕様では、文字列の中の改行は `\n` の2文字にエスケープする必要があります。
生の改行（0x0A）は入れられません。タブや復帰も同じです。

**やっかいな点**：GAS は処理に失敗しても **HTTPステータス 200 を返す**ため、
Dify 上はこのノードが「成功」と表示されます。Slack 通知は別ノードなので届きます。
そのため「Slackには来ているのに台帳には無い」という状態になります。

### 再現確認

GAS と同じ V8 エンジンで再現したところ、エラーメッセージが完全に一致しました。

```
壊れた版: Bad control character in string literal in JSON at position 66 (line 1 column 67)
修正版  : parse成功
```

---

## 修正手順

要約を JSON に埋め込むのをやめ、**コードノードで JSON を組み立てて**から渡します。
`JSON.stringify` が改行を `\n` に正しく変換してくれます。GAS 側の変更は不要です。

### 手順1：今の Body を控える

「HTTP リクエスト（相談記録登録：引き継ぎサマリー）」ノードを開き、
**Body の中身をまるごとコピーしてメモしておいてください。**
どのキー名で送っているかが、このあと必要になります。

（例：`type` `user_id` `user_name` `category` `urgency` `summary` など。
GAS 側がこのキー名で受け取っているので、**キー名は絶対に変えないでください**。）

### 手順2：コードノードを追加する

このHTTPノードの**すぐ手前**に、コードノードを1つ追加します。
名前は「サマリーJSON組み立て」などにしてください。

### 手順3：入力変数を設定する

手順1で控えた Body の中で `{{#○○#}}` になっていた変数を、
コードノードの**入力変数**として登録します。

例：`summary` ← `llm / text`、`user_name` ← `conversation / collected_user_name` など。

### 手順4：コードを貼る

**JavaScript の場合**

```javascript
function main({ summary, user_id, user_name, category, urgency }) {
  return {
    payload: JSON.stringify({
      // ↓ キー名は手順1で控えた Body と完全に同じにすること
      type: "summary",
      user_id: user_id || "",
      user_name: user_name || "",
      category: category || "",
      urgency: urgency || "",
      summary: summary || ""
    })
  };
}
```

**Python3 の場合**

```python
import json

def main(summary: str, user_id: str, user_name: str,
         category: str, urgency: str) -> dict:
    body = {
        # ↓ キー名は手順1で控えた Body と完全に同じにすること
        "type": "summary",
        "user_id": user_id or "",
        "user_name": user_name or "",
        "category": category or "",
        "urgency": urgency or "",
        "summary": summary or "",
    }
    return {"payload": json.dumps(body, ensure_ascii=False)}
```

出力変数に **`payload`（文字列）** を登録してください。

### 手順5：HTTPノードの Body を差し替える

Body は raw text のまま、中身を**この1行だけ**にします。

```
{{#サマリーJSON組み立て.payload#}}
```

※ `{{#...#}}` の中はノードIDになります。変数ピッカーから選んでください。
※ **波かっこや引用符を足さないでください。** payload がすでに完全な JSON です。

### 手順6：確認する

テスト会話を1本流し、着地させてください。
HTTPノードの応答が次のようになれば成功です。

```json
{"ok":true,"row":28}
```

まだ `{"ok":false,...}` が返る場合は、キー名が GAS 側と食い違っています。
手順1で控えた Body と見比べてください。

---

## あわせて直しておきたい2点

### 1. 他の相談記録ノードも同じ作りになっていないか

「相談記録登録：初回受付」「相談記録登録：追記」も raw text の JSON です。
テストでは成功しましたが、これは**たまたま値が1行だったから**です。

たとえば `need_basis`（判定の根拠）に改行が入れば、同じように壊れます。
同じ形に直しておくことをおすすめします。

### 2. 失敗に気づけるようにする

GAS が 200 を返す以上、Dify 側は失敗を検知できません。
HTTPノードの後ろに IF/ELSE を置き、**応答の body に `"ok":false` が含まれていたら
Slack に通知する**分岐を足しておくと、次に同じことが起きたとき即座に分かります。

条件：`HTTPノード / body` が `"ok":false` を **含む**
