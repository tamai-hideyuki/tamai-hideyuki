# テキスト処理

# 【grep】

---

- **現在居るディレクトリは以下全てに対して''任意の文字'を検索**
```bash
grep -R -n '任意の文字' .
```
---

- **カレントディレクトリ以下を再帰的に検索（行番号付き、バイナリ除外）**
```bash
grep -RnisI "pattern" *
```
- -R: 再帰的。

- -n: 行番号表示。

- -i: 大文字小文字を無視。

- -s: エラーメッセージを抑制（ファイルがない警告など）。

- -I: バイナリファイルを無視。

---

- **複数パターンを同時に検索（OR 条件）**
```bash
grep -E '(INFO|WARN)' filename 
```

- -E: 拡張正規表現を有効化。

---

- **特定パターンを除外して表示**
```bash
grep -vE '(language-tools|critical|warning)' filename
```

- -vE: 拡張正規表現を用い、該当行を除外。

---

- **コメント（#）と空行を除いて表示**
```bash
grep -v '^[[:space:]]*#' filename | grep -v '^$' 
```

- 行頭の空白＋# を除外。 
- 空行も除去。

---

- **ダッシュ・ハイフン付き文字列を検索**
```bash
grep -e -- filename 
```

- -e --: -- を検索したい場合は -e --。 
- 例: grep "\-\-" filename で "--" を検索。

---

- **空行を取り除き、結果を別ファイルに保存**
```bash
grep . filename > newfile 
```
- . は「任意の 1 文字」にマッチするため、空行行 (^$) は除外できる。

---


### 使用例

- **MEMOS_ROOT 定義を探す**
```bash
grep -R "MEMOS_ROOT" -n ./apps/backend
```

- **mkdir を使っている箇所を探す**
```bash
grep -R "mkdir" -n ./apps/backend
```


---

# 【awk】

- **「foo」を含む行を表示**
```bash
awk '/foo/' filename
```
---

- **「foo」を含まない行を表示（grep -v foo 相当）**
```bash
awk '!/foo/' filename 
```

---

- **マッチした行の行番号付きで表示（grep -n foo 相当）**
```bash
awk '/foo/{print FNR, $0}' filename 
```

---

- **最後の列を表示**
```bash
awk '{print $NF}' filename 
```
- $NF は最終列を示す。

---

- **80 文字より長い行を行番号付きで表示**
```bash
awk 'length($0) > 80 {print FNR, $0}' filename
```

---

- **80 文字未満の行のみ表示**
```bash
awk 'length < 80' filename 
```

---

- **二行ごとに空行（ダブル改行）を挿入**
```bash
awk '1; {print ""}' filename
```
- 1; {print ""} は「常に行を出力したあと空行を挿入」。

---

- **行番号を付与して表示**
```bash
awk '{print FNR "\t" $0}' filename 
```
- タブ区切りで行番号と行内容。

---

- **空白行を除外する（簡易版）**
```bash
awk 'NF > 0' filename
```
- 
- NF はフィールド数を表し、NF > 0 は「空行でない行」を意味。

---

- **重複連続行を除去**
```bash
awk 'a != $0 {print; a = $0}' filename 
```
- 直前行 a と現在行 $0 を比較し、異なる場合のみ出力。

---

- **ファイル内で重複行を除去（ソート不要版）**
```bash
awk '!x[$0]++' filename
```
- 各行をキーに連想配列 x を使って、一度も出現していない行だけを出力。

---

- **複数列を除外して表示**
```bash
awk '{$1 = $3 = ""; print}' filename 
```
- $1 と $3 を空文字に置き換えて全行を表示（他の列は残る）。

---

- **検索行マッチ後、次の 5 行も表示**
```bash
awk '/foo/{i = 5+1;} {if(i){i--; print;}}' filename
```
- マッチした行からカウンタ i = 6（現在行＋次 5 行）。
- i > 0 の間、行を全て表示しつつ i--。

---

- **特定パターン行から終了パターン行までをまとめて表示**
```bash
awk '/server {/,/}/' filename
```
- /server {/ 行から /}/ 行までをすべて出力。

