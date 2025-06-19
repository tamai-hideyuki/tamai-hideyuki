# ジェネリクス

## 概要
- 型を引数として受け取る
- 再利用性の高い関数・型を作れる

## 最小例
```ts
function wrap<T>(value: T): { value: T } {
  return { value };
}

const result = wrap(123); // T = number
```

## 使いどころ
- 配列操作、APIレスポンスラッパー

## 落とし穴
- 型推論に頼りすぎると意図が見えにくい
