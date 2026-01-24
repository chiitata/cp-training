# !/usr/bin/env python3

import sys
input = sys.stdin.readline

def LI(): return list(map(int, input().split()))
def II(): return int(input())

sound = 0
is_play = False

q = int(input())
for i in range(q):
    a = int(input())
    if a == 1:
        sound += 1
    elif a == 2:
        if sound > 0:
            sound -= 1
    elif a == 3:
        if is_play:
            is_play = False
        else:
            is_play = True
    if sound >= 3:
        if is_play:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
    