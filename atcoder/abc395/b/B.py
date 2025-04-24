n = int(input())

a = [[None for _ in range(n)] for _ in range(n)]

i = 0
j = n-1

while i<=j:
    if i%2==0:
        for m in range(i, n-i):
            for k in range(i, n-i):
                a[m][k] = '#'
    elif i%2 == 1:
        for m in range(i, n-i):
            for k in range(i, n-i):
                a[m][k] = '.'
    i += 1
    j -= 1

for i in a:
    print("".join(map(str, i)))