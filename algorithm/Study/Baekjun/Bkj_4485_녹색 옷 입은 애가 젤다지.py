import sys, heapq
input = sys.stdin.readline

def dijkstra():
    while minheap:
        cost, x, y = heapq.heappop(minheap)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and cost + MAP[nx][ny] < dist[nx][ny]:
                dist[nx][ny] = cost + MAP[nx][ny]
                heapq.heappush(minheap, (dist[nx][ny], nx, ny))


case = 0

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

while True:
    case += 1
    N = int(input())
    if N == 0:
        break
    MAP = [list(map(int, input().split())) for _ in range(N)]
    
    minheap = []
    heapq.heappush(minheap, (MAP[0][0], 0, 0))

    dist = [[int(2e+8)]*N for _ in range(N)]
    dist[0][0] = MAP[0][0]

    dijkstra()

    print('Problem {}: {}'.format(case, dist[-1][-1]))