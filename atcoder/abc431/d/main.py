#!/usr/bin/env python3
import sys

# 高速な入力を設定
input = sys.stdin.readline

n = int(input())

vals = []           # (重さ, 価値の差) を格納
base_happiness = 0  # 全て体につけたときの嬉しさ (sum(B))
w_sum = 0           # 全ての重さの合計 (sum(W))

for _ in range(n):
    wi, hi, bi = map(int, input().split())
    vals.append((wi, hi - bi))
    base_happiness += bi
    w_sum += wi

capacity = w_sum // 2

dp = [-float('inf')] * (capacity + 1)
dp[0] = 0 # 重さ0のとき、価値の差も0
for wi, val_diff in vals:
    
    for v in range(capacity, wi - 1, -1):
        
        if dp[v - wi] != -float('inf'):
            
            dp[v] = max(dp[v], dp[v - wi] + val_diff)

max_diff = max(dp)

print(base_happiness + max_diff)