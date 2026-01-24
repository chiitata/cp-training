# !/usr/bin/env python3

import sys
input = sys.stdin.readline

def LI(): return list(map(int, input().split()))
def II(): return int(input())

s = list(input())

ans = 0
for i in s:
    if i == "j":
        ans += 1
    if i == "i":
        ans += 1

print(ans)