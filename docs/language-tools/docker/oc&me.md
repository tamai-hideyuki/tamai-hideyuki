**RFC-Chronicle Docker: Orphan Container & Mount Error 解消マニュアル**

---

## 1. エラー概要

```
Error response from daemon: failed to create task for container: ...
not a directory: unknown: Are you trying to mount a directory onto a file (or vice-versa)?
WARN Found orphan containers ... for this project.
```

* **マウントエラー**: `host path` と `container path` の型不一致（ファイル vs ディレクトリ）
* **Orphan 警告**: 別プロジェクト（recrui-track）のコンテナが同一 Compose プロジェクト名で起動され混在

---

## 2. 問題点

1. **`volumes:` のホストパス不一致**

    * Compose 設定で `./nginx/default.conf` をマウントしようとしているが、実際のファイルは `docker/nginx/default.conf` にある

2. **Compose プロジェクト名の衝突**

    * デフォルトでプロジェクト名がフォルダ名 (`docker`) になるため、別リポジトリのコンテナが同一名前空間に誤検出される

---

## 3. 前提ディレクトリ構成

```
Projects/rfc-chronicle/
  ├ docker-compose.yml
  ├ docker/
  │  ├ nginx/
  │  │   └ default.conf
  │  ├ Dockerfile.backend
  │  └ Dockerfile.frontend
  └ .env                ← （これから作成）
```

---

## 4. 解決手順（時系列）

### 4.1 .env 作成 & プロジェクト名固定

```bash
# rfc-chronicle/docker フォルダへ移動
cd ~/Projects/rfc-chronicle/docker

# .env を新規作成
cat << 'EOF' > .env
COMPOSE_PROJECT_NAME=rfcchron
EOF
```

### 4.2 Compose 設定の修正

* **docker-compose.yml**: `volumes:` のパスを修正

```diff
 services:
   nginx:
     image: nginx:stable-alpine
     volumes:
-      - ./nginx/default.conf:/etc/nginx/conf.d/default.conf:ro
+      - ./docker/nginx/default.conf:/etc/nginx/conf.d/default.conf:ro
```

### 4.3 古いコンテナ・ネットワークのクリーンアップ

```bash
# 環境変数読み込み
export $(grep -v '^#' .env)

# 現在の rfcchron Compose を停止、orphan を削除
docker compose down --remove-orphans

# 不要リソースを一掃
docker system prune --volumes --force
```

### 4.4 コンテナ再起動

```bash
# 改めて起動
docker compose up -d
```

### 4.5 Docker Desktop 設定確認

1. Docker Desktop → **View configurations** を開く
2. `rfcchron` プロジェクトのみ表示されているか確認
3. 他リポジトリの設定が混在していればチェックを外す or 削除

---

## 5. 動作確認

```bash
# 正常に起動したコンテナ一覧
docker ps --filter "name=rfcchron"
# nginx ログで mount エラーが無いかチェック
docker logs rfcchron_nginx_1
```
