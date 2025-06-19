## Gitリベース＆コンフリクト解消

###  想定シナリオ

- ブランチ：feature/frontend-ui
- リベース対象：main
- ゴール：Pull Request を出す前に最新の main に追いつき、履歴を綺麗に整える

### リベース開始
```bash
git checkout feature/frontend-ui

git fetch origin

git rebase origin/main
```

### main に追いつくために、ローカルの作業を最新 main に並び直します。

### コンフリクトが発生した場合

- 状況確認
```bash
git status
```
>例：<br>
both added: apps/frontend/package.json<br>
both added: apps/frontend/package-lock.json

### 各ファイルのコンフリクトを手動で解消

#### **解消の基本ルール**
```text
<<<<<<< HEAD … main 側の内容

=======

>>>>>>> [your branch] … 作業ブランチの内容
```

### 対応方針

| ファイル                             | 解消方針                        |
| -------------------------------- | --------------------------- |
| `package.json`                   | `feature` 側（Next.js 構成）を残す  |
| `package-lock.json`              | `feature` 側を採用してそのまま使う      |
| `tsconfig.json`, `types/todo.ts` | 重複を避けてマージ、または `feature` 側優先 |

### 解消済みファイルをステージング
```bash
git add apps/frontend/package.json

git add apps/frontend/package-lock.json
```

### リベース再開
```bash
git rebase --continue
```

### 完了メッセージを確認
```bash
Successfully rebased and updated refs/heads/feature/frontend-ui.
```

### リモートに強制 push（履歴が書き換わっているため）
```bash
git push --force-with-lease --set-upstream origin feature/frontend-ui
```

**※個人開発だからこそ意味のある、実用性特化のマニュアル**
