# !/usr/bin/env python3

n = int(input())
a = list(map(int, input().split()))
can_go = a[0]-1

now = 0
while now < n:
    can_go = max(can_go, now+a[now]-1)
    if can_go == now:
        print(can_go+1)
        break
    now += 1
else:
    print(n)

