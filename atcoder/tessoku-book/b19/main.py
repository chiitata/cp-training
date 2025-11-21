# !/usr/bin/env python3

n, wi = map(int, input().split())

vals = []
max_value = 0
for _ in range(n):
    w, v = map(int, input().split())
    vals.append((w, v))
    max_value += v

dp = [float('inf')] * (max_value+1)

dp[0] = 0

for weight, value in vals:
    for i in range(max_value, value-1, -1):
        if dp[i-value] != -float('inf'):
            dp[i] = min(dp[i], dp[i-value]+weight)

for i in range(max_value, -1, -1):
    if dp[i] <= wi:
        print(i)
        break