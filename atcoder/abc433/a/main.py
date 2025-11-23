# !/usr/bin/env python3

x, y, z = map(int, input().split())

for i in range(100000):
    if x//y == z and x%y == 0:
        print('Yes')
        break
    x , y = x+1, y+1
else:
    print('No')