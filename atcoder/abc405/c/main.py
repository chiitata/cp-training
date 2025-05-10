# !/usr/bin/env python3

n = int(input())
a = list(map(int, input().split()))

sigma = sum(a)
answer = 0
for i in range(n):
    answer += a[i]*(sigma-a[i])
    sigma -= a[i]
print(answer)