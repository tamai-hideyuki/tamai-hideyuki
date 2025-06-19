### [ ⏎ 戻る](../learning-journal.md)
# 主要プロバイダの OAuth 認証＆ユーザー情報取得仕様まとめ
### 各詳細ファイル ☞  [Google](./oauth/google.md) ・ [Apple](./oauth/apple.md) ・ [Yahoo!JAPAN](./oauth/yahoo.md) ・ [Alipay](./oauth/alipay.md) ・ [Facebook](./oauth/facebook.md)

## 概要：

このリポジトリでは、以下の主要 5 サービスにおける OAuth 2.0 認証フローと、認証後のユーザー情報取得手順をひとまとめにしています。

- Google
  - システムステータスページ: https://status.cloud.google.com/

- Apple (Sign in with Apple)
  - システムステータスページ: https://www.apple.com/support/systemstatus/

- Yahoo! JAPAN
  - システムステータスページ: 存在しません。しかし、[LINEヤフー株式会社](https://www.lycorp.co.jp/ja/privacy-security/announcement/) のページで公開されることがあります。

- Alipay+
  - システムステータスページ: 存在しません。

- Facebook
  - システムステータスページ: https://metastatus.com/

---

## 目的：

- 実装の手間を削減：サービスごとに異なるエンドポイントやパラメータを一目で把握

- セキュリティ担保：CSRF・PKCE・署名など、各社推奨のベストプラクティスを押さえた設計

- 可読性向上：Mermaid 図による「流れの可視化」でチーム内共有をスムーズに

---

## ドキュメント内容：

- **各ファイルには下記セクションを用意しています。**

### 認可エンドポイント

- URL・HTTP メソッド

- 必須クエリパラメータ

- リダイレクト／POST レスポンス形式

### トークンエンドポイント

- URL・HTTP メソッド

- 必須リクエストボディまたはクエリパラメータ

- 正常レスポンス JSON 構造

### ユーザー情報取得

- URL・HTTP メソッド

- Authorization ヘッダーやパラメータ

- 取得フィールド一覧

### アクセストークン & リフレッシュトークン

- 有効期限

- 更新手順

- 注意点

### Mermaid シーケンス図

- 認可→トークン→ユーザー情報取得の流れを視覚化

### エラーハンドリング

- 主なエラーコード／レスポンス例

- 再試行・ユーザーフィードバックの指針

 ---
### OIDCとは？

- OpenID Connect (OIDC) は、OAuth 2.0プロトコルの上に構築された、シンプルで相互運用可能な認証レイヤーです。<br>
- ユーザーの身元を検証し、その基本的なプロフィール情報を、認可サーバー（Identity Provider: IdP）からクライアントアプリケーションへ提供することを主な目的としています。

- [詳細へ](./oidc/oidc.md)

---
### 各詳細ファイル ☞  [Google](./oauth/google.md) ・ [Apple](./oauth/apple.md) ・ [Yahoo!JAPAN](./oauth/yahoo.md) ・ [Alipay](./oauth/alipay.md) ・ [Facebook](./oauth/facebook.md)

### [ ⏎ 戻る](../learning-journal.md)