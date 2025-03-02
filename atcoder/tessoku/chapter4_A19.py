n, q = map(int, input().split())

w = []
for i in range(n):
    w1 = list(map(int, input().split()))
    w.append(w1)

dp = [([0]+[None for _ in range(q)]) for _ in range(n+1)]

dp[0][0] = 0
dp[1][0] = 0
dp[1][w[0][0]] = w[0][1]
for i in range(1, n):
    weight = w[i][0]
    value = w[i][1]
    for j in range(q+1):
        if dp[i][j] != None and i<n:
            if dp[i+1][j] == None:
                dp[i+1][j] =dp[i][j]
            else:
                dp[i+1][j] = max(dp[i+1][j],dp[i][j])
            if j+weight<= q:
                if dp[i+1][j+weight] == None:
                    dp[i+1][j+weight] = dp[i][j] + value
                else:
                    dp[i+1][j+weight] = max(dp[i+1][j+weight], dp[i][j] + value)
    
answer = []
for i in range(q+1):
    if dp[n][i] != None:
        answer.append(dp[n][i])
    
print(max(answer))
