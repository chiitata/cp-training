# !/usr/bin/env python3

n, q = map(int, input().split())
if q == 1:
    if 1600<=n<=2999:
        print('Yes')
    else:
        print("No")
elif q==2:
    if 1200<=n<=2399:
        print("Yes")
    else:
        print('No')