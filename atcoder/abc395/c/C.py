n = int(input())
a = list(map(int, input().split()))

min_index = {}

min_gap = n+1
for i, num in enumerate(a):
    if num in min_index:
        gap = i - min_index[num]
        min_gap =min(min_gap, gap)
    min_index[num]=i

if min_gap == n+1:
    print(-1)
else:
    print(min_gap+1)

