from collections import deque
import sys
n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[v].append(u) 

is_black = [False] * n

def mark_black(n, graph, start, is_black):
    queue = deque()
    
    if is_black[start]:
        return
        
    is_black[start] = True
    queue.append(start)
    
    while queue:
        u = queue.popleft()
        
        for v in graph[u]:
            if not is_black[v]:
                is_black[v] = True
                queue.append(v)


q = int(input())
for i in range(q):
    s, t = map(int, input().split())
    
    if s == 1:
        mark_black(n, graph, t - 1, is_black)
    elif s == 2:
        if is_black[t - 1]:
            print("Yes")
        else:
            print("No")