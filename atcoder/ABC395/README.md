### 1行に複数の整数の入力を取得し、整数として出力する
```Python
a = list(map(int, input().split()))
```

### N×Nの行列を出力する
```Python
for i in a:
    print("".join(map(str, i)))
```

### 空の行列を作成するときに
```Python
a = [[None for _ in range(n)] for _ in range(n)]
```
各行が独立したリストになる
内側のリスト ```[None for _ in range(n)]``` が毎回新しく作成され、それが外側のリストに追加されます。
影響範囲が限定される
ある行の要素を変更しても、他の行には影響しません。
```Python
a = [[None]*n]*n
```
浅いコピーが行われる
内側のリスト ```[None]*n``` を1回作成し、それを n 回コピーして外側のリストに追加します。
全ての行が同じリストを参照する
そのため、ある行の要素を変更すると、全ての行で同じ位置の要素が変更されてしまいます。

### 辞書をうまく使えるようになる
indexと数字を同時に扱いたいときは
```enumerate(iterable, start=)```startは必須ではない
```for i, num in enumerate(a):
    if num in last_occurrence(辞書):```
enumerateでindexと数字を取り出した後にその数字が辞書の中に入っているか確認するコード

### D 物理的巣番号と論理的巣番号
計算を軽くするためにdict型を使う
巣の入れ替えは論理的巣番号を変更することで実装

