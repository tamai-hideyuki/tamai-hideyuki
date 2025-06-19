# ユーティリティ型

## 概要
- 既存の型を変形して再利用する
- 代表例: `Partial`, `Pick`, `Omit`, `Record`

## 最小例
```ts
type User = {
  id: string;
  name: string;
  email: string;
};

type UserPreview = Pick<User, "id" | "name">;
type UserUpdate = Partial<User>;
```

## 使いどころ
- API更新フォーム、一覧表示用の簡易型

## 落とし穴
- `Partial` で必須項目が曖昧になる点に注意
