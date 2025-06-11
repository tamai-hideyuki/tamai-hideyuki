>[Yahoo!デベロッパーネットワーク: Yahoo! JAPAN ID連携に関する全てのドキュメントの起点です。](https://developer.yahoo.co.jp/)<br>
> [Yahoo! ID連携 v2: 認可コードフローを含むY!Connectの仕様に関する詳細。](https://developer.yahoo.co.jp/yconnect/v2/)

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

### 分かりやすく

```mermaid
sequenceDiagram
    participant 君 as 君（ユーザー）
    participant ゲームサイト as ゲームサイト（あなたのWebサイト）
    participant Yahoo as Yahoo! JAPAN（OAuthの許可を出す場所）
    
    君->>ゲームサイト: 1. ゲームサイトにログインしたい！
    ゲームサイト->>君: 2. 「Yahoo! JAPANでログインする？」って聞くよ
    君->>Yahoo: 3. Yahoo! JAPANの画面に行って、「このゲームサイトに名前教えてもいいよ」って許可するよ
    Yahoo->>君: 4. Yahoo! JAPANが「よし！許可の印（しるし）の【認可コード】をあげるね！」って言うよ
    君->>ゲームサイト: 5. その「認可コード」をゲームサイトに渡すよ
    
    ゲームサイト->>Yahoo: 6. ゲームサイトがYahoo! JAPANに「この認可コードで、君の『名前を見る許可証』をちょうだい！」って言うよ（こっそりAPI通信）
    Yahoo->>ゲームサイト: 7. Yahoo! JAPANが「OK！じゃあこれが【名前を見る許可証】だよ」って渡すよ（これもこっそりAPI通信）
    
    ゲームサイト->>ゲームサイト: 8. ゲームサイトが【許可証】を見て、君のID（名前）を確認するよ
    ゲームサイト-->>君: 9. 「ログインできたよ！」って君に教えるよ！
```
