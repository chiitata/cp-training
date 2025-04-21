# !/usr/bin/env python3

s = list(input())
answer = []
for i in s:
    if i.isupper():
        answer.append(i)

print("".join(answer))