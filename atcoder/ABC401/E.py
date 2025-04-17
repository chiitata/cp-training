# この問題は質問に答えるすなわち頂点1から辺をたどって到達できる頂点の集合が頂点1, 頂点2, ..頂点kのちょうどk個
# からなるようにできるのか答えるパートと条件をみたすことができるときの消すべき頂点の数を求めるパート
# クラスunion-find
# same(x, y)：x, yが同じ成分に所属しているか判定
# merge(x, y)：x, yが同じ成分に結合する
# find(x)：xの属するグループの代表を探す
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # 路圧縮
            x = self.parent[x]
        return x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def merge(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False
        if self.size[x_root] < self.size[y_root]:
            x_root, y_root = y_root, x_root
        self.parent[y_root] = x_root
        self.size[x_root] += self.size[y_root]
        return True


# connected_components	現時点で存在する連結成分の数
# already_connected	頂点 i 以降で、既に前の頂点と隣接している頂点にフラグを立てる
# to_be_erased	「今後追加予定の頂点のうち、すでに今までの頂点と隣接しているもの」の個数

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

edge = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

connected_conponents = 0
already_connected = [False]*n
to_bo_erased = 0

uf = DSU(n)
for i in range(n):
    connected_conponents += 1

    if already_connected[i]:
        to_bo_erased -= 1

    for j in edge[i]:
        if j < i:
            if not uf.same(i, j):
                uf.merge(i, j)
                connected_conponents -= 1
        else:
            if not already_connected[j]:
                to_bo_erased += 1
            already_connected[j] = True
            
    if connected_conponents == 1:
        print(to_bo_erased)
    else:
        print(-1)