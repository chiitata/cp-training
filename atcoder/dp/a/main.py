# !/usr/bin/env python3

# この問題はDP足場iに行くために最小のコストを求めていく
n = int(input())
step = list(map(int, input().split()))
step_count = [float('inf')] * (n)
step_count[0] = 0
for i in range(n):
    if i + 1 < n:
        diff_1 = abs(step[i+1]-step[i])
        step_count[i+1] = min(step_count[i+1], step_count[i]+diff_1)
        if i+2<n:
            diff_2 = abs(step[i+2]-step[i])
            step_count[i+2] = min(step_count[i+2], step_count[i]+diff_2)

print(step_count[-1])
