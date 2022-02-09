import sys
from collections import defaultdict, deque
input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

def Union(a, b):
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
        if pa < pb:
            parent[pb] = pa
        else:
            parent[pa] = pb

def Find(ch):
    if parent[ch] != ch:
        parent[ch] = Find(parent[ch])
    return parent[ch]

def bfs(start, end):
    deq = deque()
    for bridge in bridges[start]:
        if Find(bridge[0]) == Find(end):
            deq.append([start] + bridge)
    while deq:
        a, b, c = deq.popleft()
        temp = min(dist[a], c)
        if temp <= dist[b]:
            continue
        dist[b] = temp
        for bridge in bridges[b]:
            if Find(bridge[0]) == Find(end):
                deq.append([b] + bridge)


N, M = MIIS()
parent = [i for i in range(N + 1)]
dist = [0] * (N + 1)

bridges = defaultdict(list)
for _ in range(M):
    a, b, c = MIIS()
    Union(a, b)
    for bridge in bridges[a]:
        if b == bridge[0]:
            bridge[1] = max(bridge[1], c)
            break
    for bridge in bridges[b]:
        if a == bridge[0]:
            bridge[1] = max(bridge[1], c)
            break
    else:
        bridges[a].append([b, c])
        bridges[b].append([a, c])

S, E = MIIS()
dist[S] = 1000000001
bfs(S, E)

print(dist[E])