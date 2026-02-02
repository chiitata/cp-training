# !/usr/bin/env python3

import sys
input = sys.stdin.readline

def LI(): return list(map(int, input().split()))
def II(): return int(input())

n , m = LI()
s = list(input())
t = list(input())
q = int(input())

for i in range(q):
    x = list(input())
    ta = True
    ao = True   
    for j in range(len(x)):
        if x[j] not in s:
            ta = False
        if x[j] not in t:
            ao = False
    if ta and ao:
        print("Unknown")
    elif ta:
        print("Takahashi")
    elif ao:
        print("Aoki")
    else:
        print("Unknown")