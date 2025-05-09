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

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent_size = [-1]*n
    def leader(self, a):
        if self.parent_size[a]<0: 
            return a
        self.parent_size[a] = self.leader(self.parent_size[a])
        return self.parent_size[a]
    def merge(self, a, b):
        x, y= self.leader(a), self.leader(b)
        if x == y:
            return
        if abs(self.parent_size[x])<abs(self.parent_size[y]): 
            x, y = y, x
        self.parent_size[x] += self.parent_size[y]
        self.parent_size[y] = x
    def same(self, a, b):
        return self.leader(a) == self.leader(b)
    def size(self, a):
        return abs(self.parent_size[self.leader[a]])
    def groups(self):
        result = [[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]