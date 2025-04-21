# !/usr/bin/env python3
from collections import deque

q = int(input())

stack = deque()
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        stack.append(query[1])
    elif query[0] == 2:
        x = stack.popleft()
        print(int(x))

if len(stack) == q:
    print()