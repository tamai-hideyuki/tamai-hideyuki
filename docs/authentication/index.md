# 🔐 Authentication Knowledge Index

各種認証・認可方式に関する仕様、実装、設計思想を体系的に整理しました。

## 📚 目次

### ▶️ OAuth（認可フロー）
- [`OAuth/Google.md`](./OAuth/Google.md)：GoogleのOAuth 2.0とIDトークンの流れ  
  

- [`OAuth/Apple.md`](./OAuth/Apple.md)：AppleのSign in with Apple、JWT署名と制約
  

- [`OAuth/Yahoo.md`](./OAuth/Yahoo.md)：Yahoo Japanのログイン方式の仕様と注意点
  

- [`OAuth/Alipay.md`](./OAuth/Alipay.md)：Alipayの中国圏向けOAuth連携と制限
  

- [`OAuth/common-flow.mmd`](./OAuth/common-flow.mmd)：OAuth 2.0の一般的なフロー（マーメイド記法）

### 🪄 OpenID Connect（認証補完）

- [`OpenIDConnect.md`](./OpenIDConnect.md)：IDトークンによる認証とOAuthの補完関係

### 🧾 JWT（トークンの構造）

- [`JWT.md`](./JWT.md)：アクセストークン／IDトークンの構造・署名・検証・セキュリティ論点

### 🔍 比較・考察

- [`Comparison.md`](./Comparison.md)：各方式の違い・用途別推奨・落とし穴比較

## 🧠 目的と意図

このディレクトリは、以下の目的を持って設計：

1. 各種ログイン連携実装時の**参照知識ベース**として機能すること
2. 認証・認可の技術的誤解を正し、構成判断の拠り所とすること
3. 実務上の落とし穴（Appleの署名、Alipayの特殊仕様など）に事前に気付けるようにすること

---

## 🌐 構成
```text
Authentication/
├── README.md              # 各方式の概要と思想を記述
├── OAuth/
│   ├── Google.md          # Googleのフローや仕様
│   ├── Apple.md           # Apple ID連携の認証フロー
│   ├── Yahoo.md           # Yahoo Japanの特殊仕様
│   ├── Alipay.md          # アリペイ中国圏OAuthの特徴
│   └── common-flow.mmd    # OAuth全体のシーケンス（マーメイド記法）
├── OpenIDConnect.md       # 認証補完としてのOIDC解説
├── JWT.md                 # トークン方式の認証構造
└── Comparison.md          # 各方式の違いと選定基準まとめ

```