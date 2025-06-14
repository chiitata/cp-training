# !/usr/bin/env python3

a, b = map(int, input().split())

if a/b-a//b < 0.5:
    print(a//b)
else:
    print((a//b)+1)