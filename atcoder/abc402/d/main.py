import sys
from collections import Counter

input = sys.stdin.readline
N, M = map(int, input().split())
cnt = Counter()

for _ in range(M):
    a, b = map(int, input().split())
    # 問題の番号は 1..N なので 0..N-1 に変換し，和を mod N
    s = ((a) + (b)) % N
    cnt[s] += 1

total_pairs = M * (M-1) // 2
parallel_pairs = sum(v*(v-1)//2 for v in cnt.values())
print(total_pairs - parallel_pairs)