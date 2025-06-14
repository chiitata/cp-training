def max_monsters(H, M, A, B):
    N = len(A)
    # dp[h][m] = i体目まで生き残れるか
    dp = [[False] * (M + 1) for _ in range(H + 1)]
    dp[H][M] = True

    for i in range(N):
        new_dp = [[False] * (M + 1) for _ in range(H + 1)]
        for h in range(H + 1):
            for m in range(M + 1):
                if not dp[h][m]:
                    continue
                # 行動1：体力を使って戦う
                if h >= A[i]:
                    new_dp[h - A[i]][m] = True
                # 行動2：魔力を使って戦う
                if m >= B[i]:
                    new_dp[h][m - B[i]] = True
        if all(not cell for row in new_dp for cell in row):
            # どの状態でも生き残れなかったらゲーム終了
            return i
        dp = new_dp  # 状態更新
    return N  # 全部倒せた

n, h, m = map(int, input().split())
A = []
B = []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

answer = max_monsters(h, m, A, B)
print(answer)