import sys
from collections import deque
input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

M, N, V = MIIS()
X, Y = MIIS()
X, Y = X - 1, Y - 1
island = [list(MIIS()) for _ in range(M)]
MAP = [[1000] * N for _ in range(M)]
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
dust_lst = []
max_height = island[X][Y]
min_time = 0

q = []

for _ in range(V):
    x, y, n = MIIS()
    MAP[x - 1][y - 1] = n
    q.append((x - 1, y - 1, n))

q.sort(key=lambda x : x[2])
deq = deque(q)
while deq:
    x, y, n = deq.popleft()
    if MAP[x][y] == n:
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < M and 0 <= ny < N:
                if MAP[nx][ny] >= 0 and MAP[nx][ny] > n + 1:
                    MAP[nx][ny] = n + 1
                    deq.append((nx, ny, n + 1))

deq.append((X, Y, 0))
while deq:
    x, y, n = deq.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < M and 0 <= ny < N and MAP[nx][ny] > n + 1:
            deq.append((nx, ny, n + 1))
            if island[nx][ny] >= max_height:
                if island[nx][ny] == max_height:
                    min_time = min(min_time, n + 1)
                else:
                    min_time = n + 1
                max_height = island[nx][ny]

print(max_height, min_time)