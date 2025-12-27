import sys

# 入力を高速に読み込む
input_data = sys.stdin.read().split()
    
n = int(input_data[0])
a = input_data[1:] # 全て文字列のままリストへ

stack = []

for x in a:
    stack.append(x)
    # スタックの末尾4つが同じかチェック
    if len(stack) >= 4:
        if stack[-1] == stack[-2] == stack[-3] == stack[-4]:
            # 4つ削除
            for _ in range(4):
                stack.pop()
                
print(len(stack))