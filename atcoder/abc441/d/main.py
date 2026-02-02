from collections import defaultdict

n, m, l, s, t = map(int, input().split())

adj = [[] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))

current_costs = defaultdict(set)
current_costs[1].add(0)

for _ in range(l):
    next_costs = defaultdict(set)
    for u, costs in current_costs.items():
        for v, c in adj[u]:
            for w in costs:
                new_cost = w + c
                if new_cost <= t:
                    next_costs[v].add(new_cost)
    current_costs = next_costs

answer = []
for v in range(1, n + 1):
    if any(s <= w <= t for w in current_costs[v]):
        answer.append(v)

print(*answer)




