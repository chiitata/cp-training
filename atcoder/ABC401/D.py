# まず最初に与えられた文字列sの中にある'o'の隣の'?'を
# 全て'.'に置き換える(この作業を忘れていた)
# その後sの中の'o'の数をできる限り多くする
# その後'?'が偶数個連続するところはそのままで
# 奇数個連続するところは一通りに決まる

n, k =map(int, input().split())
import copy

s = list(input())
m = 0
# 答えのためのs
s_for_answer = copy.deepcopy(s)

if n == 1:
    if k == 0:
        print(".")
        exit()
    elif k == 1:
        print("o")
        exit()
# S内部でoに隣接している?は全て.に置き換える
for i in range(len(s)):
    if 1<= i <= n-2:
        if s[i] == '?':
            if s[i-1] == 'o' or s[i+1] == 'o':
                s[i] = '.'
    elif i == 0:
        if s[i] == '?':
            if s[i+1] == 'o':
                s[i] = '.'
    elif i == len(s) - 1:
        if s[i] == '?':
            if s[i-1] == 'o':
                s[i] = '.'

# 結果を出力する際に使用
s_copy = copy.deepcopy(s)

# oの数を数える
counter_o = s.count('o')

# Sにもともと含まれるoの数が問題でしてされたKと等しい場合は?を全て.に置き換え
if counter_o == k:
    t = [ch.replace('?', '.') for ch in s]
    print("".join(t))
    exit()

# それ以外の場合、すなわちもともとSに含まれるoの数とKが一致しない場合
# この時はSの中のoの数を最大にしてみる
for i in range(len(s)):
    if i == 0:
        if s[i] == '?':
            s[i] = 'o'
    elif i == len(s)-1:
        if s[i] == '?':
            s[i] = 'o'
    else:
        if s[i] == '?':
            if s[i-1] != 'o':
                s[i] = 'o'
            else:
                s[i] = '.'

# S内部のoの数を最大にしてみて何個になるか計算
max_o = s.count('o')

# ?が何個連続するか計算するよう
def count_question(t, i, n):
    count = 1
    while i + count<= n-1:
        if t[i+count] == '?':
            count += 1
        else:
            break
    return count

if max_o == k:
    i = 0
    while i <= n-1:
        if s_copy[i] == '?':
            count = count_question(s_copy, i, n)
            if count % 2 == 0:
                i += count
            elif count % 2 == 1:
                for j in range(i, i+count):
                    if j == i:
                        s_copy[j] = 'o'
                    elif s_copy[j-1] == 'o':
                        s_copy[j] = '.'
                    elif s_copy[j-1] == '.':
                        s_copy[j] = 'o'
                i += count
            continue
        i += 1
    print("".join(s_copy))
    exit()


if max_o > k:
    print("".join(s_copy))
    exit()


