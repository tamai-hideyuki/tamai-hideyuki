# any / unknown / never

## 概要
- `any`: 何でも許容（型安全を失う）
- `unknown`: 何でも受け取れるが利用時に絞り込みが必要
- `never`: 到達しない型（例外、無限ループ）

## 最小例
```ts
let a: any = 1;
let b: unknown = "text";

function fail(message: string): never {
  throw new Error(message);
}
```

## 使いどころ
- `unknown` を入口、絞り込み後に型確定
- `never` は網羅性チェックに活用

## 落とし穴
- `any` は最後の手段として使う
