import sys

# 入力を高速に受け取るための工夫（大量のテストケース対策）
input = sys.stdin.readline

def solve():
    # 最初の行の T (テストケース数) を取得
    try:
        line = input().split()
        if not line: return # 空行対策
        T = int(line[0])
    except ValueError:
        return

    for _ in range(T):
        # N: 目標数, H: 初期高度
        line = input().split()
        if not line: break
        N, H = int(line[0]), int(line[1])

        # 現在可能な高度の範囲 (最初は H〜H)
        now_min = H
        now_max = H
        
        # 前回の時刻
        prev_t = 0
        
        possible = True
        
        for _ in range(N):
            t, l, u = map(int, input().split())
            
            # すでに不可能とわかっていても、入力だけは最後まで読み飛ばす必要がある
            if not possible:
                continue
                
            # 経過時間を計算
            dt = t - prev_t
            
            # 1. 時間経過分だけ範囲を広げる
            # (上に dt 行ける、下に dt 行ける)
            now_max += dt
            now_min -= dt
            
            # 2. 目標の範囲との「共通部分」をとる
            # 上限は「今の限界」と「目標の上限」の小さい方
            now_max = min(now_max, u)
            # 下限は「今の限界」と「目標の下限」の大きい方
            now_min = max(now_min, l)
            
            # 3. 矛盾チェック
            # 下限が上限を超えてしまったら、その範囲には存在できない＝不可能
            if now_min > now_max:
                possible = False
            
            # 時刻を更新
            prev_t = t

        if possible:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    solve()