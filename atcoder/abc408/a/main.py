# !/usr/bin/env python3

s, t = map(int, input().split())

a = [0] + list(map(int, input().split()))

for i in range(s):
    if a[i+1]-a[i]>t:
        print("No")
        exit()
else:
    print("Yes")