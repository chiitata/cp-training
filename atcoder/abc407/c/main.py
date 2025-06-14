# !/usr/bin/env python3


s = list(str(input()))

answer = 0
for i in range(len(s)-1, -1, -1):
    if i == len(s)-1:
        answer += int(s[i])
    else:
        t = int(s[i])-answer
        if t >= 0:
            answer += t
        else:
            t = str(abs(t))
            p = list(t)
            q = 10 - int(p[-1])
            if q != 10:
                answer += q
print(answer+len(s))