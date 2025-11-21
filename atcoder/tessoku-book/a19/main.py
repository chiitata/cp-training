# !/usr/bin/env python3

n, w = map(int, input().split())

vals = []
dp = [-float('inf')] * (w + 1)
dp[0] = 0
for _ in range(n):
    wi, vi = map(int, input().split())
    vals.append((wi, vi))


for weight, value in vals:
    for i in range(w, weight - 1, -1):
        if dp[i - weight] != -float('inf'):
            dp[i] = max(dp[i], dp[i - weight] + value)

print(max(dp))
