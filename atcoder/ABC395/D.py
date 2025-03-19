n, q = map(int, input().split())

d = {i: i for i in range(1, n+1)}
container = {i: i for i in range(1, n+1)}
container_inv = {i: i for i in range(1, n+1)}

lis = []
for i in range(q):
    lis.append(list(map(int, input().split())))

for i in range(q):
    if lis[i][0] == 1:
        a = lis[i][1]
        b = lis[i][2]
        target_container = container_inv[b]
        d[a] = target_container
    elif lis[i][0] == 2:
        a = lis[i][1]
        b = lis[i][2]
        container_a = container_inv[a]
        container_b = container_inv[b]
        container[container_a], container[container_b] = container[container_b], container[container_a]
        container_inv[ container[container_a] ] = container_a
        container_inv[ container[container_b] ] = container_b

    elif lis[i][0] == 3:
        pos = d[lis[i][1]]
        print(container[pos])


