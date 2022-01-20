import sys
from collections import deque
input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

def air_check():
    global grid, deq
    cheese = []
    while deq:
        x, y = deq.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if not grid[nx][ny]:
                    grid[nx][ny] = 2
                    deq.append((nx, ny))
                elif grid[nx][ny] == 1:
                    cheese.append((nx, ny))
    return list(set(cheese))


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)

cheese_cnt = 0
for x in range(N):
    for y in range(M):
        if grid[x][y] == 1:
            cheese_cnt += 1

deq = deque()
for x, y in [(0, 0), (0, M - 1), (N - 1, 0), (N - 1, M - 1)]:
    deq.append((x, y))
    grid[x][y] = 2
cheese = air_check()

time = 0
while cheese_cnt:
    last_cnt = cheese_cnt
    cheese_cnt -= len(cheese)
    deq.extend(cheese)
    for x, y in cheese:
        grid[x][y] = 2
    cheese = air_check()
    time += 1

print(time)
print(last_cnt)