### [ ⏎ 戻る](../learning-journal.md)
# 主要プロバイダの OAuth 認証＆ユーザー情報取得仕様まとめ
### 各詳細ファイル :
[Google](./oauth/google.md) ・ 
[Apple](./oauth/apple.md) ・ 
[Yahoo!JAPAN](./oauth/yahoo.md) ・
[Yahoo! (米国版)](./oauth/yahoo-usa.md) ・
[Facebook](./oauth/facebook.md)・ 
[Alipay+](oauth/alipay+.md) ・ 
[中国大陸版Alipay](oauth/alipay.md)


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
### OIDCとは？

- OpenID Connect (OIDC) は、OAuth 2.0プロトコルの上に構築された、シンプルで相互運用可能な認証レイヤーです。<br>
- ユーザーの身元を検証し、その基本的なプロフィール情報を、認可サーバー（Identity Provider: IdP）からクライアントアプリケーションへ提供することを主な目的としています。

- [詳細へ 📖](./oidc/oidc.md)


### [ ⏎ 戻る](../learning-journal.md)