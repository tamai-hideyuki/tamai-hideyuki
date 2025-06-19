# type と interface

## 概要
- `type` は型エイリアス
- `interface` はオブジェクト形状を宣言

## 最小例
```ts
type User = {
  id: string;
  name: string;
};

interface User2 {
  id: string;
  name: string;
}
```

## 使いどころ
- オブジェクトの拡張が必要なら `interface`
- UnionやIntersectionを作るなら `type`

## 落とし穴
- `interface` は同名で宣言合成される

## 補足: 宣言合成（declaration merging）
同じ名前の `interface` は自動的に結合される。

```ts
interface User {
  id: string;
}

interface User {
  name: string;
}

const u: User = { id: "1", name: "Aki" };
```

結果として `User` は次の形になる。

```ts
interface User {
  id: string;
  name: string;
}
```

## 宣言合成のメリット・デメリット

### メリット
- 外部ライブラリやグローバル型の拡張がしやすい
- 大きい型を分割して段階的に拡張できる
- 既存JS資産に後から型を足せる

### デメリット
- 同名の意図しない拡張が起きやすい
- どこで追加されたか追いづらくなる
- 設計意図とずれた拡張が混ざると保守性が下がる

## 使いどころ（慎重に選ぶ指針）
- ライブラリやグローバル型を拡張したいとき（例: `Window`, `Express.Request`）
- 公開APIの契約として「将来拡張」を想定するとき
- 複数モジュールが同じ型を拡張するプラグイン設計
- クラスと組み合わせて `implements` する場合

## 慎重になるべきケース
- 予期せぬ宣言合成を避けたいとき
- 同名が多くなりそうな大規模コードベース

## 具体例

### 1. ライブラリ型の拡張（グローバル）
```ts
declare global {
  interface Window {
    appVersion: string;
  }
}

window.appVersion = "1.2.3";
```

### 2. プラグイン設計での拡張
```ts
interface PluginOptions {
  name: string;
}

// 別モジュールで拡張
interface PluginOptions {
  enabled: boolean;
}

const opt: PluginOptions = { name: "logger", enabled: true };
```

### 3. クラスと組み合わせる
```ts
interface Identifiable {
  id: string;
}

class User implements Identifiable {
  constructor(public id: string) {}
}
```
