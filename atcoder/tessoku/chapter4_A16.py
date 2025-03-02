n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp = [None]*(n+1)
for i in range(n):
    if i == 0:
        dp[0] = 0
    elif i == 1:
        dp[i] = a[0]
    else:
        dp[i] = min(dp[i-1]+a[i-1], dp[i-2]+b[i-2])

print(dp[n-1])


