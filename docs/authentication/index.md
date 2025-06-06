# Authentication Knowledge Base Index

本リポジトリは、OAuth 2.0、OpenID Connect（OIDC）、JWT といった現代の Web 認証・認可技術を体系的に整理し、実装者が迷わず参照できる知識ベースを提供します。  
最終的な目的は、外部認証プロバイダ（Google、Apple、Yahoo! JAPAN、Alipay など）でログインしたユーザーの情報を、安全かつ確実に取得・検証することです。

---

## 1. 構成概要

1. **OAuth（認可フロー）**
    - プロバイダ別の仕様解説と共通フロー図
2. **OpenID Connect（認証補完）**
    - OIDC の役割と利用方法
3. **JWT（トークン構造）**
    - JSON Web Token の生成・署名・検証
4. **技術比較・実装ガイド**
    - 各方式の選定基準、ユーザー情報取得手法
5. **UserInfo（プロフィール取得）**
    - ログイン後に取得可能なユーザーデータと API
6. **Auth Flow Examples（擬似実装コード）**
    - 実際のリクエスト例と処理手順

---

## 2. 目次

### 2.1 OAuth（認可フロー）

- [`oauth/common-flow.mmd`](oauth/common-flow.md)  
  共通の OAuth 2.0 フロー図（マーメイド記法）

- プロバイダごとの詳細
    - [`oauth/google.md`](./oauth/google.md)  
      Google OAuth 2.0 + OIDC の仕様と実装ポイント
    - [`oauth/apple.md`](./oauth/apple.md)  
      Sign in with Apple のフロー、トークン制約
    - [`oauth/yahoo.md`](./oauth/yahoo.md)  
      Yahoo! JAPAN OAuth のスコープ・制限事項
    - [`oauth/alipay.md`](./oauth/alipay.md)  
      Alipay 中国向け OAuth の特徴

### 2.2 OpenID Connect

- [`openid-connect.md`](./openid-connect.md)  
  OIDC の概要、ID トークンの活用方法

### 2.3 JWT（JSON Web Token）

- [`jwt.md`](./jwt.md)  
  トークンの構造、署名検証、セキュリティ上の留意点

### 2.4 技術比較・実装ガイド

- [`comparison.md`](./comparison.md)  
  各方式・各プロバイダの特徴と選定基準
- [`login-user-data.md`](./login-user-data.md)  
  ログイン後に取得可能なユーザー情報一覧と手順

### 2.5 UserInfo（プロフィール取得）

- [`user-info/README.md`](./user-info/README.md)  
  ディレクトリ構成と本セクションの目的
- プロバイダ別取得方法
    - [`user-info/google.md`](./user-info/google.md)  
      ID トークン／`/userinfo` API の使い分け
    - [`user-info/apple.md`](./user-info/apple.md)  
      Apple ID トークンから得られる情報と制限
    - [`user-info/yahoo.md`](./user-info/yahoo.md)  
      Yahoo! JAPAN のプロフィール API 仕様
    - [`user-info/alipay.md`](./user-info/alipay.md)  
      Alipay OpenAPI によるユーザー情報取得
- [`user-info/comparison.md`](./user-info/comparison.md)  
  各社の取得項目と方法の比較表

### 2.6 Auth Flow Examples（擬似実装コード）

- 言語別サンプル
    - [`auth-flow-examples/google.ts`](./auth-flow-examples/google.ts)  
      Google ログイン処理の TypeScript サンプル
    - [`auth-flow-examples/apple.php`](./auth-flow-examples/apple.php)  
      PHP での Sign in with Apple 実装例
    - [`auth-flow-examples/yahoo.py`](./auth-flow-examples/yahoo.py)  
      Python による Yahoo! JAPAN OAuth フロー
    - [`auth-flow-examples/alipay.rb`](./auth-flow-examples/alipay.rb)  
      Ruby での Alipay OAuth サンプル

---

## 3. 推奨学習順序

1. **共通フロー図**（`oauth/common-flow.mmd`）で OAuth の全体像を理解
2. **OIDC** と **JWT**（`openid-connect.md`、`jwt.md`）で基礎技術を把握
3. **プロバイダ別仕様**（`oauth/` 配下）を確認
4. **ユーザー情報取得**（`user-info/`）で実装手順を学ぶ
5. **サンプルコード**（`auth-flow-examples/`）を動かして検証

---

## 4. おわりに

本目次は「安全・確実なユーザー情報取得」を支援する実装ガイドとして機能します。  
各章を順にたどることで、認証・認可の誤解を排し、具体的な実装手順へスムーズに移行できることを目指しています。


---

## 🌐 構成
```text
. 
├── auth-flow-examples        # 各OAuthプロバイダにおける認証・認可フローの擬似コード（実装者向け）
│   ├── alipay.rb             # AlipayのOAuthフロー擬似コード（Ruby）
│   ├── apple.php             # Appleのログイン処理例、JWT署名生成含む（PHP）
│   ├── google.ts             # Googleログイン処理（TypeScript、トークン取得など）
│   └── yahoo.py              # Yahoo! JAPANのOAuth処理例（Python）

├── comparison.md             # 各プロバイダや技術要素（OIDC/JWTなど）の比較と選定指針

├── index.md                  # この知識ベースの目次兼ハブファイル（ナビゲーションの起点）

├── jwt.md                    # JWT（JSON Web Token）の構造、署名、検証方法、注意点など

├── login-user-data.md        # 各プロバイダのOAuthログイン後、取得できるユーザー情報のまとめ

├── oauth                     # 各OAuthプロバイダに関する仕様とフローの解説
│   ├── alipay.md             # AlipayのOAuth認可フローと特殊仕様の解説
│   ├── apple.md              # Apple Sign-Inの仕組み、制約、セキュリティ仕様
│   ├── common-flow.mmd       # OAuth 2.0の共通フローをマーメイド記法で表現（図解）
│   ├── google.md             # GoogleのOAuth 2.0 + OIDC仕様解説
│   └── yahoo.md              # Yahoo! JAPAN OAuthの特徴、スコープ仕様など

├── openid-connect.md         # OpenID Connectの役割、IDトークンとの違い、OAuthとの補完関係

└── user-info                 # 各OAuthログイン後に取得できるユーザー情報とその方法の解説
    ├── alipay.md             # Alipayから取得できるユーザー情報とその取得手順
    ├── apple.md              # AppleのIDトークンに含まれるユーザー情報と注意点
    ├── comparison.md         # 各プロバイダのユーザー情報取得手法・項目の比較表
    ├── google.md             # Googleのuserinfo APIおよびIDトークンに含まれる情報の取得方法
    ├── README.md             # この user-info/ ディレクトリの意図と構成の概要
    └── yahoo.md              # Yahoo! JAPANのユーザー情報取得APIとレスポンス構造

```