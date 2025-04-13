import math

N = int(input())
count = 0

max_b = math.isqrt(N)
# b を奇数のみでループ
for b in range(1, max_b + 1, 2):
    # b^2が上限を超えない場合のみ
    X = b * b
    limit = N // X  # 2^a の上限
    # limit >= 2 でなければ a>=1 を満たすことはできない
    if limit >= 2:
        # floor(log2(limit)) を求める (limit.bit_length()-1 は floor(log2(limit)) に一致)
        a_max = limit.bit_length() - 1
        count += a_max

print(count)
