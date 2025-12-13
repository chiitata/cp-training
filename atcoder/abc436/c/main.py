import sys

input = sys.stdin.readline

n, m = map(int, input().split())
occupied = set()
answer = 0
for _ in range(m):
    r, c = map(int, input().split())
    target_cells = [
        (r-1, c-1),
        (r-1, c),
        (r, c-1),
        (r, c)
    ]
    is_valid = True
    for tr, tc in target_cells:
        if tr < 0 or tc < 0: 
            is_valid = False
            break
        if (tr, tc) in occupied:
            is_valid = False
            break
    
    if is_valid:
        for cell in target_cells:
            occupied.add(cell)
        answer += 1

print(answer)