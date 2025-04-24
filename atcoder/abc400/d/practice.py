# これは01BFSの問題である
from collections import deque

h, w = map(int, input().split())

s = []
for _ in range(h):
    s.append(list(input()))

a, b, c, d = map(int, input().split())
a -= 1
b -= 1 
c -= 1 
d -= 1 

def in_grid(x, y):
    return 0<=x<h and 0<=y<w

done = []
for _ in range(h):
    done.append([False]*w)

Q = deque()
Q.append((0, a, b))

while Q:
    dist, x, y = Q.popleft()
    if done[x][y]:
        continue
    if (c, d) == (x, y):
        print(dist)
        break
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if in_grid(x+dx, y+dy) and not done[x+dx][y+dy] and s[x+dx][y+dy] == '.':
            Q.appendleft((dist, x+dx, y+dy))
        elif in_grid(x+dx, y+dy) and not done[x+dx][y+dy]:
            Q.append((dist+1, x+dx, y+dy))
            if in_grid(x+2*dx, y+2*dy) and not done[x+2*dx][y+2*dy]:
                Q.append((dist+1, x+2+dx, y+2*dy)) 

