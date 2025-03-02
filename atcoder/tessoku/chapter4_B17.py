#2/24〇
n = int(input())
h = list(map(int, input().split()))

dp = [None]*(n+1)
dp[1] = 0
dp[2] = abs(h[1]-h[0])
for i in range(3, n+1):
    dp[i] = min(dp[i-1]+abs(h[i-1]-h[i-2]), dp[i-2]+abs(h[i-1]-h[i-3]))

answer = []
pos = n
answer.append(pos)
while True:
    if pos == 1:
        break
    if dp[pos] - dp[pos-1] == abs(h[pos-1]-h[pos-2]):
        pos -= 1
        answer.append(pos) 
    elif dp[pos] - dp[pos-2] == abs(h[pos-1]-h[pos-3]):
        pos -= 2
        answer.append(pos) 


answer.reverse()
print(len(answer))
for i in answer:
    print(i, end=' ')

print()
