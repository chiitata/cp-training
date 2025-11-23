# !/usr/bin/env python3

t = input()
l = [int(x) for x in list(str(t))]

hunman = []
renzoku = 1
for i in range(1, len(l)):
    if i == len(l)-1:
        if l[i] == l[i-1]:
            renzoku += 1
            hunman.append((l[i], renzoku))
        else:
            hunman.append((l[i-1], renzoku))
            hunman.append((l[i], 1))
    else:
        if l[i] == l[i-1]:
            renzoku += 1
        else:
            hunman.append((l[i-1], renzoku))
            renzoku = 1

if len(hunman) == 1:
    print(0)
    exit()
answer = 0
for i in range(1, len(hunman)):
    a, b = hunman[i-1]
    c, d = hunman[i]
    if a + 1 == c:
        answer += min(b, d)

print(answer)