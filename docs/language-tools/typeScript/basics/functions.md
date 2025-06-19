# 関数の型

## 概要
- 引数と戻り値に型を付ける
- 戻り値は推論でOKだが、公開APIは明示すると安心

## 最小例
```ts
function add(a: number, b: number): number {
  return a + b;
}

const greet = (name: string): string => {
  return `Hello, ${name}`;
};
```

## 使いどころ
- コールバックやイベントは関数型を明示

## 落とし穴
- `void` と `undefined` は異なる
