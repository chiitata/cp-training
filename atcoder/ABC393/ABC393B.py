s = list(input())
answer = 0
for i in range(len(s)):
    j = 0
    if s[i] == 'B':
        while i-j-1>=0 and i+j+1<=len(s)-1:
            j += 1
            if s[i-j]== 'A' and s[i+j] == 'C':
                answer += 1
    
print(answer)