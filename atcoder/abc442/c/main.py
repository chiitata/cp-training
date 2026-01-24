# !/usr/bin/env python3

import sys
input = sys.stdin.readline

def LI(): return list(map(int, input().split()))
def II(): return int(input())

n, m = map(int, input().split())
graph = [ 1 for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u] += 1
    graph[v] += 1

ans = []
for i in range(n):
    if n-graph[i] >= 3:
        a = graph[i]
        ans.append(((n-a)*(n-a-1)*(n-a-2))//6)
    else:
        ans.append(0)

print(*ans)