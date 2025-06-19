# オブジェクト型

## 概要
- オブジェクトの形（プロパティ名と型）を定義する
- オプショナルは `?` を使う
- 読み取り専用は `readonly`

## 最小例
```ts
type User = {
  id: string;
  name: string;
  email?: string;
  readonly createdAt: Date;
};
```

## 使いどころ
- データ構造の共有
- APIレスポンスやフォームの型付け

## 落とし穴
- オプショナルは「存在しない」ケースもあるため利用前にチェックする
