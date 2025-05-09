# !/usr/bin/env python3
# どうすればいいかわからないこれはdpの問題であるが
# 仮にBを選んで最大になる事象があった場合一個前の最大値がBを選んで最大だった場合
# Bを選ばなかった最大値すなわちA, Cを選んで最大になったものを考えればよい
# ということは最大値と二番目の最大値を保持しておけば大丈夫なのか？
# Bを選んで最大値ということはACどちらを選んでいても構わないからそれまでに二番目に大きい方から考えればよい
# ではどのようにして二番目に最大を保持するのか？
# もう一つ配列を準備するのでもよいが
n = int(input())
dp = [[0 for _ in range(3)] for _ in range(n)]
p = list(map(int, input().split()))
dp[0][0] = p[0]
dp[0][1] = p[1]
dp[0][2] = p[2]
for i in range(1, n):
    a = list(map(int, input().split()))
    dp[i][0] = max(dp[i-1][1]+a[0], dp[i-1][2]+a[0])
    dp[i][1] = max(dp[i-1][0]+a[1], dp[i-1][2]+a[1])
    dp[i][2] = max(dp[i-1][0]+a[2], dp[i-1][1]+a[2])

print(max(dp[n-1][0], dp[n-1][1], dp[n-1][2]))