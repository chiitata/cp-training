# !/usr/bin/env python3

n = int(input())
a = list(map(int, input().split()))
k = int(input())

answer = 0
for i in a:
    if i >= k:
        answer += 1

print(answer)