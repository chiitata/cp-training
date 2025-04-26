# !/usr/bin/env python3

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
            result[self.leader(i).append(i)]
        return [r for r in result if r != []]
    
n, m = map(int, input().split())

UF = UnionFind(n+1)

count = [0]*(n+1)
for i in range(m):
    a, b = map(int, input().split())
    if UF.same(a, b) == True:
        print('No')
        exit() 
    UF.merge(a, b)
    count[a] += 1
    count[b] += 1
    if count[a] == 3 or count[b] == 3:
        print('No')
        exit() 
else:
    print('Yes')
