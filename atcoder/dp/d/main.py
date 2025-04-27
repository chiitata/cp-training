# !/usr/bin/env python3

n, W = map(int, input().split())

w = [0 for _ in range(n)]
v = [0 for _ in range(n)]
# Knapsack問題二個目の引数で合計がちょうどWという制約をつけている
for i in range(n):
    w[i], v[i] = map(int, input().split())
# リストの説明第一引数には重さの合計、第二引数には選択可能な商品の合計数
# インデックスは商品に合わせている
dp = [[-10**9 for _ in range(W+1)] for _ in range(n+1)]
# 初期化０商品選択可能０グラムのでの価値の合計の最大値は０
dp[0][0] = 0
# こちらのループは選ぶことのできる商品を決めるループ
for i in range(n):
    # こちらのループは全探索するためのループ
    for j in range(W+1):
        # まずは商品数を一つ増やしても重さが変わらない＝その商品が選ばれなかった
        dp[i+1][j] = max(dp[i][j], dp[i+1][j])
        # もし現在の位置から次に選択可能になる物の重さの合計がWを超えなかったら
        if j+w[i] <= W:
            dp[i+1][j+w[i]] = max(dp[i+1][j+w[i]], dp[i][j]+v[i])

print(max(dp[n]))
# answer = 0
# for i in range(W, -1, -1):
#     answer = max(answer, dp[n][i])
# print(answer)

# ミス
# 初期化を忘れていたdp[0][0]=0
# 商品を増やしても重さが変わらない＝その商品が選ばれなかったときにdp[i+1][j]=dp[i][j]としてしまったこれでは仮にdp[i+1][j]に何か重さが入っているときに更新してしまう
# インデックスを決めるときにどう決めるべきか迷った結論dp[i][j] iはi番目の商品の中から選ぶ jは重さ合計がjになるように選ぶ
# jは合計の重さがj以下という考え方もできた