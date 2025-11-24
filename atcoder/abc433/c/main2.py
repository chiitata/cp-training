n = int(input())
a = list(map(int, input().split()))
val = []

for i in range(n):
    if i == 0:
        val.append((a[i], 1))
    else:
        if a[i] == a[i-1]:
            val[-1] = (a[i], val[-1][1]+1)
        else:
            val.append((a[i], 1))
