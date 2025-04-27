#!/usr/bin/env python3
import sys

input = sys.stdin.readline

n, m, q = map(int, input().split())

# 1) d[x] に追加した y を O(1) で検索できるように set を使う
d = [set() for _ in range(n+1)]
# 2) 「タイプ2」でマークする x を O(1) で調べるために真偽値リストを用意
marked = [False] * (n+1)

out = []
for _ in range(q):
    qry = list(map(int, input().split()))
    t = qry[0]

    if t == 1:
        _, x, y = qry
        d[x].add(y)               # O(1)
    elif t == 2:
        _, x = qry
        marked[x] = True          # O(1)
    else:  # t == 3
        _, x, y = qry
        # マーク済み or d[x] に y があれば Yes
        if marked[x] or (y in d[x]):
            out.append("Yes\n")  # membership in set is O(1)
        else:
            out.append("No\n")

# まとめて出力でさらに高速化
sys.stdout.write(''.join(out))
