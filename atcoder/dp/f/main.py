# !/usr/bin/env python3

# これはDPの問題である
# キーポイント indexが二次元になったDP　復元
# まず二次元配列を用意して文字列二つの文字列sとtのi文字目とj文字目が一致すれば
s = [None]+list(input())
t = [None]+list(input())
dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]

def in_grid(x, y):
    return 0<=x<len(s) and 0<=y<len(t)
for i in range(1, len(s)):
    for j in range(1, len(t)):
        if s[i] == t[j]:
            dp[i][j] = max(dp[i-1][j-1]+1, dp[i-1][j], dp[i][j-1])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# 復元パート
answer = []
# i,j は dp の末尾
while i > 0 and j > 0:
    # まず文字一致をチェック
    if s[i] == t[j]:
        answer.append(s[i])
        i -= 1
        j -= 1
    # 文字が合わない or 一致部から来たわけでなければ
    # dp[i][j] が上から来たのか左から来たのかを比較
    elif dp[i-1][j] >= dp[i][j-1]:
        i -= 1
    else:
        j -= 1

# 最後に前から逆順で一度だけ reverse
answer.reverse()
print(''.join(answer))

