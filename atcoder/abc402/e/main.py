#!/usr/bin/env python3
import sys

input = sys.stdin.readline
N, X = map(int, input().split())
S = [0]*N
C = [0]*N
P = [0.0]*N
for i in range(N):
    s, c, p = map(int, input().split())
    S[i], C[i], P[i] = s, c, p / 100.0

# dp[mask][money] = mask の問題群が既に解けている状態で、
# 残り money 円を使って得られる最大期待得点
M = 1 << N
dp = [ [0.0] * (X + 1) for _ in range(M) ]

for money in range(1, X + 1):
    for mask in range(M):
        # 1) 何もしない（money-1 円まで使ったときと同じ期待値）
        best = dp[mask][money - 1]

        # 2) まだ解けていない問題 i を 1 回提出してみる
        for i in range(N):
            if not (mask & (1 << i)):
                cost = C[i]
                if cost <= money:
                    rem = money - cost
                    m2 = mask | (1 << i)
                    # 成功時：得点 S[i] + dp[m2][rem]
                    # 失敗時：dp[mask][rem]
                    exp_val = P[i] * (S[i] + dp[m2][rem]) \
                                + (1.0 - P[i]) * dp[mask][rem]
                    if exp_val > best:
                        best = exp_val

        dp[mask][money] = best

# 初期状態：どの問題も解いていない mask=0, 全予算 X 円
ans = dp[0][X]
# 小数点以下 10 桁まで表示
print(f"{ans:.10f}")