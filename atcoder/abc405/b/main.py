# !/usr/bin/env python3

n, m = map(int, input().split())
a = list(map(int, input().split()))

t = ["None" for _ in range(m+1)]
answer = 0
length = 0
for i in range(n):
    if t[a[i]] == "None":
        answer += 1
        t[a[i]] = "Yes"
    if answer == m:
        length = i+1
        break
else:
    print(0)
    exit()

print(n-length+1)
