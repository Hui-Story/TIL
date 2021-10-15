import heapq

def dijkstra(dist, adj):
     while minheap:
        cost, now = heapq.heappop(minheap)
        if dist[now] < cost: continue

        for w, next in adj[now]:
            if cost + w < dist[next]:
                dist[next] = cost + w
                heapq.heappush(minheap, (cost + w, next))


T = int(input())

for case in range(1, T+1):
    N, M, X = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    adj_2 = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        adj[x].append((c, y))
        adj_2[y].append((c, x))

    result = 0

    minheap = []
    heapq.heappush(minheap, (0, X))
    dist = [int(21e8) for _ in range(N+1)]
    dist[X] = 0
    dijkstra(dist, adj)

    minheap = []
    heapq.heappush(minheap, (0, X))
    dist_2 = [int(21e8) for _ in range(N+1)]
    dist_2[X] = 0
    dijkstra(dist_2, adj_2)

    for i in range(1, N+1):
        result = max(result, dist[i] + dist_2[i])

    print('#{} {}'.format(case, result))