import sys
from collections import defaultdict
input = sys.stdin.readline

def dfs(now):
    if not tree[now]:
        return
    for i in tree[now]:
        pass

N, S, D = map(int, input().split())
tree = defaultdict(list)
depth = [0] * (N + 1)
depth_check = False

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

