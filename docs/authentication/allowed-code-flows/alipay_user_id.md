>[Alipay+ Docs: Alipay+のサービス統合に関する主要なドキュメントポータルです。認証や決済フローについて記載されています。](https://docs.alipayplus.com/)<br>
>[Antom Docs: (Alipay+の親会社であるAnt Groupのドキュメントで、より深い技術情報を含むことがあります)](https://docs.antom.com/)


```mermaid
sequenceDiagram
    participant User
    participant ClientApp as Your Web App (Client)
    participant AlipayAuth as Alipay Authorization Server
    participant AlipayAPI as Alipay Open API Gateway
    
    User->>ClientApp: 1. Access login page
    ClientApp->>User: 2. Redirect to AlipayAuth for login/consent
    User->>AlipayAuth: 3. Login and grant consent
    AlipayAuth->>User: 4. Redirect to ClientApp with Authorization Code
    User->>ClientApp: 5. Browser redirects with Authorization Code in URL (e.g., 'auth_code')
    
    ClientApp->>AlipayAuth: 6. Exchange Authorization Code for Access Token (Server-to-Server)
    AlipayAuth->>ClientApp: 7. Return Access Token (JSON)
    
    ClientApp->>AlipayAPI: 8. Call User Info API with Access Token (e.g., alipay.user.userinfo.share)
    AlipayAPI->>ClientApp: 9. Return User Profile (JSON with 'user_id' field)
    
    ClientApp->>ClientApp: 10. Extract User ID (from 'user_id' field)
    ClientApp-->>User: 11. User is logged in!
```

### 分かりやすく

```mermaid
sequenceDiagram
    participant 君 as 君（ユーザー）
    participant ゲームサイト as ゲームサイト（あなたのWebサイト）
    participant Alipay as Alipay（ログインの許可を出す場所）
    participant AlipayAPI as Alipayの質問コーナー（IDを教えてくれる場所）
    
    君->>ゲームサイト: 1. ゲームサイトにログインしたい！
    ゲームサイト->>君: 2. 「Alipayでログインする？」って聞くよ
    君->>Alipay: 3. Alipayの画面に行って、「このゲームサイトに名前見てもいいよ」って許可するよ
    Alipay->>君: 4. Alipayが「よし！許可の印（しるし）の【認可コード】をあげるね！」って言うよ
    君->>ゲームサイト: 5. その「認可コード」をゲームサイトに渡すよ
    
    ゲームサイト->>Alipay: 6. ゲームサイトがAlipayに「この認可コードで、君の『何かを見れる許可証』をちょうだい！」って言うよ（こっそりAPI通信）
    Alipay->>ゲームサイト: 7. Alipayが「OK！じゃあこれが【何かを見れる許可証】だよ」って渡すよ（これもこっそりAPI通信。でも**IDはまだ渡さないよ**）
    
    ゲームサイト->>AlipayAPI: 8. ゲームサイトが【許可証】を使って、Alipayの質問コーナーに「この許可証の人のIDって何番？」って聞くよ（こっそりAPI通信）
    AlipayAPI->>ゲームサイト: 9. 質問コーナーが「その人のIDは【〇〇番】だよ」って教えてくれるよ（これもこっそりAPI通信）
    
    ゲームサイト->>ゲームサイト: 10. ゲームサイトが教えてもらったID（番号）を確認するよ
    ゲームサイト-->>君: 11. 「ログインできたよ！」って君に教えるよ！
```
