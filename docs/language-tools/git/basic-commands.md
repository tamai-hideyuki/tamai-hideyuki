# 基本コマンド

## 初期設定
| コマンド | 挙動 | 補足 |
| --- | --- | --- |
| `git config --global user.name "Your Name"` | ユーザー名を全体設定に保存 | 初回だけでOK |
| `git config --global user.email "you@example.com"` | メールを全体設定に保存 | 初回だけでOK |
| `git config --global core.editor "code --wait"` | コミット編集時のエディタ指定 | VS Code の例 |

## 基本の流れ
| コマンド | 挙動 | 補足 |
| --- | --- | --- |
| `git init` | 既存フォルダをGit管理にする | `.git` を作成 |
| `git clone <url>` | リポジトリを複製する | 初回取得 |
| `git status -sb` | 現在の状態を短く表示 | ブランチ/差分の確認 |
| `git add <path>` | 変更をステージに載せる | 追加/更新に使う |
| `git commit -m "message"` | ステージ済み変更を確定 | 履歴に残る |
| `git push` | リモートへ送信 | 共有用 |
| `git pull` | リモートから取得+マージ | `fetch`+`merge` |

## 状態確認
| コマンド | 挙動 | 補足 |
| --- | --- | --- |
| `git status` | 作業ツリーの状態表示 | 変更/未追跡の確認 |
| `git status -sb` | 短い表示 | ぱっと見重視 |

## 差分
| コマンド | 挙動 | 補足 |
| --- | --- | --- |
| `git diff` | 未ステージの差分表示 | 作業中の差分 |
| `git diff --staged` | ステージ済み差分表示 | コミット前の確認 |
| `git diff <branch>` | 現在ブランチとの差分表示 | 比較用途 |

## 追加・ステージ
| コマンド | 挙動 | 補足 |
| --- | --- | --- |
| `git add <path>` | ステージに載せる | ファイル指定 |
| `git add -p` | 差分を対話的に選ぶ | 細かい調整 |
| `git reset <path>` | ステージから外す | 変更は残る |

## コミット
| コマンド | 挙動 | 補足 |
| --- | --- | --- |
| `git commit -m "message"` | 新しいコミット作成 | 基本操作 |
| `git commit --amend` | 直前コミットを修正 | メッセージ/内容変更 |
| `git commit --amend --no-edit` | メッセージはそのまま修正 | 追記用 |

## 履歴
| コマンド | 挙動 | 補足 |
| --- | --- | --- |
| `git log --oneline --decorate --graph --all` | 履歴を簡潔に表示 | ブランチ状況も見える |
| `git show <hash>` | 指定コミットの詳細 | 差分とメタ情報 |

## ブランチ
| コマンド | 挙動 | 補足 |
| --- | --- | --- |
| `git branch` | ローカルブランチ一覧 | 現在の確認 |
| `git branch -a` | ローカル+リモート一覧 | 全体把握 |
| `git checkout -b <branch>` | 新規ブランチ作成+移動 | 旧式 |
| `git switch -c <branch>` | 新規ブランチ作成+移動 | 推奨 |
| `git switch <branch>` | ブランチ切り替え | 推奨 |
| `git branch -d <branch>` | ブランチ削除 | マージ済みのみ |

## リモート
| コマンド | 挙動 | 補足 |
| --- | --- | --- |
| `git remote -v` | リモート一覧 | URL確認 |
| `git remote add origin <url>` | リモート追加 | 初回設定 |
| `git fetch` | リモートの履歴取得 | マージはしない |
| `git push -u origin <branch>` | 初回pushと追跡設定 | 以降`git push`だけでOK |

## 取り消し
| コマンド | 挙動 | 補足 |
| --- | --- | --- |
| `git restore <path>` | 作業ツリーの変更を破棄 | 変更が消える |
| `git restore --staged <path>` | ステージから外す | 変更は残る |
| `git reset --soft HEAD~1` | 直前コミットだけ取り消し | 変更は残る |

## スタッシュ
| コマンド | 挙動 | 補足 |
| --- | --- | --- |
| `git stash` | 変更を一時退避 | 作業をきれいにする |
| `git stash list` | スタッシュ一覧 | 退避履歴を見る |
| `git stash pop` | 退避内容を戻す | 適用して削除 |

## タグ
| コマンド | 挙動 | 補足 |
| --- | --- | --- |
| `git tag` | タグ一覧 | バージョン確認 |
| `git tag -a v1.0.0 -m "release"` | 注釈付きタグ作成 | リリース用 |
| `git push --tags` | タグをリモートへ送信 | リリース共有 |
