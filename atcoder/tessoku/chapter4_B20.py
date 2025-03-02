s = [None]+list(input())
t = [None]+list(input())
dp = [[0 for _ in range(len(t))]for _ in range(len(s))]
for i in range(1, len(s)):
    for j in range(1, len(t)):
        if s[i] == t[j]:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]+1, dp[i][j-1]+1)
        else:
            dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)

print(dp[len(s)-1][len(t)-1]+1)