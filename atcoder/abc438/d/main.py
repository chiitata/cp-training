import sys

def solve():
    # 入力の高速化
    input = sys.stdin.read().split()
    N = int(input[0])
    A = list(map(int, input[1:N+1]))
    B = list(map(int, input[N+1:2*N+1]))
    C = list(map(int, input[2*N+1:3*N+1]))

    inf = float('inf')
    dp0 = -inf
    dp1 = -inf
    dp2 = -inf

    dp0 = A[0]

    for i in range(1, N):
        if dp1 != -inf:
            dp2 = max(dp2, dp1) + C[i]
        
        if dp0 != -inf:
            dp1 = max(dp1, dp0) + B[i]
            
        dp0 = dp0 + A[i]

    print(dp2)

solve()