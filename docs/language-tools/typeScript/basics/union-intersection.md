# Union / Intersection

## 概要
- Union: `A | B` どちらかの型
- Intersection: `A & B` 両方の型を満たす

## 最小例
```ts
type Id = string | number;

type WithName = { name: string };
type WithAge = { age: number };

type Person = WithName & WithAge;
```

## 使いどころ
- Unionで分岐パターンを表現
- Intersectionで複数の特徴を合成

## 落とし穴
- Unionは利用時に絞り込みが必要（型ガード）
