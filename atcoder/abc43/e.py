n, q = map(int, input().split())

a = list(map(int, input().split()))
q = []
for i in range(q):
    a, b, c = map(int, input())
    q.appen((a, b, c))

lis = set(a)

for que, l, r in q:
    if que == 1:
        lis[a[l]] -= 1
        lis[r] += 1
    elif que == 2:
        if l>r:
            print(l*len(a))
        else:
            