import heapq

def dijkstra(x, y):
    while heap:
        now_dist, x, y = heapq.heappop(heap)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                next_dist = now_dist + 1 + max(0, MAP[nx][ny] - MAP[x][y])
                if dist[nx][ny] > next_dist:
                    dist[nx][ny] = next_dist
                    heapq.heappush(heap, (next_dist, nx, ny))


T = int(input())

for case in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    dist = [[2e+10]*N for _ in range(N)]
    dist[0][0] = 0
    heap = []
    heapq.heappush(heap, (0, 0, 0))

    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    dijkstra(0, 0)

    print('#{} {}'.format(case, dist[-1][-1]))