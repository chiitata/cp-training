x = list(input())
y = []
for i in x:
    y.append(int(i)) 

t = []
z = []
for i in y:
    if i != 0:
        t.append(i)
    else:
        z.append(i)

t.sort()

print(t[0], end='')

if len(z) != 0:
    for i in z:
        print(i, end='')

for i in range(1, len(z)):
    print(t[i], end='')


