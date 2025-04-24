# この問題はbitDPの問題
N, X = map(int, input().split())
S = [0] * N
C = [0] * N
P = [0] * N
for i in range(N):
    S[i], C[i], P[i] = map(int, input().split())
    P[i] /= 100
d = [[0.0 for _ in range(X + 1)] for _ in range(1 << N)]
# お金をいくら使うのかのループ
for x in range(X + 1):
    # どの問題を解いたことがあるのかのループ
    for s in range(1 << N):
        # 解く問題のループ
        for i in range(N):
            # 残金
            xx = x - C[i]
            # その問題を解いているのかいないのか
            ss = s | (1 << i)
            # すでに解いたことがある
            # たとえば解く問題を010とした時に011が解いたことのある問題なら一致するs==ss
            # または解こうとすると残金が０以下になってしまって挑戦できない
            if xx < 0 or s == ss:
                continue
            # 解いたことがなければその問題に取り組んだことにより結果を考える
            val = P[i] * (d[ss][xx] + S[i]) + (1 - P[i]) * d[s][xx]
            # 最大値を考える
            d[s][x] = max(d[s][x], val)
print(d[0][X])
# 結構多重ループになってしまっているけど大丈夫な模様