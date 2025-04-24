#　これは01BFSの問題っぽい気がする
# (0, 0)を壁蹴り回数0回に設定して、もし(i, j)が#ならば(i-1, j)と(i, j-1)の小さいほうの値を挿入

from collections import deque

H, W = map(int, input().split())
grid = []
for _ in range(H):
    grid.append(list(input()))

def in_grid(i, j):
    return 0<=i<H and 0<= j<W

done = []
for _ in range(H):
    done.append([False]*W)
a, b, c, d = map(int, input().split())
a, b, c, d = a-1, b-1, c-1, d-1

Q = deque([(0, a, b)])
while Q:
    dist, x, y = Q.popleft()
    if done[x][y]:
        continue
    if (x, y) == (c, d):
        print(dist)
        break
    done[x][y] = True
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        if in_grid(x+dx, y+dy) and not done[x+dx][y+dy] and grid[x+dx][y+dy] == '.':
            Q.appendleft((dist, x+dx, y+dy))
        elif in_grid(x+dx, y+dy) and not done[x+dx][y+dy]:
            Q.append((dist+1, x+dx, y+dy))
            if in_grid(x+2*dx, y+2*dy) and not done[x+2*dx][y+2*dy]:
                Q.append((dist+1, x+2+dx, y+2*dy)) 


