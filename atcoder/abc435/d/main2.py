from collections import deque
n, m = map(int, input().split())

graph = [[] for _ in range(n)]
is_black = [False for _ in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x].append(y)


def check(a):
    if is_black[a] == True:
        return True
    else:
        return False

def black(a, graph):
    d = deque()
    d.append(a)
    is_black[a] = True
    while d:
        p = d.popleft()
        if is_black[p] == True:
            break
        else:
            is_black[p] = True
        d.append(graph[p])

q = int(input())

for i in range(q):
    a, b = map(int, input().split())
    b -= 1
    if a == 1:
        black(a, graph)
    elif a == 2:
        judge = check(b)
        if judge:
            print('Yes')
        else:
            print('No')






