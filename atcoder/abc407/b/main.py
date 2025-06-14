# !/usr/bin/env python3

x, y = map(int, input().split())
dice = [1, 2, 3, 4, 5, 6]
x_ans = 0
for i in dice:
    for j in dice:
        if i + j < x and abs(i-j) < y:
            x_ans += 1

print((36-x_ans)/36)