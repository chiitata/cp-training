# どうすれば単純な問題に帰着できるか考える
# ？にできるだけoを入れてみて減らすことは容易なのでどこにoが入るかが重要である
# この際oに隣接する？には必ず.が入ることが分かる
# よって残ったはてな群を考えればよい？の連続数が奇数の場合はoと.の組み合わせはただ一通りに決まる
# しかし偶数の場合は二通り考えらえるので全て？のまま

N, K = map(int, input().split())
s = list(input())

if N == 1:
    if K == 1:
        print('o')
        exit()
    elif K == 0:
        print('.')
        exit()
# sに含まれるoの個数がKとひとしいとき
s_count = s.count('o')
if s_count == K:
    for i in range(N):
        if s[i] == '?':
            s[i] = '.'
    print("".join(s))
    exit()

# まずは先頭と最後の処理をする
if s[0] == '?':
    if s[1] == 'o':
        s[0] = '.'

if s[N-1] == '?':
    if s[N-2] == 'o':
        s[N-1] = '.'
    

# oのとなりの？は全て.にする
for i in range(1, N-1):
    if s[i] == '?':
        if s[i-1] == 'o' or s[i+1] == 'o':
            s[i] = '.'

# 解答ようにｓをコピー
import copy

s_for_answer = copy.deepcopy(s)

# まずは先頭を処理
if s[0] == '?':
    s[0] = 'o'

# ここからできるだけoをいれる
for i in range(1, N):
    if s[i] == '?':
        if s[i-1] == 'o':
            s[i] = '.'
        elif s[i-1] == '.':
            s[i] = 'o'
# oをカウントしていく
o_max = s.count('o')

# どれだけ?が連続するかカウントする関数
def counter(s, i, N):
    count = 1
    while i + count <= N-1:
        if s[i+count] == '?':
            count += 1
        else:
            break
    return count
# o_maxとKが一致したときここにおいてはs_for_answerを用いる
if o_max == K:
    i = 0
    while i <= N-1:
        if s_for_answer[i] == '?':
            count = counter(s_for_answer, i, N)
            if count % 2 == 0:
                i += count
            elif count % 2 == 1:
                for j in range(0, count):
                    if j % 2 == 0:
                        s_for_answer[i+j] = 'o'
                    elif j % 2 == 1:
                        s_for_answer[i+j] = '.'
                else:
                    i += count
        elif s_for_answer[i] != '?':
            i += 1
    print("".join(s_for_answer))
    exit()

if o_max > K:
    print("".join(s_for_answer))
    exit()


    