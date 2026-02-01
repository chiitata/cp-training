n, t = map(int, input().split())

a = list(map(int, input().split()))

close = [False for _ in range(t)]

for i in range(len(a)):
    for j in range(a[i]):
        if j-1<=len(t)-1:
            close[j-1] = True
