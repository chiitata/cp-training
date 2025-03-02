#2/24〇
n = int(input())
h = list(map(int, input().split()))

dp = [None]*(n+1)
dp[1] = 0
dp[2] = abs(h[1]-h[0])
for i in range(3, n+1):
    dp[i] = min(dp[i-1]+abs(h[i-1]-h[i-2]), dp[i-2]+abs(h[i-1]-h[i-3]))

print(dp[n])