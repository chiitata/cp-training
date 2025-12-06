# !/usr/bin/env python3

n = int(input())

a = list(map(int, input().split()))

answer = 0
for i in range(n-1):
    for j in range(i+1, n):
        check = a[i:j+1]
        goukei = sum(check)
        for k in range(len(check)):
            if goukei % check[k] == 0:
                break
        else:
            answer += 1

print(answer)