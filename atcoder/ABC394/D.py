s = list(input())
from collections import deque

l = deque()

for i in range(len(s)):
    try:
        if (s[i] == '[')or(s[i] == '<')or(s[i] == '('):
            l.append(s[i])
        elif s[i] == ')':
            if l[-1] != '(':
                print('No')
                exit()
            l.pop()
        elif s[i] == ']':
            if l[-1] != '[':
                print('No')
                exit()
            l.pop()
        elif s[i] == '>':
            if l[-1] != '<':
                print('No')
                exit()
            l.pop()
    except IndexError:
        print('No')
        exit()
else:
    if len(l) == 0:
        print('Yes')
    else:
        print('No')

