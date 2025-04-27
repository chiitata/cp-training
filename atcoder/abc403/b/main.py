# !/usr/bin/env python3

t = list(input())
s = list(input())

for i in range(len(t)):
    if t[i] == "?":
        for j in range(1, len(s)):
            if i+j<len(t):
                if t[i+j] == s[j] or t[i+j] == "?":
                    continue
                else:
                    break
            else:
                break
        else:
            print('Yes')
            exit()
    elif t[i] == s[0]:
        for j in range(1, len(s)):
            if i+j<len(t):
                if t[i+j] == s[j] or t[i+j] == '?':
                    continue
                else:
                    break
            else:
                break
        else:
            print('Yes')
            exit()
else:
    print('No')
