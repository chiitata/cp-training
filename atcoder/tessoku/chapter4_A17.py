n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [0]*(n+1)
dp[1] = 0
dp[2] = a[0]
for i in range(3, n+1):
    dp[i] = min(dp[i-1]+a[i-2], dp[i-2]+b[i-3])

answer = []
pos1 = n
while pos1>0:
    if pos1 == 2:
        answer.append(2)
        answer.append(1)
        break
    elif pos1 == 1:
        answer.append(1)
        break
    if dp[pos1]-dp[pos1-1] == a[pos1-2]:
        answer.append(pos1)
        pos1 -= 1
    elif dp[pos1]-dp[pos1-2] == b[pos1-3]:
        answer.append(pos1)
        pos1 -= 2

print(len(answer))
for i in range(len(answer)-1, -1, -1):
    print(answer[i], end=' ')
print()
