
import sys
input_data = sys.stdin.read().split()


iterator = iter(input_data)
num_test_cases = int(next(iterator))

results = []

for _ in range(num_test_cases):
    try:
        N = int(next(iterator))
        R = []
        for _ in range(N):
            R.append(int(next(iterator)))
    except StopIteration:
        break

    H = list(R)

    for i in range(1, N):
        if H[i] > H[i-1] + 1:
            H[i] = H[i-1] + 1

    for i in range(N - 2, -1, -1):
        if H[i] > H[i+1] + 1:
            H[i] = H[i+1] + 1

    total_moves = 0
    for i in range(N):
        total_moves += (R[i] - H[i])
        
    results.append(str(total_moves))

print('\n'.join(results))
