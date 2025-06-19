# 🔐 認証・設定関連

| コマンド                            | 説明                                            |
| ------------------------------- | --------------------------------------------- |
| `gh auth login`                 | GitHub CLI にログインする（OAuthフロー）                  |
| `gh auth logout`                | ログアウト                                         |
| `gh auth status`                | 現在の認証状態を確認                                    |
| `gh auth refresh`               | トークンを再認証                                      |
| `gh config set <key> <value>`   | CLIの設定値を変更（例：git\_protocol）                   |
| `gh config get <key>`           | 設定値を取得                                        |
| `gh alias set <name> <command>` | コマンドの別名を定義（例：`gh alias set co 'pr checkout'`） |

# 📦 リポジトリ管理

| コマンド                   | 説明                      |
| ---------------------- | ----------------------- |
| `gh repo create`       | 新しいリポジトリを作成             |
| `gh repo clone <repo>` | リポジトリを複製（`git clone`相当） |
| `gh repo fork`         | フォークの作成                 |
| `gh repo view`         | リポジトリ情報の表示              |
| `gh repo delete`       | リポジトリの削除（要確認）           |
| `gh repo list`         | 所有または所属リポジトリ一覧表示        |


# 🛠️ Issue関連

| コマンド                        | 説明             |
| --------------------------- | -------------- |
| `gh issue create`           | 新しいIssueを作成    |
| `gh issue list`             | Issueの一覧を表示    |
| `gh issue view <number>`    | 特定のIssueを詳細表示  |
| `gh issue comment <number>` | コメントを追加        |
| `gh issue close <number>`   | Issueを閉じる      |
| `gh issue reopen <number>`  | 閉じたIssueを再オープン |

# 🔀 Pull Request（PR）関連

| コマンド                      | 説明                       |
| ------------------------- | ------------------------ |
| `gh pr create`            | 新しいPRを作成（対話形式）           |
| `gh pr list`              | PR一覧の表示                  |
| `gh pr view [<number>]`   | PRの詳細を見る                 |
| `gh pr checkout <number>` | 指定PRのブランチに切り替え           |
| `gh pr merge <number>`    | PRをマージ（squash／rebase指定可） |
| `gh pr close <number>`    | PRをクローズ                  |
| `gh pr comment <number>`  | PRにコメントする                |
| `gh pr diff`              | 差分表示                     |


# 💬 Discussions（議論）関連

| コマンド                          | 説明             |
| ----------------------------- | -------------- |
| `gh discussion list`          | ディスカッション一覧を表示  |
| `gh discussion view <number>` | 特定ディスカッションを見る  |
| `gh discussion create`        | 新しいディスカッションを開始 |


# 🧪 GitHub Actions（CI/CD）

| コマンド                     | 説明                      |
| ------------------------ | ----------------------- |
| `gh run list`            | ワークフロー実行履歴を表示           |
| `gh run view <run-id>`   | 特定の実行内容を表示              |
| `gh run watch <run-id>`  | 実行状態をリアルタイム監視           |
| `gh run rerun <run-id>`  | 再実行                     |
| `gh workflow list`       | 登録されたワークフロー一覧           |
| `gh workflow run <name>` | ワークフローの手動実行（パラメータ指定も可能） |


# 🏷 リリース・管理系

| コマンド                      | 説明                        |
| ------------------------- | ------------------------- |
| `gh release list`         | リリース一覧                    |
| `gh release create <tag>` | 新しいリリース作成（オプションでアセット添付も可） |
| `gh release delete <tag>` | リリース削除                    |
| `gh release view <tag>`   | リリースの詳細を表示                |

# 👥 組織・ユーザー関連

| コマンド                | 説明                    |
| ------------------- | --------------------- |
| `gh user view`      | 自分のユーザー情報を表示          |
| `gh api <endpoint>` | GitHub APIを直接叩く（上級者用） |
| `gh gist create`    | Gist（コード断片）を作成・共有     |


# 🎓 使用例集

| やりたいこと     | コマンド例                                                                   |
| ---------- | ----------------------------------------------------------------------- |
| 新リポジトリを作る  | `gh repo create my-project --private --source=. --remote=origin --push` |
| PR作成       | `gh pr create --fill`（タイトル・本文を自動補完）                                     |
| Issueを一覧表示 | `gh issue list --label bug --state open`                                |
| CIの状況確認    | `gh run list` → `gh run view 123456789`                                 |
| ログイン状況を確認  | `gh auth status`                                                        |


