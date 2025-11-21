import copy

n, x, y = map(int, input().split())

a = list(map(int, input().split()))

check = []

for i in a:
    check.append(i*x)

gcd = y - x
for_answer = copy.copy(check)
check.sort()

for i in range(len(a)):
    if (check[i]-for_answer[0])%gcd != 0 or gcd*a[i]+for_answer[i]<check[-1]:
        print(-1)
        exit()

answer = 10**20
for i in range(len(for_answer)):
    answer = min(answer, for_answer[i]+gcd*a[i])

max_count = 0
for i in range(len(check)):
    max_count += (answer - check[i])//gcd

print(max_count)

