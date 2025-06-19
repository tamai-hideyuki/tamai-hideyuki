### [ ⏎ 戻る](../index.md)

# Yahoo! (米国版) OAuth 2.0 認証フロー


---

## 認可リクエストURL (/request_auth - Authorization Endpoint)
**ユーザーの許可を得るために使用されるエンドポイント**

### URL:
- `https://api.login.yahoo.com/oauth2/request_auth`
- HTTPメソッド: GET または POST

### 必須クエリパラメーター:

- `client_id`: あなたのConsumer Key (アプリケーションのID)。
- `redirect_uri`: 認証後にYahooがユーザーをリダイレクトするURL。ブラウザアクセスがない場合は oob (out-of-band) を指定します。
- `response_type`: code である必要があります。


### 正常時のレスポンス:

Yahooは、ユーザーを認証ページにリダイレクトするために 302 redirect を発行します。  
ユーザーが承認すると、指定された redirect_uri にユーザーをリダイレクトし、URLに認可コード (code) と state (もし指定されていれば) が追加されます。  
例: `https://www.example.com/callback?code=abcdef&state=XYZ`


---

## アクセストークン取得 (/get_token - Initial Exchange)

**認可コードをアクセストークンと交換するために使用されるエンドポイント**

### URL:

- `https://api.login.yahoo.com/oauth2/get_token`
- HTTPメソッド: POST


### 必須リクエストパラメーター:

- `client_id`: あなたのConsumer Key。
- `client_secret`: あなたのConsumer Secret (アプリケーションの秘密鍵)。
- `redirect_uri`: 認証後にYahooがユーザーをリダイレクトするURL。oob も指定可能です。
- `code`: /request_auth からリダイレクトで受け取った認可コード。
- `grant_type`: authorization_code である必要があります。

### 正常時のレスポンス (JSON形式):

- `access_token`: Yahoo! APIにアクセスするためのトークン（有効期限は約1時間）。
- `token_type`: トークンのタイプ（通常は bearer）。
- `expires_in`: access_token の有効期限（秒）。
- `refresh_token`: access_token の有効期限が切れた際に新しいトークンを取得するためのトークン。
- `xoauth_yahoo_guid`: Yahoo!ユーザーのグローバルで一意なID。これがユーザー識別子として機能します。


---

## アクセストークン取得 (/get_token - Refresh Token Exchange)
**refresh_token を使用して、新しい access_token を取得するために使用されるエンドポイント**

### URL:
- `https://api.login.yahoo.com/oauth2/get_token`
- HTTPメソッド: POST

### 必須リクエストパラメーター:

- `client_id`: あなたのConsumer Key。
- `client_secret`: あなたのConsumer Secret。
- `redirect_uri`: 認証後にYahooがユーザーをリダイレクトするURL。oob も指定可能です。
- `refresh_token`: 初回の /get_token 呼び出しで取得したリフレッシュトークン。
- `grant_type`: refresh_token である必要があります。


### 正常時のレスポンス (JSON形式):

- `access_token`: 新しいYahoo! APIにアクセスするためのトークン。
- `token_type`: トークンのタイプ。
- `expires_in`: 新しい access_token の有効期限（秒）。
- `refresh_token`: 更新された（または同じ）リフレッシュトークン。
- `xoauth_yahoo_guid`: ユーザーのグローバルで一意なID。


---

# 参考資料まとめ

- サーバーサイドアプリの認可コードフロー:
  - [`https://developer.yahoo.com/oauth2/guide/flows_authcode/#refresh-token-label`](https://developer.yahoo.com/oauth2/guide/flows_authcode/#refresh-token-label)

**備考**
- このドキュメントは、主にトークンとリフレッシュフローに焦点を当てているため、ユーザー情報取得（User Info）のための明確な独立したエンドポイントの詳細は記載されていません。
- Yahoo!のユーザー情報は、取得したaccess_tokenを使ってYahoo!のProfile APIなどのGraph APIライクなエンドポイントを呼び出すことで取得するのが一般的です。
- xoauth_yahoo_guid がユーザーを一意に識別するIDとなります。


### [ ⏎ 戻る](../index.md)