[README.md](../../README.md)

## さまざまなシェル操作やコマンドを用途別に整理し、日本語で解説したマニュアル

# 目次

- [シェル操作](./shell-operations.md)
  - シェルの再読み込み・終了方法
  - サブプロセスの制御
  - シェル履歴の管理
  - シェル関数の定義例

- [条件分岐・パイプ・リダイレクト](./branching-pipe-redirect.md)
  - ブランチ条件
  - 標準出力・標準エラーの分離／同時出力

- [ファイル・ディレクトリ操作](./file-dir-operations.md)
  - ファイルのバックアップ・空ファイル化
  - ディレクトリの作成と移動
  - リネーム・拡張子一括変換
  - 特定拡張子以外のファイル削除

- [ファイル検索（find）](./find-usage.md)
  - 更新日時・サイズ・重複検索など
  - パーミッション・所有者条件での検索
  - 空ディレクトリや古いファイルの削除
  - 再帰的な文字列置換（sed と併用例）

- [プロセス管理](./process-management.md)
  - プロセス閲覧 (ps, top)
  - ファイルロック・使用中プロセス (fuser, lsof)
  - プロセス強制終了 (kill)
  - プロセスのカレントディレクトリ取得 (pwdx)

- [ネットワーク関連ツール](./network-tools.md)
  - curl / httpie
  - netcat / nc
  - tcpdump / tcpick / ngrep
  - nmap
  - socat
  - 接続確認／SSLテスト (openssl, gnutls-cli)
  - ホスト名・IP解決 (host, dig)

- [テキスト処理](./text-processing.md)
  - grep
  - awk
  - sed
  - perl

- [システム監視・統計](./system-monitoring.md)
  - vmstat
  - iostat
  - du
  - netstat

- [アーカイブ・バックアップ](./archive-backup.md)
  - tar
  - dump / restore
  - rsync

- [セキュリティ・暗号化](./security-encryption.md)
  - OpenSSL 基本操作
  - GPG 基本操作
  - certbot での証明書取得
  - セキュア消去 (shred, scrub, badblocks, secure-delete)

- [開発支援・その他ツール](./dev-tools.md)
  - git
  - Python 簡易 HTTP サーバー
  - screen / script
  - inotifywait

- [便利なワンライナー・シェルスクリプト例](./shell-one-liners.md)
  - シェル立ち上げ時の初期化 (script, stty, reset)
  - ログイン・ログアウト時にコマンド実行 (trap)
  - ループで数列生成・ファイル監視
  - ファイルサーバー・HTTP サーバー（BusyBox, Netcat, Python など）

- [シェル関数例: ドメイン解決・ASN 取得](./shell-functions-domain-asn.md)
  - DomainResolve（ドメイン→IPを取得）
  - GetASN（IP→ASN情報を取得）

### [ ⏎ 戻る](../learning-journal.md)
