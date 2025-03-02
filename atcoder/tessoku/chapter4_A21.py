n = int(input())
p = [None]*n
a = [None]*n
for i in range(n):
    p[i], a[i] = map(int, input().split())

dp = [[None for _ in range(n+1)]for _ in range(n+1)]
dp[1][n] = 0
for i in (1, n):
    for j in range(i+1):
        if 
        dp[j+1][n-(i-j)]