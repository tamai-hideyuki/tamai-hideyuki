# リテラル型 / as const

## 概要
- 文字列や数値そのものを型として扱う
- `as const` でリテラル型を固定できる

## 最小例
```ts
const status = "ready"; // 型: "ready"
let mode = "dark"; // 型: string

const config = {
  theme: "dark",
  retry: 3,
} as const;
```

## 使いどころ
- ステータス値や固定フラグ
- 定数オブジェクトの型固定

## 落とし穴
- `as const` は全プロパティを読み取り専用にする

## 補足: 「読み取り専用」とは
`as const` を付けるとオブジェクトの各プロパティが `readonly` になり、値もリテラル型に固定される。

```ts
const config = {
  theme: "dark",
  retry: 3,
} as const;

// 型のイメージ
// {
//   readonly theme: "dark";
//   readonly retry: 3;
// }

// 代入はエラー
// config.theme = "light";
// config.retry = 5;
```
