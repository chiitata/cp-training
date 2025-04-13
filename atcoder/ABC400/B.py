def power(a, n):
    if n == 0:
        return 1
    elif n%2 == 0:
        temp = power(a, n/2)
        return temp * temp
    else:
        temp = power(a, (n-1)/2)
        return a * temp * temp

n, m = map(int, input().split())

if n == 1:
    print(n*m+1)
    exit()

try:
    answer = int((power(n, m+1)-1)/(n-1))
    if answer <= 10**9:
        print(answer)
    else:
        print("inf")
except OverflowError:
    print("inf")


