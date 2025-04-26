# !/usr/bin/env python3
# これはUnionFindの問題らしいがあまりよくわからない
# A_iとA_N+1-iがすべてのNについて成り立つときAが回分ということができる
# 仮に1を3に変更した場合1と3をmergeすることに等しいと考えることができる
# そしてA_iとA_N+1-iが同じ木に含まれればそれは同一の文字と考えることができる
# すなわち何回のmergeで全ての木がsameになるかを考えればよい
# でも最小回数ってどうやって求めるの？
# 最小回数を求めるときはDP？
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
            result[[self.leader(i)].append(i)]
        return [r for r in result if r != []]
    
answer = 0
n = int(input())
a = [0] + list(map(int, input().split()))
# これは最初から調べて行ってUF.same()出なければmergeしていけばいいのではss
uf = UnionFind((2*(10**6))+1)
for i in range(1, n//2+1):
    if uf.same(a[i], a[n+1-i]) == False:
        uf.merge(a[i], a[n+1-i])
        answer += 1

print(answer)