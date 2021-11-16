import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    global result, max_length
    deq = deque()
    deq.append([x, y, 1])
    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 1

    while deq:
        ax, ay, cnt = deq.popleft()
        route_check = False
        for d in range(4):
            nx = ax + dx[d]
            ny = ay + dy[d]
            if 0 <= nx < N and 0 <= ny < M and MAP[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                deq.append([nx, ny, cnt + 1])
                route_check = True
        if not route_check:
            if cnt > max_length:
                result = MAP[x][y] + MAP[ax][ay]
                max_length = cnt
            elif cnt == max_length:
                result = max(result, MAP[x][y] + MAP[ax][ay])


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

result = 0
max_length = 0

for x in range(N):
    for y in range(M):
        if MAP[x][y]:
            route_count = 0
            border_count = 0
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < N and 0 <= ny < M and MAP[nx][ny]:
                    route_count += 1
            if route_count == 0:
                if max_length <= 1:
                    result = max(result, MAP[x][y] * 2)
            elif route_count <= 2:
                bfs(x, y)

print(result)