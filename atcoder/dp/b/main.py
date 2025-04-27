# !/usr/bin/env python3

n, k = map(int, input().split())
h = list(map(int, input().split()))

def in_grid(i):
    return 0<=i<n
dp = [10**9 for _ in range(n)]

dp[0] = 0

for i in range(n):
    for j in range(1, k+1):
        if in_grid(i+j):
            jmp = i+j
            dp[jmp] = min(dp[jmp], dp[i]+abs(h[jmp]-h[i]))

print(dp[n-1])
