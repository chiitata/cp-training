import sys
from collections import deque, defaultdict

input = sys.stdin.readline

h, w = map(int, input().split())
s = []
for i in range(h):
    s.append(list(input().strip()))

warp_points = defaultdict(list)
for i in range(h):
    for j in range(w):
        if s[i][j] != "#" and s[i][j] != ".":
            warp_points[s[i][j]].append((i, j))

used_chars = set()

dist = [[-1] * w for _ in range(h)]
dist[0][0] = 0

dp = deque([(0, 0)])

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while dp:
    r, c = dp.popleft()

    if r == h - 1 and c == w - 1:
        print(dist[r][c])
        sys.exit()

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        
        if 0 <= nr < h and 0 <= nc < w:
            if s[nr][nc] != "#" and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                dp.append((nr, nc))

    char = s[r][c]
    if 'a' <= char <= 'z' and char not in used_chars:
        for nr, nc in warp_points[char]:
            if dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                dp.append((nr, nc))
        
        used_chars.add(char)

print(-1)