s = [None]+list(input())
t = [None]+list(input())
dp = [[0 for _ in range(len(t))]for _ in range(len(s))]
dp2 = [[0 for _ in range(len(t))]for _ in range(len(s))]
renzoku = 0
count = []
for i in range(1, len(s)):
    for j in range(1, len(t)):
        if s[i] == t[j]:
            dp[i][j] = max(dp[i-1][j-1]+1, dp[i-1][j], dp[i][j-1])
            if dp[i][j] == dp[i-1][j-1]+1:
                dp2[i][j] = dp2[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp)
a = 0
for i in count:
    if i > 1:
        a += i-1
print(a)