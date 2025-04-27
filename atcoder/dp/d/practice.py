# Knapsack問題
# dp[i][j] jは重さの合計がj以下で考える

N, W = map(int, input().split())
w = []
v = []
for _ in range(N):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)

# dp作成
dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
