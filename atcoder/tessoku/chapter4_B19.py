n, q = map(int, input().split())
w = []
w.append([0, 0])
for i in range(n):
    w.append(list(map(int, input().split())))

dp = [[10**15 for _ in range(100001)]for _ in range(n+1)]

dp[0][0] = 0
for i in range(1, n+1):
    for j in range(0, 100001):
        if j<w[i][1]:
            dp[i][j] = dp[i-1][j]
        elif j >= w[i][1]:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-w[i][1]]+w[i][0])
        

for i in range(100000, -1, -1):
    if dp[n][i] <= q:
        print(i)
        break