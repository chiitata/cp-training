N = int(input())

P = list(map(int, input().split()))

p = [0 for _ in range(101)]

for i in range(N):
    p[P[i]] += 1


r = 1
for i in range(100, 0, -1):
    k = p[i]
    p[i] = r
    r += k

for i in P:
    print(p[i])
