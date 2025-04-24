# !/usr/bin/env python3
# これはBFSの問題である
# このような問題を多点スタートな最短経路問題という
# まずは標準入力
h, w = map(int, input().split())
grid = []
for i in range(h):
    grid.append(list(input()))

def in_grid(x, y):
    return 0<=x<h and 0<=y<w

from collections import deque

que = deque()

for i in range(h):
    for j in range(w):
        if grid[i][j] == '#':
            que.append((i, j, 0))

while que:
    x, y, dist = que.popleft()
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if in_grid(x+dx, y+dy) and grid[x+dx][y+dy] == '.':
            que.append((x+dx, y+dy, dist+1))
            grid[x+dx][y+dy] = '#'

print(dist)