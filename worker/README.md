# Cloudflare Worker（tetote-line-dify）

LINE と Dify と Google Apps Script（相談記録シート）をつなぐ中継サーバーです。

## これは何のためのファイルか

本番で動いている Worker の**写し**です。2026-09-11 に Cloudflare の管理画面から取り出しました。

これまで保管場所が管理画面だけで、いつ誰が何を変えたのかが残らない状態でした。ここに置くことで、差分と履歴が追えるようにしています。

## 合言葉（秘密の値）は入っていません

コードは環境変数を参照するだけです（39か所）。値はすべて Cloudflare 側にあります。

参照している環境変数は次の9つです。`LINE_CHANNEL_ACCESS_TOKEN` `LINE_CHANNEL_SECRET` `DIFY_API_KEY` `DIFY_BASE_URL` `GAS_TOKEN` `GAS_URL` `SLACK_WEBHOOK` `CHAT_WEBHOOK` `SESSIONS`（KV）

**このファイルに値を書き込まないでください。このリポジトリは公開されています。**

## 直すときの注意

いまの運用では、本番の編集は Cloudflare の管理画面で行っています。そのため、管理画面で直したら、このファイルも同じ内容に更新してください。

ずれると、あとから「どちらが本番か」が分からなくなります。

## 改行について

元のファイルには CRLF が5か所混ざっていました（残り956か所は LF）。ここでは LF に統一しています。JavaScript の動作は変わりません。
