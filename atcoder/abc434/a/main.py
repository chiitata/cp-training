# !/usr/bin/env python3

a, b = map(int, input().split())

a = a*1000

p = 0

while a >= b:
    a -= b
    p += 1

print(p)