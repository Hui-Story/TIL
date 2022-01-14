import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def depth_check(now):
    global visited, result
    if not tree[now]:
        return 1
    now_depth = 0
    for i in tree[now]:
        if not visited[i]:
            visited[i] = 1
            child_depth = depth_check(i)
            now_depth = max(now_depth, child_depth + 1)
            if child_depth >= D:
                result += 2
            visited[i] = 0
    return now_depth


N, S, D = map(int, input().split())
tree = defaultdict(list)
visited = [0] * (N + 1)
visited[S] = 1
result = 0

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

depth_check(S)

print(result)