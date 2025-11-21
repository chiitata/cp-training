# !/usr/bin/env python3

x = int(input())
n = int(input())
parts = [False]*n
w = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    query = int(input())-1
    if parts[query]:
        x -= w[query]
    else:
        x += w[query]

print(x)
