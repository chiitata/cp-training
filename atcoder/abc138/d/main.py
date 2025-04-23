# !/usr/bin/env python3
from collections import deque

n, q = map(int, input().split())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [False]*(n+1)
visited[1] = True
que = deque()
que.append(1)
counter = [0 for _ in range(n+1)]
for _ in range(q):
    p, x = map(int, input().split())
    counter[p] += x


while que:
    now = que.popleft()
    now_number = counter[now]
    for to in tree[now]:
        if visited[to] == False:
            counter[to] += now_number
            visited[to] = True
            que.append(to)
print(*counter[1:])