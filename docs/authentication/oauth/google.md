### [ ⏎ 戻る](../index.md)

# Google OAuth 2.0 認証フロー

---

## 認可エンドポイント (Authorization Endpoint)

### URL:
- `https://accounts.google.com/o/oauth2/v2/auth`

### 主な必須クエリパラメーター:

- `client_id`: あなたのアプリケーションのクライアント ID。
- `redirect_uri`: 認可コードが送信されるリダイレクト URI。Google API Console で登録したものと完全に一致する必要あり。
- `response_type`: 取得したいレスポンスのタイプ。認可コードフローでは code を指定。OpenID Connect の場合は code と id_token を組み合わせることもある。
- `scope`: アクセスを要求する情報の範囲を示す文字列。スペース区切りで複数指定できる。

### 正常時のレスポンス:

- `code`: 一時的な認可コード。アクセストークンと交換するために使用。
- `state`: リクエスト時に送信した state パラメーターと同じ値。

---

## トークンエンドポイント (Token Endpoint):

### URL:
- `https://oauth2.googleapis.com/token`

### 主な必須クエリパラメーター(POST リクエストのボディに含める):
- `code`: 認可エンドポイントから取得した認可コード。
- `client_id`: あなたのアプリケーションのクライアント ID。
- `client_secret`: あなたのアプリケーションのクライアントシークレット (ウェブサーバーアプリケーションなど、サーバーサイドで実行されるアプリケーションの場合に必要となってくる)。
- `redirect_uri`: 認可コード取得時と同じリダイレクト URI。
- `grant_type`: authorization_code (認可コードフローの場合)。

### 正常時のレスポンス:
**JSON 形式で以下のデータが返却**
- `access_token`: Google API にアクセスするためのアクセストークン。有効期限あり。
- `expires_in`: アクセストークンの有効期限（秒数）。
- `id_token`: ユーザーの認証情報を含む JSON Web Token (JWT)。sub (ユーザーの一意な識別子)、email、name などの情報が含まれる。OpenID Connect を使用する場合に返される。
- `scope`: 許可されたスコープ。
- `token_type`: 通常は Bearer。
- `refresh_token`: (オフラインアクセスが許可されている場合) アクセストークンの有効期限が切れた際に新しいアクセストークンを取得するためのトークン。


---

## Userinfo エンドポイント (Userinfo Endpoint):

### URL:
- `https://openidconnect.googleapis.com/v1/userinfo`

- より古いエンドポイントも存在するみたい。 `https://www.googleapis.com/oauth2/v3/userinfo` や `https://www.googleapis.com/oauth2/v1/userinfo` 。しかし、OpenID Connect に準拠した上記 URL の使用が推奨されているようです。

### 主な必須クエリパラメーター:

- このエンドポイントへのリクエストは、通常、アクセストークンを Authorization ヘッダーに Bearer トークンとして含めることで行われる。
- クエリパラメーターは通常必要ない。
- HTTP ヘッダー: Authorization: Bearer YOUR_ACCESS_TOKEN

### 正常時のレスポンス:
**JSON 形式でユーザー情報を返却。返される情報の種類は、トークン取得時に要求した scope によって異なる。**

- `sub`: ユーザーの一意な識別子 (ID トークンの sub クレームと同じ値)。
- `name`: ユーザーのフルネーム。
- `given_name`: ユーザーの名。
- `family_name`: ユーザーの姓。
- `picture`: ユーザーのプロフィール画像の URL。
- `email`: ユーザーのメールアドレス。
- `email_verified`: メールアドレスが確認済みかどうか (boolean)。
- `locale`: ユーザーの言語/地域。
- `hd`: (Hosted Domain) Google Workspace (旧 G Suite) ドメインユーザーの場合、そのドメイン名。 

---

## 参考資料

- Google Identity の認証に関するドキュメント: 
  - [`https://developers.google.com/identity/protocols/oauth2?hl=ja`](https://developers.google.com/identity/protocols/oauth2?hl=ja)  
  

- OpenID Connectの中核機能 & エンドユーザーに関する情報を伝達するためのクレームの使用を定義し、OpenID Connectの使用におけるセキュリティとプライバシーに関する考慮事項についてを説明した仕様書: 
  - [`https://openid.net/specs/openid-connect-core-1_0.html`](https://openid.net/specs/openid-connect-core-1_0.html)

### [ ⏎ 戻る](../index.md)
