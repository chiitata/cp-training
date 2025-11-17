##### segfunc#####
# 2つのノード (count, sum) タプルをマージ（合計）する関数
def segfunc(p1, p2):
    # p1 = (count1, sum1), p2 = (count2, sum2)
    return (p1[0] + p2[0], p1[1] + p2[1])
#################

##### ide_ele#####
# (count, sum) タプルの単位元
ide_ele = (0, 0)
#################

class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])
    
    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = self.segfunc(res, self.tree[r])
            l >>= 1
            r >>= 1
        return res

# --- ここからメイン処理 ---

# A[i] の取りうる最大値
V_MAX = 500000

n, q = map(int, input().split())
a = list(map(int, input().split())) # 元の配列 (更新追跡用)

# --- セグメント木の構築 ---
# 値 0 から V_MAX までの (count, sum) を集計

# 1. 各値の個数を集計
counts = [0] * (V_MAX + 1)
for val in a:
    counts[val] += 1

# 2. セグメント木の初期配列 (init_val) を作成
#    長さは V_MAX + 1
init_val = []
for v in range(V_MAX + 1):
    if counts[v] > 0:
        # (個数, 値 * 個数)
        init_val.append((counts[v], v * counts[v]))
    else:
        init_val.append(ide_ele) # (0, 0)

# 3.「値ベース」のセグメント木を構築
# tree.tree[tree.num + v] が (値 v の個数, 値 v の合計) を保持
tree = SegTree(init_val, segfunc, ide_ele)

query_line = []
# --- クエリ処理 ---
for _ in range(q):
    query_line.append(list(map(int, input().split())))
for i in range(q):
    
    if query_line[i][0] == 1:
        # --- クエリ 1: 更新 ---
        _, x, y = query_line[i]
        x -= 1 # 問題文は 1-indexed のため 0-indexed に
        
        old_y = a[x] # 更新前の値
        new_y = y    # 更新後の値
        
        if old_y == new_y:
            continue
            
        a[x] = new_y # 元の配列を更新
        
        # セグメント木（値ベース）を更新
        
        # old_y の情報を木から減らす
        # k = old_y がセグメント木のインデックスに対応
        old_count, old_sum = tree.tree[tree.num + old_y]
        tree.update(old_y, (old_count - 1, old_sum - old_y))
        
        # new_y の情報を木に増やす
        new_count, new_sum = tree.tree[tree.num + new_y]
        tree.update(new_y, (new_count + 1, new_sum + new_y))
        
    else:
        # --- クエリ 2: 合計 (ここが続き) ---
        _, l, r = query_line[i]
        
        if l > r:
            # l > r なら、max(l, min(r, A[i])) は常に l
            print(n * l)
            continue
        
        total_ans = 0
        
        # 1. A[i] < l (値の範囲 [0, l-1])
        #    → これらは全て l としてカウントされる
        if l > 0:
            # tree.query(0, l) は [0, l) すなわち [0, l-1] の閉区間の (count, sum)
            count_low, _ = tree.query(0, l)
            total_ans += count_low * l
        
        # 2. l <= A[i] <= r (値の範囲 [l, r])
        #    → これらは A[i] の合計値がそのまま使われる
        # tree.query(l, r + 1) は [l, r+1) すなわち [l, r] の閉区間の (count, sum)
        _, sum_mid = tree.query(l, r + 1)
        total_ans += sum_mid
        
        # 3. A[i] > r (値の範囲 [r+1, V_MAX])
        #    → これらは全て r としてカウントされる
        if r < V_MAX:
            # tree.query(r + 1, V_MAX + 1) は [r+1, V_MAX+1) 
            # すなわち [r+1, V_MAX] の閉区間の (count, sum)
            count_high, _ = tree.query(r + 1, V_MAX + 1)
            total_ans += count_high * r
            
        print(total_ans)