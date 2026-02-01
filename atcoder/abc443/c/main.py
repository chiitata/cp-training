N, T = map(int, input().split())
A = list(map(int, input().split()))

total_watch_time = 0
open_time = 0  

for a in A:
    if open_time < a:
        total_watch_time += (a - open_time)
        open_time = a + 100
    else:
        pass

if open_time < T:
    total_watch_time += (T - open_time)

print(total_watch_time)