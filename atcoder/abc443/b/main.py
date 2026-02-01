n, k = map(int, input().split())
t = 0
c = 0
while True:
    t += n
    n += 1
    c += 1
    if t >= k:
        break
print(c-1)
