import heapq

def dijkstra():
    while minheap:
        cost, x, y = heapq.heappop(minheap)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and cost+int(MAP[nx][ny]) < dist[nx][ny]:
                dist[nx][ny] = cost + int(MAP[nx][ny])
                heapq.heappush(minheap, (dist[nx][ny], nx, ny))


T = int(input())

for case in range(1, T+1):
    N = int(input())
    MAP = [list(str(input())) for _ in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    minheap = []
    heapq.heappush(minheap, (0, 0, 0))
    dist = [[int(21e8)]*N for _ in range(N)]
    dist[0][0] = 0

    dijkstra()

    print('#{} {}'.format(case, dist[-1][-1]))