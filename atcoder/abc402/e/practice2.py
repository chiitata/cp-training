n, x = map(int, input().split())
s = [0 for _ in range(n)]
c = [0 for _ in range(n)]
p = [0 for _ in range(n)]
for i in range(n):
    s[i], c[i], p[i] = map(int, input().split())
    p[i] /= 100


# 残りはX円で解いた問題はNの時
dp = [[0 for _ in range(x+1)] for _ in range(1 << n)]

# 残りのお金のループ
for i in range(x+1):
    # 解いた問題のループ
    for j in range(1<<n):
        # 解く問題のループ
        for k in range(n):
            # 残金
            ii = i -c[k]
            # その問題を解いているかいないのか
            jj = j | (1 << k)
            if ii < 0 or jj == j:
                continue
            # 問題にとりかかった後＝正解確率×（もらえるお金＋その問題をすでに解いたDP）＋不正解確率×（その問題をまだ解けていないDP）
            val = p[k]*(s[k]+dp[jj][ii]) + (1-p[k])*dp[j][ii]
            dp[j][i] = max(val, dp[j][i])

print(dp[0][x])