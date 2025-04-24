N, M = map(int, input().split())

a = []
num = 0

for i in range(M):
    u, v = map(int, input().split())
    if u == v or [u, v] in a or [v, u] in a:
        num += 1
        continue
    a.append([u, v])

print(num)
