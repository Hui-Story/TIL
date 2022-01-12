import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(now, end, dist):
    global result
    if now == end:
        result = min(result, dist)
    if dist >= result:
        return
    for n, d in tree[now]:
        if not visited[n]:
            visited[n] = 1
            dfs(n, end, dist + d)
            visited[n] = 0


N, M = map(int, input().split())

tree = defaultdict(list)
for _ in range(N-1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

for _ in range(M):
    a, b = map(int, input().split())
    visited = [0] * (N+1)
    visited[a] = 1
    result = 10000000
    dfs(a, b, 0)
    print(result)