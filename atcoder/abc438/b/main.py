# !/usr/bin/env python3

import sys
input = sys.stdin.readline

def LI(): return list(map(int, input().split()))
def II(): return int(input())

n, m = map(int, input().split())

# int() を使わずに、文字列として受け取る
s_raw = input().strip()
t_raw = input().strip()

# 文字列のまま 1 文字ずつ整数に変換してリスト化する
s = [int(d) for d in s_raw]
t = [int(d) for d in t_raw]

def count(s, t):
    if s == t:
        return 0
    elif s > t:
        return s-t
    elif s < t:
        return 10 + s - t

answer = 10000000000
for i in range(len(s)-len(t)+1):
    tmp = 0
    for j in range(len(t)):
        tmp += count(s[i+j], t[j])
    answer = min(answer, tmp)

print(answer)
