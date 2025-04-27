#!/usr/bin/env python3
import sys

input = sys.stdin.readline

class XNode:
    __slots__ = ('ch','term')
    def __init__(self):
        self.ch = {}
        self.term = False

class YNode:
    __slots__ = ('ch','sub','marked')
    def __init__(self):
        self.ch = {}
        self.sub = 0      # 部分木の未マーク Y カウント
        self.marked = False  # 部分木全体が既にマーク済みか

# Trie のルート
x_root = XNode()
y_root = YNode()

# グローバルカウンタ
total_Y = 0
bad_Y   = 0

def add_X(s):
    node = x_root
    # ★ここで any-prefix-in-X をチェックして early return★
    for c in s:
        # 途中で term=True → 既に短い接頭辞が X にある
        if node.term:
            return 0
        if c not in node.ch:
            node.ch[c] = XNode()
        node = node.ch[c]
    # 完全一致の重複追加もスキップ
    if node.term:
        return 0
    node.term = True

    # 以下、もともとの Y-trie 部分木マーク処理…
    path = [y_root]
    yn = y_root
    for c in s:
        if c not in yn.ch:
            return 0
        yn = yn.ch[c]
        path.append(yn)

    k = yn.sub
    if k == 0:
        return 0
    for p in path:
        p.sub -= k
    yn.marked = True
    return k


def add_Y(s):
    """ X-trie で事前検出。マークすべきなら True, さもなくば Y-trie に挿入して False """
    # 空文字もチェック
    xn = x_root
    if xn.term:
        return True
    for c in s:
        if c not in xn.ch:
            break
        xn = xn.ch[c]
        if xn.term:
            return True

    # 未マーク Y として Y-trie に登録
    yn = y_root
    yn.sub += 1
    for c in s:
        # 部分木全体が以前マーク済かどうかに関わらず、新文字列は未マーク扱い
        if c not in yn.ch:
            yn.ch[c] = YNode()
        yn = yn.ch[c]
        yn.sub += 1
    return False

q = int(input())
out = []

for _ in range(q):
    t, s = input().split()
    t = int(t)
    if t == 1:
        # X に追加
        k = add_X(s)
        bad_Y += k
    else:
        # Y に追加
        total_Y += 1
        if add_Y(s):
            bad_Y += 1

    out.append(str(total_Y - bad_Y))

sys.stdout.write("\n".join(out))
print()

