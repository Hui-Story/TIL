import sys
from collections import deque
input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

M, N, V = MIIS()
X, Y = MIIS()
X, Y = X - 1, Y - 1
island = [list(MIIS()) for _ in range(M)]
MAP = [[-1] * N for _ in range(M)]
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
dust_lst = []
max_height = island[X][Y]
min_time = 0

for _ in range(V):
    x, y, n = MIIS()
    x -= 1
    y -= 1
    dust_lst.append((x, y, n))

dust_lst.sort(key=lambda x : x[2], reverse=True)
i = V - 1
time = dust_lst[i][2]
now_dust_lst = []

while i >= 0 and dust_lst[i][2] == time:
    now_dust_lst.append(dust_lst[i])
    i -= 1

while now_dust_lst:
    new_dust_lst = []
    time += 1
    while i >= 0 and dust_lst[i][2] == time:
        new_dust_lst.append(dust_lst[i])
        i -= 1
    for x, y, n in now_dust_lst:
        if MAP[x][y] == -1 or MAP[x][y] == n:
            MAP[x][y] = n
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < M and 0 <= ny < N:
                    if MAP[nx][ny] == -1:
                        MAP[nx][ny] = n + 1
                        new_dust_lst.append((nx, ny, n + 1))
    now_dust_lst = new_dust_lst[:]

for x, y, n in dust_lst:
    MAP[x][y] = -1

deq = deque()
deq.append((X, Y, 0))
while deq:
    x, y, n = deq.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < M and 0 <= ny < N and MAP[nx][ny] > n + 1 and MAP[nx][ny] != -1:
            deq.append((nx, ny, n + 1))
            MAP[nx][ny] = -1
            if island[nx][ny] >= max_height:
                if island[nx][ny] == max_height:
                    min_time = min(min_time, n + 1)
                else:
                    min_time = n + 1
                max_height = island[nx][ny]

print(max_height, min_time)