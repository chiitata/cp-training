# !/usr/bin/env python3

import sys
import math
import bisect
input = sys.stdin.readline

def LI(): return list(map(int, input().split()))
def II(): return int(input())

n, q = map(int, input().split())
m = []
for _ in range(n):
    x, y = map(int, input().split())
    m.append(math.atan2(y, x))

monster = m.copy()
m.sort()

for _ in range(q):
    a, b = map(int, input().split())
    s, t = monster[a-1], monster[b-1]
    if s >= t:
        print(bisect.bisect_right(m, s)-bisect.bisect_left(m, t))
    else:
        right = bisect.bisect_right(m, s)
        left = bisect.bisect_left(m, t)
        print(n+right-left)

