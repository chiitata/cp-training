# !/usr/bin/env python3

import sys
input = sys.stdin.readline

def LI(): return list(map(int, input().split()))
def II(): return int(input())

n = int(input())

digits = [int(d) for d in str(n)]

def check(digits):
    digits_tmp = 0
    for i in range(len(digits)):
        if i == 0:
            digits_tmp = 0
        digits_tmp += digits[i]**2
        if digits_tmp == 1 and i == len(digits) - 1:
            return True, digits_tmp
    return False, digits_tmp

old = []

while True:
    is_ok, digits_tmp = check(digits)
    if is_ok:
        print("Yes")
        break
    if digits_tmp in old:
        print("No")
        break
    old.append(digits_tmp)
    digits = [int(d) for d in str(digits_tmp)]