# 🏰 GitHub Pages について

---

## 🥉 はじめの一歩

1. **GitHub Pages とは？**
    - GitHub リポジトリをそのまま静的サイトとして公開できる
    - URL: `https://ユーザー名.github.io/リポジトリ名/`

2. **基本的な有効化手順**
```text
# 1. リポジトリを作成（Public 推奨）

# 2. mainブランチに index.html や README.md を配置

# 3. GitHub → Settings → Pages → Branch: main / Folder: /root を選択 → Save
```
3. 最小サンプル
- index.html を以下のように置くだけでOK
```html
<!DOCTYPE html>
<html>
<body>
<h1>GitHub Pages</h1>
</body>
</html>
```
4. 公式ドキュメント ☞
[`https://docs.github.com/pages`](https://docs.github.com/pages)

---

## 🥈 実用的カスタマイズ

1. カスタムドメイン設定
- DNS レコード
  - Aレコード: 185.199.108.153（GitHub Pages IP）
  - CNAME レコード: ユーザー名.github.io
- DNSレコードの最新IP確認 ☞ [`https://docs.github.com/ja/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages`](https://docs.github.com/ja/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages)

- リポジトリに CNAME ファイルを追加

2. Jekyll で Markdown → テンプレート
- _config.yml でサイト設定
- _posts/ にブログ投稿

**テーマ導入**

```yaml
theme: minima
```

**ビルドコマンド**

```bash
bundle exec jekyll serve
```

**実践的ヒントのアップデート**
- 🔧 Jekyll テーマ最適化
  - GitHub Pages は github-pages gem に同梱されたテーマ・プラグインのみ利用可。 　
  - テーマカスタマイズ or サードパーティテーマ使用時には GitHub Actions でビルドする必要あり。

```yaml
# _config.yml の例（明示的に github-pages を指定）
plugins:
  - jekyll-feed
  - jekyll-seo-tag

# Gemfile には以下を指定
gem "github-pages", group: :jekyll_plugins
```

- 公式サポートテーマ一覧 ☞ [`https://pages.github.com/themes/`](https://pages.github.com/themes/)
- 自作テーマやカスタムプラグインを使いたい場合は、ローカル or CI でビルドして gh-pages ブランチに出力。



3. GitHub Actions で自動デプロイ

```yaml
name: deploy
on:
  push:
    branches: [ main ]
jobs:
  build-and-publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with: node-version: '18'
      - run: npm install
      - run: npm run build     # React/Vue なら npm run build
      - uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public # build 出力先
```

---

## 🥇 さらに最適化

1. SPA デプロイ
- Next.js / Nuxt.js / Create React App → npm run build → gh-pages ブランチへ配備
- homepage フィールド設定（package.json）

```text
- SPA デプロイでのルーティング対策
  - GitHub Pages は すべてのリクエストを静的ファイルとして処理するため、SPAではリロード時に 404 エラーが発生。
    - 回避策
      - 404.html フォールバック
        - 404.html にルーティングスクリプトを記述し、すべてのパスを index.html に書き戻す。
      - React / Vue 向け調整
        - React: HashRouter に切り替える（URLに # を含める）
        - Vue Router: モードを hash にする or history モード + CIビルドで 404.html に適切に転送設定
```

- actions内で 404 を生成する例
```yaml
- name: Copy 404 to index.html (for SPA routing)
  run: cp public/index.html public/404.html

```

- 補足
- homepage フィールドを package.json に正確に記述（https://ユーザー名.github.io/リポジトリ名/）
- 複雑なパスルールが必要なら Cloudflare Pages や Netlify も検討
> peaceiris/actions-gh-pages は対象ブランチ（例：gh-pages）が存在しなくても、初回実行時に自動作成してくれる。


2. パフォーマンス & キャッシュ制御
- Cache-Control ヘッダーは _headers（Netlify）ではなく、GitHub Pages の限界を理解
- 外部CDN（Cloudflare）でエッジキャッシュを最適化

3. SEO & アナリティクス
- `<meta name="description">,　<link rel="canonical">`
- Google Analytics, Plausible などを <head> に埋め込む

4. プラグイン & 拡張
- Jekyll プラグイン（jekyll-seo-tag, jekyll-sitemap）
- GitHub Pages 制約下でも動作する「whitelisted」プラグインのみ利用可

5. セキュリティ
- https:// 強制リダイレクト（カスタムドメイン時に必要）
- 外部APIキーはビルド時に環境変数で注入

---


