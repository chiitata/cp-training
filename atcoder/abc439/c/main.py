import sys

N = int(sys.stdin.readline())

if N < 5:
    print(0)
    print()
    exit()

spf = list(range(N + 1))
for i in range(2, int(N**0.5) + 1):
    if spf[i] == i:
        for j in range(i*i, N + 1, i):
            if spf[j] == j:
                spf[j] = i

good_integers = []

for n in range(1, N + 1):
    temp = n
    
    count_4k1 = 0
    exponent_4k1 = 0
    is_valid = True
    
    while temp > 1:
        p = spf[temp]
        exponent = 0
        while temp % p == 0:
            temp //= p
            exponent += 1
        
        if p == 2:
            continue
        
        if p % 4 == 1:
            count_4k1 += 1
            exponent_4k1 = exponent
            if count_4k1 > 1:
                is_valid = False
                break
        else:
            if exponent % 2 != 0:
                is_valid = False
                break
    
    if is_valid and count_4k1 == 1 and (exponent_4k1 == 1 or exponent_4k1 == 2):
        good_integers.append(n)

print(len(good_integers))
print(*good_integers)

