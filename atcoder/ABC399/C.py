def count_connected_components(n, edges):
    # 隣接リストの作成
    graph = [[] for _ in range(n+1)]  # 頂点番号は 1-indexed
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n + 1)
    
    def dfs(v):
        stack = [v]
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
    
    component_count = 0
    for vertex in range(1, n+1):
        if not visited[vertex]:
            dfs(vertex)
            component_count += 1
    
    return component_count

# まず、最初の行を読み込み、数値に変換します
n, m = map(int, input().split())

# 空のリストを用意します
edges = []

# 続くm行のペアをリストに追加していきます
for _ in range(m):
    a, b = map(int, input().split())
    edges.append((a, b))  # タプルとして追加

answer = count_connected_components(n, edges)  # 出力は 3 となるはずです

print(m-(n-answer))