import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
dic = defaultdict(list)

for _ in range(E):
    u, v, w = map(int, input().split())
    dic[u].append((w, v))

heap = []
heapq.heappush(heap, (0, K))

dist = defaultdict(lambda: 'INF')

while heap:
    cost, now = heapq.heappop(heap)
    if dist[now] != 'INF' : continue
    dist[now] = cost

    for w, next in dic[now]:
        next_cost = w + cost
        if dist[next] == 'INF':
            heapq.heappush(heap, (next_cost, next))
    
for i in range(1, V+1):
    print(dist[i])