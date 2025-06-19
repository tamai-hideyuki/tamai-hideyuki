# シェル操作

---

## 【シェルの再読み込み・終了方法】

---

- **シェルの再読み込み（環境変数・プロファイルを再読込）**
```bash
exec $SHELL -l
```
- exec で現在のプロセスを置き換え、$SHELL -l（ログインシェル起動）を実行。
- 環境変数や .bashrc / .profile の変更を反映させたいときに便利。
---

- **シェルを閉じるが、バックグラウンドのサブプロセスはキルしない**
```bash
disown -a && exit
```
- disown -a：現在のシェルが管理するジョブをすべて親シェルから切り離す
- その後 exit でシェルを終了しても、バックグラウンドで走っているジョブは継続

---
- **シェルを終了するが、ヒストリーファイルを保存せずに終了**
```bash
kill -9 $$
```
- $$ は現在のシェルの PID を表す
- kill -9 で強制終了するため、通常のシェル終了処理（履歴書き込みなど）をスキップ
- 注意: プロセスがすべて強制終了されるので、作業中のジョブや剥離できていないプロセスも全滅する

---
- **環境変数を消してヒストリーを残さずに終了**
```bash
unset HISTFILE && exit 
```
- unset HISTFILE でシェルが履歴を書き込むファイルを未定義にする。
- そのまま exit すると、履歴ファイルへの書き込みが行われずに終了する。

---

## 【サブプロセスの制御】

---
- **シェルを抜ける際に子プロセスを終了させる（ログアウト後に強制的に SSH プロセスを kill など）**
```bash
cat > /etc/profile << __EOF__
_after_logout() {
  username=$(whoami)
  for _pid in $(ps afx | grep sshd | grep "$username" | awk '{print $1}') ; do
    kill -9 $_pid
  done
}
trap _after_logout EXIT
__EOF__ 
```
- ログアウト時 (EXIT トラップ) に _after_logout 関数を呼び出す設定を /etc/profile に書き込む
- 指定ユーザー (whoami) の sshd プロセスを検索し、強制終了
- SSH 接続切断後に特定プロセスを自動的に殺したい場合などに使う

---

## 【シェル履歴の管理】

---

- **頻出コマンドを一覧表示する**
```bash
history | \
awk '{CMD[$2]++;count++;} END {
    for (a in CMD) 
        print CMD[a] " " CMD[a]/count*100 "% " a;
}' | \
grep -v "./" | \
column -c3 -s " " -t | \
sort -nr | nl | head -n 20
```

1. history で履歴を取得。

2. awk でコマンド文字列ごとに出現数 (CMD[$2]++) をカウントし、全履歴数を count に保持。

3. 最終出力時に「使用回数, 全体に占める割合, コマンド名」を表示。

4. grep -v "./" で ./ 付き（ローカル実行）コマンドを除外。

5. column で揃え、sort -nr で回数降順、nl で行番号付き、head -n 20 で上位20件を表示。

---

- **bash ヒストリーから機密情報を取り除く（Sterilize）関数例**

```bash
function sterile() {
  history | awk '$2 != "history" { $1=""; print $0 }' | 
  egrep -vi "\
  curl\b+.*(-E|--cert)\b+.*\b*|\
  curl\b+.*--pass\b+.*\b*|\
  curl\b+.*(-U|--proxy-user).*:.*\b*|\
  curl\b+.*(-u|--user).*:.*\b*|\
  .*(-H|--header).*(token|auth.*)\b+.*|\
  wget\b+.*--.*password\b+.*\b*|\
  http.?://.+:.+@.*" > $HOME/histbuff
  history -r $HOME/histbuff
}
export PROMPT_COMMAND="sterile"
```

- sterile 関数は、history の出力から機密情報が含まれがちなコマンドを正規表現でフィルタリングし、履歴を一旦 $HOME/histbuff に保存後、再読込み (history -r) するもの。

- PROMPT_COMMAND に登録すると、各プロンプト表示時に自動で実行され、直前のコマンドヒストリーを「クリーニング」します。

- 例: curl -u user:pass ...、wget --password=...、HTTPヘッダーにトークンを含むコマンド、URL に user:pass@ が含まれるコマンドなどをヒストリーから除外。

---

## 【シェル関数の定義例】

---

- **ディレクトリを作成して同時にそのディレクトリに移動**
```bash
mkd() { mkdir -p "$@" && cd "$@"; } 
```
- mkd ディレクトリ名 と入力すると、mkdir -p ディレクトリ名 で親も含め作成後、cd ディレクトリ名 で即移動。

---
- **ドメイン名から IP アドレスを取得する関数（後述）**
```bash
function DomainResolve() {
  local _host="$1"
  local _curl_base="curl --request GET"
  local _timeout="15"
  _host_ip=$($_curl_base -ks -m "$_timeout" "https://dns.google.com/resolve?name=${_host}&type=A" | \
    jq '.Answer[0].data' | tr -d "\"" 2>/dev/null)
  if [[ -z "$_host_ip" ]] || [[ "$_host_ip" == "null" ]] ; then
    echo -e "Unsuccessful domain name resolution."
  else
    echo -e "$_host > $_host_ip"
  fi
} 
```

- 引数に渡したホスト名（例: google.com）を Google DNS API 経由で解決し、最初の A レコードを表示。

- jq で JSON から .Answer[0].data 部分を抽出し、" を剥がして表示。

- 解決失敗時はメッセージを返却。

---
- **IP アドレスから ASN 情報を取得する関数（後述）**

```bash
function GetASN() {
  local _ip="$1"
  local _curl_base="curl --request GET"
  local _timeout="15"
  _asn=$($_curl_base -ks -m "$_timeout" "http://ip-api.com/line/${_ip}?fields=as")
  _state=$(echo $?)
  if [[ -z "$_ip" ]] || [[ "$_ip" == "null" ]] || [[ "$_state" -ne 0 ]]; then
    echo -e "Unsuccessful ASN gathering."
  else
    echo -e "$_ip > $_asn"
  fi
}
```
- 引数に IP アドレスを渡すと、ip-api.com で ASN 情報（例: AS15169 Google LLC）を取得して表示。
- 失敗時はエラーメッセージを返却。
