# !/usr/bin/env python3

import sys
input = sys.stdin.readline

def LI(): return list(map(int, input().split()))
def II(): return int(input())

n, k, x = map(int, input().split())
a = LI()

a.sort()
ans = 0
for i in range(k):
    ans += a[k-1-i]  
    if ans >= x:
        print(i+1+(n-k))
        exit()
else:
    print(-1)
        