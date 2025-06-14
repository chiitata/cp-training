# !/usr/bin/env python3

n, q = map(int, input().split())

x = list(map(int, input().split()))

hako = [0 for _ in range(n)]

for i in x:
    i -= 1
    if i == -1:
        min_value = min(hako)
        min_index = hako.index(min_value)
        print(min_index+1, end =" ")
        hako[min_index] += 1
        continue
    print(i+1, end = " ")
    hako[i] += 1
print()
