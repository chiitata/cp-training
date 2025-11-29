# !/usr/bin/env python3

n, m = map(int, input().split())

weight = [0 for i in range(m+1)]
number = [0 for i in range(m+1)]

for i in range(n):
    a, b = map(int, input().split())
    weight[a] += b
    number[a] += 1

for i in range(1, m+1):
    if number[i] != 0:
        print(weight[i]/number[i])
