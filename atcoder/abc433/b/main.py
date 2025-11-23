# !/usr/bin/env python3

n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    if i == 0:
        print(-1)
        continue
    for j in range(i-1, -1, -1):
        if a[j] > a[i]:
            print(j+1)
            break
    else:
        print(-1)

