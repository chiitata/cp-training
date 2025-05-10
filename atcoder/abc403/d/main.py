# !/usr/bin/env python3

#!/usr/bin/env python3
import sys
from collections import defaultdict

input = sys.stdin.readline


def min_deletions(A, D):
    N = len(A)
    # D=0 の場合は「等しいペアは禁止」→ 同じ値は1つしか残せない
    if D == 0:
        return N - len(set(A))

    # 1. 各値 v の出現回数を数える
    freq = defaultdict(int)
    for v in A:
        freq[v] += 1

    # 2. あまり r = v % D ごとにグループ化
    groups = defaultdict(list)
    for v in freq:
        groups[v % D].append(v)

    max_keep = 0
    # 3. 各グループで、「隣接する値 v, v+D が選べない」重み付き独立集合 (パスDP)
    for _, vs in groups.items():
        vs.sort()
        # dp0 = i-1 の値を選ばなかったときの最大重み
        # dp1 = i-1 の値を選んだときの最大重み
        dp0 = dp1 = 0
        prev = None
        for v in vs:
            w = freq[v]
            if prev is not None and v == prev + D:
                # 直前のノードと衝突する場合は典型的パスDP:
                ndp0 = max(dp0, dp1)
                ndp1 = dp0 + w
            else:
                # 衝突しない（D 間隔が飛んでいる）なら両方取ってOK
                ndp0 = max(dp0, dp1)
                ndp1 = ndp0 + w
            dp0, dp1 = ndp0, ndp1
            prev = v
        max_keep += max(dp0, dp1)

    # 4. 残せる要素数 max_keep → 削除数は N - max_keep
    return N - max_keep


N, D = map(int, input().split())
A = list(map(int, input().split()))
print(min_deletions(A, D))

