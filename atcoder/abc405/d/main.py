# !/usr/bin/env python3
h, w = map(int, input().split())

def in_grid(x, y):
    if 0<=x<h:
        if 0<=y<w:
            return True
        else:
            False
    else:
        return False
t = []
visited = [[False for _ in range(w)]for _ in range(h)]
startlist = []
for i in range(h):
    t.append(list(input()))
start, end = 0, 0
for i in range(h):
    for j in range(w):
        if t[i][j] == "E":
            startlist.append((i, j))
from collections import deque

d = [[10**9 for _ in range(w)]for _ in range(h)]
que = deque()
for i, j in startlist:
    que.append((i, j))
for i, j in startlist:
    d[i][j] = 0
while que:
    x, y = que.popleft()
    if visited[x][y]:
        continue
    visited[x][y] = "True"
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if in_grid(x+dx, y+dy) and t[x+dx][y+dy] == ".": 
            if visited[x+dx][y+dy] == False:
                d[x+dx][y+dy] = min(d[x+dx][y+dy], d[x][y]+1)
                que.append((x+dx, y+dy))
            else:
                continue
visited2 = [[False for _ in range(w)]for _ in range(h)]
answer = [[None for _ in range(w)]for _ in range(h)]
que2 = deque()
for i, j in startlist:
    que2.append((i, j))
for i, j in startlist:
    answer[i][j] = "E"
while que2:
    x, y = que2.popleft()
    if visited2[x][y]:
        continue
    visited2[x][y] = "True"
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if in_grid(x+dx, y+dy):
            que2.append((x+dx, y+dy))
            if d[x][y] == d[x+dx][y+dy]-1:
                if dx == 1:
                    answer[x+dx][y+dy] = "^"
                elif dx == -1:
                    answer[x+dx][y+dy] = "v"
                elif dy == 1:
                    answer[x+dx][y+dy] = "<"
                elif dy == -1:
                    answer[x+dx][y+dy] = ">"

for i in range(h):
    for j in range(w):
        if answer[i][j] == None:
            print("#", end="")
        else:
            print(answer[i][j], end="")
    else:
        print()




