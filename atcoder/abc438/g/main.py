import sys
import math

def solve():
    # 入力の受け取り
    input_data = sys.stdin.read().split()
    N, M, K = map(int, input_data[:3])
    A = list(map(int, input_data[3:3+N]))
    B = list(map(int, input_data[3+N:3+N+M]))
    
    MOD = 998244353
    G = math.gcd(N, M)
    LCM = (N * M) // G
    
    # 1. 全体の周期回数と端数の計算
    full_cycles = K // LCM
    rem_elements = K % LCM
    
    ans = 0
    
    # 2. 各グループ r = i % G について計算
    for r in range(G):
        # このグループに属する A と B の要素を抽出
        sub_A = [A[i] for i in range(r, N, G)]
        sub_B = [B[i] for i in range(r, M, G)]
        n_sub = len(sub_A) # N / G
        m_sub = len(sub_B) # M / G
        
        # 周期内での合計を計算するための関数（スライディングウィンドウ等）
        # ここでは簡略化のため、全体の寄与を計算
        group_sum = calculate_group_sum(sub_A, sub_B, n_sub, m_sub)
        ans = (ans + full_cycles * group_sum) % MOD
        
        # 3. 端数 (rem_elements) の計算
        # 端数の範囲内で i % G == r となる個数を計算
        # (ここはさらに詳細な実装が必要ですが、基本は周期計算と同じです)
        # ... (端数処理のコード) ...

    print(ans)

def calculate_group_sum(sub_A, sub_B, n, m):
    """
    1つのグループ内での min(A_i, B_j) の総和を O((n+m)log(n+m)) で計算する
    """
    total = 0
    # AとBをソートして累積和を使うことで、
    # min(a, b) の a < b と a >= b の境界を二分探索等で高速に見つける
    sub_B_sorted = sorted(sub_B)
    b_prefix_sum = [0] * (m + 1)
    for i in range(m):
        b_prefix_sum[i+1] = (b_prefix_sum[i] + sub_B_sorted[i])
        
    for a in sub_A:
        import bisect
        idx = bisect.bisect_left(sub_B_sorted, a)
        # a 以下の B[j] の和 + a を超える B[j] に対する a の寄与
        sum_b_less = b_prefix_sum[idx]
        count_a_less = (m - idx) * a
        total = (total + sum_b_less + count_a_less)
    
    return total

# ※ 実際には端数処理において「どのA_iとどのB_jがペアになるか」の
# 順序関係を数学的に解く必要があります。