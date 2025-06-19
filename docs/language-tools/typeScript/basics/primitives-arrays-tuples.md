# プリミティブ型・配列・タプル

## 概要
- 基本型: `string`, `number`, `boolean`, `bigint`, `symbol`, `null`, `undefined`
- 配列は `T[]` または `Array<T>`
- タプルは固定長・各要素に型を指定

## 最小例
```ts
const name: string = "Aki";
const age: number = 30;
const isActive: boolean = true;

const tags: string[] = ["ts", "js"];
const scores: Array<number> = [10, 20];

const user: [string, number] = ["Aki", 30];
```

## 使いどころ
- 配列は同じ型の集まり
- タプルは「順番が意味を持つ」小さな固定データ

## 落とし穴
- タプルでも `push` は許可されることがある（型崩れ注意）
