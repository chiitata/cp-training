# !/usr/bin/env python3

n, q = map(int, input().split())

a = [(i+1) for i in range(n)]
t = 0
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        p, x = query[1], query[2]
        p = (p+t-1)%len(a)
        a[p] = x
    elif query[0] == 2:
        p = query[1]
        p = (p+t-1)%len(a)
        print(a[p])
    elif query[0] == 3:
        k = query[1]
        k = k%len(a)
        t = (t+k)%len(a)
