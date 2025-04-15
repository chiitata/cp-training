# 計算し終わった後に割ると実行が遅くなるかもしれないから毎回の計算の時に割り算を実行した方がいいかも
# 差分を考えると一個前のA_nとA_n+1の違いはA_nにA_nを足してA_i-kを引くと求めることができる
# 全てのK<=iに対してAiの項数がすべて等しいことに注意
N, K = map(int, input().split())
# Nが必ずKよりも大きいとは限らないことに注意

if K >= N + 1:
    print(1)
    exit()

a = [1 for _ in range(N+1)]

A = K

for i in range(K, N+1):
    a[i] = A
    A = (A + a[i] - a[i-K]) % 10**9
# やはり毎回余りを取らないと答えの数値が莫大になってしまう様である
answer = a[N] 

print(answer)