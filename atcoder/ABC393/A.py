s = list(input().split())

if s[0] == 'sick' and s[1] == 'sick':
    print(1)
elif s[0] == 'sick' and s[1] == 'fine':
    print(2)
elif s[0] == 'fine' and s[1] == 'sick':
    print(3)
elif s[0] == 'fine' and s[1] == 'fine':
    print(4)