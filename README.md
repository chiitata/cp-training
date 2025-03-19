### 競技プログラミング学習用リポジトリです。  

# 1行に複数の整数の入力を取得し、整数として出力する
```Python
a = list(map(int, input().split()))
```

# N×Nの行列を出力する
```Python
for i in a:
    print("".join(map(str, i)))
```

# 空の行列を作成するときに
```Python
a = [[None for _ in range(n)] for _ in range(n)]
```
これと
```Python
a = [[None]*n]*n
```
は別物なので注意