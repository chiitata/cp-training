import sys

input = sys.stdin.readline
MOD = 10**9

n, k = map(int, input().split())
a = [1 for i in range(n+1)]

s = k
for i in range(k, n+1):
    a[i] = s
    s -= a[i-k]
    s += a[i]
    s %= 10**9

print(a[n])