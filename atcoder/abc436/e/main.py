import sys

# 再帰深度の制限を増やす（念のため）
sys.setrecursionlimit(10**6)

def solve():
    # 入力受け取り
    # N: 整数の数
    # P: スペース区切りの整数列
    # input() は適宜 sys.stdin.readline 等に置き換えてください
    try:
        line1 = sys.stdin.readline()
        if not line1:
            return
        N = int(line1.strip())
        
        line2 = sys.stdin.readline()
        if not line2:
            return
        P = list(map(int, line2.split()))
    except ValueError:
        return

    # 0-indexed に調整（Pの中身を 0 ~ N-1 にする）
    P = [x - 1 for x in P]

    visited = [False] * N
    ans = 0

    # 全ての要素についてサイクルを確認
    for i in range(N):
        if visited[i]:
            continue
        
        # 新しいサイクルを発見
        current_node = i
        cycle_len = 0
        
        # サイクルを一周するまで探索
        while not visited[current_node]:
            visited[current_node] = True
            current_node = P[current_node]
            cycle_len += 1
        
        # 長さ L のサイクルから 2 点を選ぶ組み合わせは L * (L-1) / 2 通り
        ans += cycle_len * (cycle_len - 1) // 2

    print(ans)

if __name__ == '__main__':
    solve()