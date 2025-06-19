# externally-managed-environment

##  エラー内容

```bash
python3 -m pip install --user pandas
```

- 実行時に以下のエラーが発生：

```bash
language-tools: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try brew install ...
```
## 原因
```text
このエラーは、Homebrew が管理している Python 環境で pip install を実行したことにより発生します。

PEP 668 に準拠し、Homebrew 環境では Python パッケージを直接インストールすることで、
 
Python 本体や Homebrew の整合性が壊れるリスクがあるため、制限がかかっています。
```

## 解消方法（おすすめ順）

- **方法1：仮想環境（venv）を使う【推奨】**
```bash
# 仮想環境を作成
python3 -m venv .venv

# 仮想環境を有効化（bash/zshの場合）
source .venv/bin/activate

# パッケージをインストール
pip install pandas
```

- **方法2：--break-system-packages を使用【自己責任】**
```bash
python3 -m pip install --break-system-packages --user pandas
```
> ⚠ Homebrew 環境に予期しない影響を与える可能性あり。非推奨。

- **方法3：pipx を使う（CLIツール向け）**
```bash
brew install pipx
pipx install pandas  # 通常は pandas には向かない
```


## 補足
- --user オプションであっても、macOS + Homebrew の一部環境ではブロックされることがあります。
- システムに影響を与えない開発のために、仮想環境（venv）を活用するのがベストプラクティスです。
- 