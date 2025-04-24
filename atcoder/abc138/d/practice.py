from collections import deque

n, q = map(int, input().split())
visited = [False]*(n+1)
que = deque()
tree = [[]for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

count = [0 for _ in range(n+1)]
for i in range(q):
    p, x = map(int, input().split())
    count[p] += x

que.append(1)
visited[1] = True
while que:
    now = que.popleft()
    now_numbers = count[now]
    for i in tree[now]:
        if visited[i] == False:
            count[i] += now_numbers
            visited[i] = True
            que.append(i)

print(*count[1:])
