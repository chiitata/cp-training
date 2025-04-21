# 入力読み込み
N, M = map(int, input().split())
adj = [ [] for _ in range(N+1) ]
rem = [0]* (M+1)

for j in range(1, M+1):
    Ks = list(map(int, input().split()))  # 先頭が K_j, 以降が A_{j,1}...A_{j,K_j}
    K = Ks[0]
    rem[j] = K
    for x in Ks[1:]:
        adj[x].append(j)

B = list(map(int, input().split()))  # 長さ N

cnt = 0
ans = [0]*N

for i, b in enumerate(B, start=1):
    for j in adj[b]:
        rem[j] -= 1
        if rem[j] == 0:
            cnt += 1
    ans[i-1] = cnt

print(*ans, sep="\n")
