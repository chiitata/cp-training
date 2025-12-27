# !/usr/bin/env python3

import sys
input = sys.stdin.readline

def LI(): return list(map(int, input().split()))
def II(): return int(input())

d, f = map(int, input().split())

while f<=d:
    f += 7
print(f-d)