---

- **複数列を整形して表示**
```bash
awk -F' ' '{print "ip:\t" $2 "\nport:\t" $3}' filename
```
- -F' ' で区切り文字を空白に指定し、第2列を ip:, 第3列を port: としてラベル付きで表示。

---

- **行末のトレーリング空白（タブ・スペース）を削除**
```bash
awk '{sub(/[ \t]*$/, ""); print}' filename
```

---

- **行頭のリーディング空白（タブ・スペース）を削除**
```bash
awk '{sub(/^[ \t]+/, ""); print}' filename
```

- **Apache アクセスログの過去 1 時間分を取得**
```bash
awk '/'$(date -d "1 hour ago" "+%d/%b/%Y:%H:%M")'/,/'$(date "+%d/%b/%Y:%H:%M")'/ {print $0}' /var/log/httpd/access_log
```
- date -d "1 hour ago" "+%d/%b/%Y:%H:%M" と date "+%d/%b/%Y:%H:%M" で範囲を動的に指定。

---

# 【sed】

- **特定の行を表示**
```bash
sed -n 10p /path/to/file
```
- -n: 通常はパターン空間を出力しない。

- 10p: 10 行目だけ表示。

---

- **特定行を削除**
```bash
sed -i 10d /path/to/file
```
- ファイルを上書き (-i) で 10 行目を削除。

- BSD 系（macOS など）では sed -i '' 10d /path/to/file のように空文字を指定。

---
- **行範囲を削除**
```bash
sed -i '<start>,<end>d' filename
```
- <start>～<end> の行を全て削除。

---

- **改行文字をスペースに一括置換**
```bash
sed -e ':a' -e 'N' -e '$!ba' -e 's/\n/ /g' /path/to/file
```
- :a: ラベル a を定義。

- N: 次の行をパターン空間に追加。

- $!ba: 最終行でなければ :a に戻る → 全行を一つのパターン空間にまとめる。

- s/\n/ /g: 改行をすべてスペースに置換。

---

- **「start」を含む行から次の 4 行まで削除**
```bash
sed '/start/,+4d' /path/to/file
```
- /start/,+4 でマッチ行およびその後 4 行を削除。

---


# 【perl】

- **インプレース置換（(in place) で直接編集）**
```bash
perl -i -pe 's/SEARCH/REPLACE/g' filename
```
- -i: 直接ファイルを更新。

- -p: 1 行ずつ読み込んで自動出力。

- -e: ワンライナー式指定。

---
- **複数ファイル (*.conf) を編集し、バックアップを .orig で残す**
```bash
perl -p -i.orig -e 's/\bfoo\b/bar/g' *.conf
```
- 元ファイルを filename.conf.orig として保存し、foo → bar 置換。

---
- **最初の 20 行だけを各ファイルから出力**
```bash
perl -pe 'exit if $. > 20' *.conf
```
- $. は現在行番号。

- 20 行以上になったら exit でループ終了。

---

- **10行目から20行目までを表示**
```bash
perl -ne 'print if 10 .. 20' filename
```
- .. は範囲演算子。行番号 10 から 20 までを表示。

---

- **最初の 10 行を除去（バックアップ付き）**
```bash
perl -i.orig -ne 'print unless 1 .. 10' filename
```
- unless 1 .. 10 で 1～10 行目をスキップ。

- バックアップは filename.orig。

---

- **“foo” ～ “bar” の間をすべて除去**
```bash
perl -i.orig -ne 'print unless /^foo$/ .. /^bar$/' filename
```
- ^foo$ 行から ^bar$ 行までのブロックをすべて除去。

- バックアップは filename.orig。

---

- **複数連続する空行を 1 行にまとめる**
```bash
perl -p -i -00pe0 filename
```
- -00 はパラグラフモード。

- 連続する空行を 1 行に置き換え。

---

- **タブをスペース 2 つに置換**
```bash
perl -p -i -e 's/\t/  /g' filename
```
---
