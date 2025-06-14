import sys
from itertools import product


def main():
    H, W = map(int, sys.stdin.readline().split())
    A = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

    possible_domino = [0]  # 盤面のビット表現
    domino_vertical = (1 << W) + 1
    domino_horizontal = 3

    for i in range(H):
        for j in range(W):
            bit = i * W + j
            tmp = []
            for b in possible_domino:
                # 横に置ける場合
                # not (b & (domino_horizontal << bit)) &演算の結果が0すなわちかぶりがない
                if j + 1 < W and not (b & (domino_horizontal << bit)):
                    tmp.append(b | (domino_horizontal << bit))
                # 縦に置ける場合
                if i + 1 < H and not (b & (domino_vertical << bit)):
                    tmp.append(b | (domino_vertical << bit))
            possible_domino += tmp

    ans = 0
    for b in possible_domino:
        now = 0
        for i in range(H):
            for j in range(W):
                bit = i * W + j
                if not ((b >> bit) & 1):  # ドミノが置かれていないマス
                    now ^= A[i][j]
        ans = max(ans, now)

    print(ans)

if __name__ == "__main__":
    main()