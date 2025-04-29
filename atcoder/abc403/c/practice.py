n, m, q = map(int, input().split())

a = [set() for _ in range(2*10**5+1)]
oauth = [0 for _ in range(2*10**5+1)]
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        y = query[2]
        a[y] += x
    elif query[0] == 2:
        x = query[1]
        oauth[x] = 1
    else:
        x = query[1]
        y = query[2]
        if oauth[x] == 1:
            print('Yes')
            continue
        if y in query[x]:
            print('Yes')
        else:
            print('No')