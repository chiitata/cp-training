n = int(input())
s = [None] + list(input())
counter = s.count('1')
index = [None]
for i in range(1, n+1):
    if s[i] == '1':
        index.append(i)

center = 0
count = 0
for i in range(len(s)):
    if s[i] == '1':
        count += 1
        if count == s.count('1')//2+1:
            center = i
            break

answer = 0
for i in range(1, counter+1):
    cnt = abs(counter//2-i+1)
    answer += abs(index[i]-center)-cnt

print(answer)

