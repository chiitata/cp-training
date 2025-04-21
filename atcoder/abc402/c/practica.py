# この問題はいちいちfor文で全食材を見ていくことはできないので
# 食材を確認したらその食材を使っている料理を覚えておきその料理の数を1減らして0になったならば
# answerを１増やすという操作をする
# 入力を得ている
N, M = map(int, input().split())
# これは各料理の素材数を格納しておくリスト
food_count = [None for _ in range(M+1)]
# これは各素材がどの料理に使われているか格納しておくところ
what_food = [[] for _ in range(N+1)]
# 入力を受け取り素材数のところとどういった素材が使われているか分ける
for i in range(1, M+1):
    dish = list(map(int, input().split()))
    k = dish[0]
    food_count[i] = k
    # 各素材に使われている料理の情報を格納
    for s in dish[1:]:
        what_food[s].append(i)

# これは素材を克服していく順番を格納しているリスト
B = list(map(int, input().split()))

answer = 0
# 各素材が使われている料理を確認してその料理の素材数をー１する
for i in B:
    for j in what_food[i]:
        food_count[j] -= 1
        if food_count[j] == 0:
            answer += 1
    print(answer)

    