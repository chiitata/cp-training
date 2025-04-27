# !/usr/bin/env python3

# dpを作らないといけないしかし重さは10**9まであるので重さでdpは作れない→価値と品物でdpを作ればよい
# dp[i][j]　iはどの品物まで選択可能かmaxはｎ jは価値がどれほどか一番多くても10**5までなのでそこで作ればよい
# すなわち品物iまで選択可能な時の価値jを得るために必要な重さminを使うそして最後に取り出せばよい

N, W = map(int, input().split())
w = []
v = []
for _ in range(N):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)

dp = [[(10**9)+1 for _ in range(10**5+1)] for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range((10**5)+1):
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        if j+v[i] <= (10**5):
            dp[i+1][j+v[i]] = min(dp[i+1][j+v[i]], dp[i][j]+w[i])

for i in range(10**5, -1, -1):
    if dp[N][i] <= W:
        print(i)
        exit()
