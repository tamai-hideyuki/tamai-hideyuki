>[Sign in with Apple (開発者向け): Sign in with Appleの実装に関する公式ドキュメントの起点です。](https://developer.apple.com/documentation/authenticationservices/implementing_user_authentication_with_sign_in_with_apple)<br>
> [REST API ドキュメント: サーバーサイドでの認可コード交換に関する詳細が含まれます。](https://developer.apple.com/documentation/signinwithapplerestapi)

## OpenID Connect (OIDC) に準拠したサービス

```mermaid
sequenceDiagram
    participant User
    participant ClientApp as Your Web App (Client)
    participant AuthzServer as Authorization Server (Google/Apple/Yahoo! JAPAN)
    
    User->>ClientApp: 1. Access login page
    ClientApp->>User: 2. Redirect to AuthzServer for login/consent
    User->>AuthzServer: 3. Login and grant consent
    AuthzServer->>User: 4. Redirect to ClientApp with Authorization Code
    User->>ClientApp: 5. Browser redirects with Authorization Code in URL
    
    ClientApp->>AuthzServer: 6. Exchange Authorization Code for Tokens (Server-to-Server)
    AuthzServer->>ClientApp: 7. Return Access Token & ID Token (JSON)
    
    ClientApp->>ClientApp: 8. Validate ID Token & Extract User ID (from 'sub' claim)
    ClientApp-->>User: 9. User is logged in!
```

### 分かりやすく(web)


```mermaid
sequenceDiagram
    participant 君 as 君（ユーザー）
    participant あなたのサイトFE as あなたのサイト（フロントエンド）
    participant あなたのサイトBE as あなたのサイト（バックエンド）
    participant AppleAuthServer as Apple認証サーバー

    君->>あなたのサイトFE: 1. あなたのサイトでAppleサインインを選んだ！
    あなたのサイトFE->>君: 2. Apple認証サーバーへリダイレクト（ユーザーはブラウザで移動）
    君->>AppleAuthServer: 3. Appleのログイン画面で、ログインと許可を行う
    AppleAuthServer->>君: 4. 許可の印【認可コード】を持って、あなたのサイトのFEへリダイレクト
    君->>あなたのサイトFE: 5. ブラウザが【認可コード】を持ってあなたのサイトに到着

    あなたのサイトFE->>あなたのサイトBE: 6. 【認可コード】をバックエンドへ渡す
    あなたのサイトBE->>AppleAuthServer: 7. 【認可コード】を渡し、『IDとアクセストークン』をちょうだい！（サーバー間通信）
    AppleAuthServer->>あなたのサイトBE: 8. OK！これが『IDトークン（ユーザーID入り）』と『アクセストークン』だよ！（サーバー間通信）

    あなたのサイトBE->>あなたのサイトBE: 9. 『IDトークン』をしっかり確認して、ユーザーIDを取り出す
    あなたのサイトBE-->>あなたのサイトFE: 10. ログイン成功！とフロントエンドへ通知
    あなたのサイトFE-->>君: 11. 「ログインできたよ！」と君に表示！
```
