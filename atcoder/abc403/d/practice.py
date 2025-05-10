import sys
from collections import defaultdict

input = sys.stdin.readline

n, d = map(int, input().split())
a = list(map(int, input().split()))
freq = defaultdict(int)
groups = defaultdict(list)
if d == 0:
    print(n-len(set(a)))
    exit()
for i in a:
    freq[i] += 1
for i in freq:
    groups[i%d].append(i)
max_keep = 0
for i, vs in groups.items():
    vs.sort()
    # dp1は一個前を選んだ時
    # dp2は一個前を選ばなかったとき
    dp1 = dp2 = 0
    prev = None
    for v in vs:
        w = freq[v]
        if prev is not None and v == prev + d:
            ndp1 = dp2 + w
            ndp2 = max(dp1, dp2)
        else:
            ndp1 = max(dp1, dp2) + w
            ndp2 = max(dp1, dp2)
        prev = v
        dp1, dp2 = ndp1, ndp2
    max_keep += max(dp1, dp2)
print(n-max_keep)