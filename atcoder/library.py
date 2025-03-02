"""itertools.chain.from_iterable の概要
目的: itertools.chain.from_iterable(iterable) は、入れ子になった（ネストされた）反復可能オブジェクトの要素を1つの連続した反復可能オブジェクトとして展開します。"""

"""forループを逆順で回す
1. reversedを使う
2. range(スタート, ストップ, 公差)"""

"""del my_list	リスト自体を削除
my_list.clear()	リストを空にする（要素を全削除）
my_list.remove(value)	指定値を削除（最初の一致のみ）
del my_list[index]	指定インデックスの要素を削除
my_list.pop(index)	指定インデックスの要素を削除して返す
リスト内包表記 / filter()	条件に合致しない要素を削除
list(set(my_list))	重複を削除"""

class unionfind:
    def __init__(self, n):
        self.n = n
        self.par = [-1] * (n+1)
        self.size = [1] * (n+1)
    def root(self, x):
        while self.par[x] != -1:
            x = self.par[x]
        return x
    def unite(self, u, v):
        rootu = self.root(u)
        rootv = self.root(v)
        if rootu != rootv:
            if self.size[rootu] < self.size[rootv]:
                self.par[rootu] = rootv
                self.size[rootv] += self.size[rootu]
            else:
                self.par[rootv] = rootu
                self.size[rootu] += self.size[rootv]
    def same(self, u, v):
        return self.root(u) == self.root(v)