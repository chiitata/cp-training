n, q = map(int, input().split())
a = [0]+list(map(int, input().split()))
b = []
sgm = 0
for i in range(len(a)):
    sgm += a[i]
    b.append(sgm)

r = [None]*(n+1)
for i in range(1, n+1):
    if i == 1:
        r[i] = 0
        while r[i] < n and b[r[i]+1]<= q:
            r[i] += 1
    else:
        r[i] = r[i-1]
        while r[i] < n and b[r[i]+1] - b[i-1] <= q:
            r[i] += 1

for i in range(1, n+1):
    r[i] = r[i]-i+1
answer = 0
for i in range(1, n+1):
    answer += r[i]

print(answer)