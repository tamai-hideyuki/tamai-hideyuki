# 開発支援・その他ツール

# git

---
- **複数のコミットを1つにSquash（まとめる）**
```text
1. インタラクティブ・リベース開始
git rebase -i HEAD~27
[HEAD~27 は直近27個のコミットを対象にするという意味。必要に応じて数は調整]

2. エディタが開くので、先頭以外を pick → squash または s に変更
pick 073d0dd [update]
squash 911c4d0 [update]
squash c16c5de [update]
squash 157aec8 [update]
...
squash da844a9 [update]

3. コミットメッセージの編集
[すべてのコミットメッセージが出てくるので、1つにまとめてわかりやすく編集]

4. リベース完了後、リモートに強制プッシュ
git push -f origin main
[リモート履歴を書き換えるので、チーム開発中であれば必ず事前相談を]
[必要なら、rebase -iをやる前にブランチを切ってバックアップしておくこともおすすめ]

```
---

- **全てをまとめて1コミットのみの美しい状態にしたいなら**
```bash
# 1. 現在の状態を1コミットに置き換える
git checkout main
git reset $(git commit-tree HEAD^{tree} -m "Profile: initial clean commit") <-(例だよ：)

# 2. GitHubに強制プッシュ
git push -f origin main

```

---

- **1つのコミットを常に「上書き」する方法**
```bash
git add .
git commit --amend --no-edit
```
```text
--amend：直前のコミットに上書き

--no-edit：コミットメッセージを変更せずそのまま
```
- リモートにも上書き反映（強制 push）
```bash
git push -f origin main
```
---
- **コミットメッセージを編集**
--amend でメッセージを編集モードで修正
```bash
git commit --amend
```
```text
エディタが開いてすでにあるcommitメッセージが表示されるので任意のメッセージに編集して保存して終了

GitHub 上のコミットも更新するには「強制 push」も忘れずに行うこと。
git push -f origin main
```

---
- **コミットログを見やすく表示（グラフ付き）**
```bash
git log --oneline --decorate --graph --all
```
```text
--oneline: 1 行要約表示（コミット SHA + メッセージ先頭）。

--decorate: ブランチ・タグ名などの装飾。

--graph: ASCII アートのツリー構造。

--all: すべての参照（ローカルブランチ、リモートブランチ、タグ）を表示。
```
---
- **カスタムフォーマットでグラフ付き表示**
```bash
git log --graph \
  --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' \
  --abbrev-commit
```
```text
%Cred%h%Creset: 赤い短縮コミットハッシュ。

%C(yellow)%d%Creset: 黄色で参照名（ブランチ/タグ）表示。

%s: コミットメッセージタイトル。

%Cgreen(%cr): 相対日付（例: 2 days ago）を緑字で。

%C(bold blue)<%an>%Creset: 著者名を太字青字で括弧付き表示。

--abbrev-commit: コミットハッシュを短縮形で表示。
```


---

## Python 簡易 HTTP サーバー

---
- **Python 3.x でカレントディレクトリを HTTP サーバーとして配信**
```bash
python3 -m http.server 8000 --bind 127.0.0.1
```
```text
8000 ポートで待ち受け。

--bind 127.0.0.1 でローカルホスト限定。
```
---
- **Python 2.x の場合**
```bash
python -m SimpleHTTPServer 8000
```

---

- **SSL 対応の簡易サーバー（Python 3.x）**
```bash
from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

httpd = HTTPServer(('localhost', 4443), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
                                keyfile="path/to/key.pem",
                                certfile="path/to/cert.pem",
                                server_side=True)
httpd.serve_forever()
```
```text
4443 ポートで SSL 版 HTTP サーバーを起動。

keyfile, certfile には秘密鍵・証明書を指定。
```
---
## screen / script

---
- **screen セッションをデタッチ（バックグラウンド化）して実行**
```bash
screen -d -m <command>
```
```text
例: screen -d -m top → top をバックグラウンドで起動。
```

---

- **既存の screen セッションにアタッチ**
```bash
screen -r -d <pid>
```
```text
<pid> は screen -ls で確認できるセッション ID。
```

---

- **端末セッションを録画し、再生**
- 録画開始
```bash
script -t 2>~/session.time -a ~/session.log
```
```text
script は自動的に疑似端末を記録し、

-t 2>~/session.time でタイミング情報を session.time に出力、

-a ~/session.log で実際の出力ログを追記。
```

- 録画終了
>Ctrl+D や exit で script を終了すると録画ファイルが生成される。

- 再生
```text
scriptreplay --timing=session.time session.log
```
---

## inotifywait
- **ディレクトリ内のファイル変更を監視し、変更後に処理を実行**
```bash
while true; do
  inotifywait -r -e MODIFY dir/ && ls dir/
done
```
```text
-r: 再帰的に監視。

-e MODIFY: ファイル変更イベント。

変更があるたびに ls dir/ を実行し、一覧を更新表示。
```

