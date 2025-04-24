#　これはDPの問題っぽい気がする
# (0, 0)を壁蹴り回数0回に設定して、もし(i, j)が#ならば(i-1, j)と(i, j-1)の小さいほうの値を挿入

H, W = map(int, input().split())

s = [['#' for _ in range(W+2)]]

# 受け取り
for i in range(H):
    t = ['#'] + list(input()) + ['#']
    s.append(t)

a, b, c, d = map(int, input().split())

# より左の方をスタートにするスタートとゴールの上下関係によってこれから条件分岐する必要がある
if a<=c:
    start_x = a
    start_y = b
    end_x = c
    end_y = d
elif a>c:
    start_x = c
    start_y = d
    end_x = a
    end_y = b

dp = [[10**9 for _ in range(W+2)]]
f = [10**9 for _ in range(W+2)]
dp.append(f)
for i in range(H):
    t = [10**9] + [0 for _ in range(W)] + [10**9]
    dp.append(t)
dp.append(f)

# 条件分岐まずその位置が#か.であるかを調べる
# もし#であればもうさらに一個前がどうなっているかを調べる
# この時にリストの外に出てしまう問題が発生
if c == d:
elif c > d:
elif c < d:

