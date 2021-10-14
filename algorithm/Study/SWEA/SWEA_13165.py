import heapq

def dijkstra():
    while minheap:
        cost, now = heapq.heappop(minheap)
        if dist[now] < cost: continue

        for w, next in adj[now]:
            if cost + w < dist[next]:
                dist[next] = cost + w
                heapq.heappush(minheap, (cost + w, next))


T = int(input())

for case in range(1, T+1):
    N, E = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s].append((w, e))
    minheap = []
    heapq.heappush(minheap, (0, 0))
    dist = [int(21e8) for _ in range(N+1)]
    dist[0] = 0

    dijkstra()

    print('#{} {}'.format(case, dist[-1]))