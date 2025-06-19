# Home Component テスト構築マニュアル (TypeScript + React Testing Library)

以下は、`Home.test.tsx` が最終的に **Jest + React Testing Library** で正常に動作するまでの**思考パターン**と手順を時系列順にまとめたマニュアル。

---

## 1. 初期状態とエラー確認

* **状況**: TSX で記述したテストが `spyOn` で `Cannot redefine property` や JSX 構文エラー、`toBeInTheDocument` 未定義などを返す。
* **気づき**:

    1. Babel による JSX 変換設定が不足 → **`jest.config.js` + `ts-jest` + `jest-environment-jsdom`** を追加。
    2. `toBeInTheDocument()` は **`@testing-library/jest-dom`** が必要。
    3. `spyOn(api, 'createMemo')` がプリミティブ関数上で失敗 → **モジュールモックが必要**。

---

## 2. Jest 設定の整備

1. **依存の追加**  (
   `package.json` の devDependencies)

   ```bash
   npm install -D jest ts-jest jest-environment-jsdom @types/jest \
     @testing-library/react @testing-library/jest-dom
   ```
2. **`jest.config.js`** を用意

   ```js
   const nextJest = require('next/jest')({ dir: './' });
   module.exports = nextJest({
     setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],
     testEnvironment: 'jest-environment-jsdom',
     transform: {
       '^.+\\.(ts|tsx)$': ['ts-jest', { tsconfig: 'tsconfig.json' }]
     }
   });
   ```
3. **`jest.setup.js`** でマッチャーをロード

   ```js
   require('@testing-library/jest-dom');
   ```

---

## 3. テスト用グローバル型の宣言

* **課題**: `global.fetch` を `jest.fn()` でモックすると TypeScript エラーが出る。
* **対応**: `global.d.ts` を追加し、`fetch` を `jest.Mock` として型定義。

  ```ts
  // global.d.ts
  import type { Mock } from 'jest';
  declare global { var fetch: Mock; }
  ```

---

## 4. `api.test.ts` の実装（fetch モック）

1. `global.fetch = jest.fn()` を直接設定
2. テスト内で **キャスト** してメソッド呼び出し

   ```ts
   (global.fetch as jest.Mock).mockClear();
   (global.fetch as jest.Mock).mockResolvedValueOnce(...);
   ```
3. 成功・失敗ケースを網羅。

    * `ok: true` → JSON レスポンス
    * `ok: false` → throws

---

## 5. `Home.test.tsx` の実装（モジュールモック）

1. **`jest.mock('../lib/api')`** でモジュール全体をモック
2. `const createMemoMock = api.createMemo as jest.Mock;`
3. 各テストで `beforeEach(() => jest.clearAllMocks());`
4. 成功時は `createMemoMock.mockResolvedValueOnce(...)`
5. 失敗時は `createMemoMock.mockRejectedValueOnce(...)`
6. UI 操作（`render` → `fireEvent`）→ 結果確認（`waitFor` + `toBeInTheDocument`）

---

## 6. 動作確認と結果

```bash
cd apps/frontend
tnpm run test
# ✔︎ 4 tests passed
```

全テストがパスしたことを確認できれば、**Home コンポーネントの API 呼び出しと UI 描画** が Jest + RTL でカバーされている状態。

---

## ポイントまとめ

* **モジュールモック** で `spyOn` 時の再定義エラーを回避
* **`ts-jest` + `jest-environment-jsdom`** で TSX の変換 & DOM API をサポート
* **`@testing-library/jest-dom`** で `toBeInTheDocument` 等の拡張マッチャーを利用
* **グローバル型宣言** で `fetch` モックの型エラーを解消
