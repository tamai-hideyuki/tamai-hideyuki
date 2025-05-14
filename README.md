# Tamai Hideyuki — Repository Snapshot

未経験から開発エンジニアへの道を歩み、**Docker × Laravel × 認証設計 × CLI自動化**を軸に、個人開発を重ねてまいりました。  
この一覧では、私が構築・設計・発表してきたリポジトリ群をジャンル別に紹介します。  
いずれも **実際に動作するプロジェクト**であり、学びと挑戦の軌跡を示しております。

---

## 🧰 技術スタックバッジ

### 🧑‍💻 言語 & スクリプト
![PHP](https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Ruby](https://img.shields.io/badge/Ruby-CC342D?style=for-the-badge&logo=ruby&logoColor=white)
![Java](https://img.shields.io/badge/Java-007396?style=for-the-badge&logo=java&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=c%2b%2b&logoColor=white)
![ShellScript](https://img.shields.io/badge/ShellScript-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)

---

### 🧱 フレームワーク & 認証
![Laravel](https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white)
![Symfony](https://img.shields.io/badge/Symfony-000000?style=for-the-badge&logo=symfony&logoColor=white)
![OAuth2](https://img.shields.io/badge/OAuth2-0066CC?style=for-the-badge)
![Google Authenticator](https://img.shields.io/badge/Google_Auth-4285F4?style=for-the-badge&logo=google)

---

### 🛠 開発支援・自動化・インフラ
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Makefile](https://img.shields.io/badge/Makefile-000000?style=for-the-badge&logo=gnu&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)

---

### 📱 PWA & オフライン技術
![PWA](https://img.shields.io/badge/PWA-5A0FC8?style=for-the-badge&logo=pwa)
![IndexedDB](https://img.shields.io/badge/IndexedDB-blue?style=for-the-badge)
![Service Worker](https://img.shields.io/badge/Service_Worker-black?style=for-the-badge)

---

### 📚 その他
![Markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown)
![REST API](https://img.shields.io/badge/REST%20API-009688?style=for-the-badge)
![Wireshark](https://img.shields.io/badge/Wireshark-1679A7?style=for-the-badge&logo=wireshark)
---

## 🔐 認証・認可（Authentication / Authorization）

| リポジトリ名 | 説明 |
|--------------|------|
| [two-factor-auth](https://github.com/tamai-hideyuki/two-factor-auth.git) | LaravelでGoogle Authenticatorと連携した2段階認証（2FA）を実装したプロジェクト |

---
## 🛠 CLI & Automation

| リポジトリ名 | 説明 |
|--------------|------|
| [devsetup](https://github.com/tamai-hideyuki/devsetup.git) | Dockerベースの**ノーコード開発起点自動生成ツール**。Laravel+Breeze+Google OAuth対応の認証基盤を対話CLIで即座に構築。Symfonyモジュールも搭載し、インフラ構築から認証設計までをローコードで完結。**「属人化ゼロ」ではなく、「構築そのものの省略」を目指す**開発支援ツール。 |
| [git-rename](https://github.com/tamai-hideyuki/git-rename.git) | 複数プロジェクトの Git リモートURL を一括更新する Bash製ユーティリティ。dry-run対応、再帰処理でフォルダを自動スキャンし差分を明示。 |

---

## 📊 スクリプト & 分析

| リポジトリ名 | 説明 |
|--------------|------|
| [TrendSeer](https://github.com/tamai-hideyuki/TrendSeer.git) | TradingView 向け Pineスクリプト。テクニカル分析ロジックを実装 |


---

## 📚 LT資料

| リポジトリ名 | 説明 |
|--------------|------|
| [lt-ddd](https://github.com/tamai-hideyuki/lt-ddd.git) | DDD再入門スライド。個人開発にDDDを取り入れた実践例 |
| [lt-oauth-reintro](https://github.com/tamai-hideyuki/lt-oauth-reintro.git) | Symfony×OAuthの再入門資料（スライド＋コード＋図解） |

---

## 🌐 Web & PWA

| リポジトリ名 | 説明                                  |
|--------------|-------------------------------------|
| [main](https://github.com/tamai-hideyuki/main.git) | オフライン⇔オンライン自動切替・IndexedDB連携のPWA実験環境 |

---

## 🎮 ゲーム & アルゴリズム

| リポジトリ名 | 説明 |
|--------------|------|
| [sudoku-generator](https://github.com/tamai-hideyuki/sudoku-generator.git) | 数独を6言語（PHP, JS, Ruby, etc）で自動生成するアルゴリズム実装 |
| [knapsack-project](https://github.com/tamai-hideyuki/knapsack-project.git) | Shellスクリプトによるナップサック問題の実装 |

---

## ⚙️ 学習用 & 設計検証

| リポジトリ名 | 説明                                      |
|--------------|-----------------------------------------|
| [docker-symfony-lite](https://github.com/tamai-hideyuki/docker-symfony-lite.git) | Symfony理解のために構築した最小Docker構成             |
| [ddd-ec-project](https://github.com/tamai-hideyuki/ddd-ec-project.git) | DDD＋クリーンアーキテクチャを適用したECサイトプロトタイプ（現在構築中） |
---

## 補足

- **設計志向：** DDD・クリーンアーキテクチャ・レイヤード設計
- **重点領域：** 認証（2FA・OAuth）／Docker活用による再現性ある環境構築／PWA・IndexedDB
- **開発スタイル：** Issue駆動／Gitフロー運用／Makefile・CLI自動化による効率化

---


> 本ページは継続的にアップデートされます。
