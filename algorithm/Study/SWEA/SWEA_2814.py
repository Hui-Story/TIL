from collections import defaultdict

def dfs(now, cnt):
    global result

    if cnt > result:
        result = cnt
    
    for node in nodes[now]:
        if not visited[node]:
            visited[node] = 1
            dfs(node, cnt+1)
            visited[node] = 0


T = int(input())

for case in range(1, T+1):
    N, M = map(int, input().split())
    nodes = defaultdict(list)
    result = 0
    visited = [0] * (N+1)

    for _ in range(M):
        a, b = map(int, input().split())
        nodes[a].append(b)
        nodes[b].append(a)
    
    for start in range(1, N+1):
        visited[start] = 1
        dfs(start, 1)
        visited[start] = 0

    print('#{} {}'.format(case, result))