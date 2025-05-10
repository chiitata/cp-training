n, m, q = map(int, input().split())

a = [set() for _ in range(n+1)]
oauth = [0 for _ in range(n+1)]
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _,x, y = query
        a[y].add(x)
    elif query[0] == 2:
        _, x = query
        oauth[x] = 1
    else:
        _, x, y = query
        if oauth[x] == 1:
            print('Yes')
            continue
        if y in query[x]:
            print('Yes')
        else:
            print('No')