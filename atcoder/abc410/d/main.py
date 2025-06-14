from collections import deque


def min_xor_walk(N, M, edges):
    from collections import defaultdict

    graph = defaultdict(list)
    for a, b, w in edges:
        graph[a].append((b, w))
    
    MAX_XOR = 1024
    visited = [set() for _ in range(N + 1)]

    dq = deque()
    dq.append((1, 0))  # (現在の頂点, 現在のXOR値)
    visited[1].add(0)

    while dq:
        node, xor_val = dq.popleft()
        for neighbor, weight in graph[node]:
            new_xor = xor_val ^ weight
            if new_xor not in visited[neighbor]:
                visited[neighbor].add(new_xor)
                dq.append((neighbor, new_xor))
    
    # 頂点Nに到達できるXOR値の中で最小を返す
    return min(visited[N]) if visited[N] else -1
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

print(min_xor_walk(N, M, edges))
