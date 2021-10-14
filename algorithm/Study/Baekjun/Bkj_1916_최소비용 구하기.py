import sys, heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, w = map(int, input().split())
    adj[a].append((w, b))
S, E = map(int, input().split())

minheap = []
dist = [int(21e8) for _ in range(N+1)]
heapq.heappush(minheap, (0, S))

while minheap:
    cost, now = heapq.heappop(minheap)
    if dist[now] != int(21e8) : continue
    dist[now] = cost

    for w, next in adj[now]:
        heapq.heappush(minheap, (cost + w, next))

print(dist[E])