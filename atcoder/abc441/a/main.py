# !/usr/bin/env python3

import sys
input = sys.stdin.readline

def LI(): return list(map(int, input().split()))
def II(): return int(input())

a, b = LI()
c, d = LI()

if 0 <= c -a <= 99 and 0 <= d - b <= 99:
    print("Yes")
else:
    print("No")