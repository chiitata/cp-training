n, q = map(int, input().split())
a = list(map(int, input().split()))+[0]

dp = [[0 for i in range(q+1)]for j in range(n+1)]

for i in range(n+1):
    t = a[i]
    if i == 0:
        dp[0][0] = 1
        for j in range(q+1):
            if dp[i][j] == 1:
                try:
                    dp[i+1][j] = 1
                    dp[i+1][j+t] = 1
                except IndexError or ValueError:
                    try:
                        dp[i+1][j] = 1
                    except IndexError or ValueError:
                        try:
                            dp[i+1][j+t] = 1
                        except IndexError or ValueError:
                            continue
    else:
        for j in range(q+1):
            if dp[i][j] == 1:
                try:
                    dp[i+1][j] = 1
                    dp[i+1][j+t] = 1
                except IndexError or ValueError:
                    try:
                        dp[i+1][j] = 1
                    except IndexError or ValueError:
                        try:
                            dp[i+1][j+t] = 1
                        except IndexError or ValueError:
                            continue
if dp[n][q] == 1:
    print('Yes')
else:
    print('No')