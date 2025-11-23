# !/usr/bin/env python3

n, m = map(int, input().split())
a = list(map(int, input().split()))

t = []
for i in range(len(a)):
    t.append((a[i]%m, len(str(a[i]))))