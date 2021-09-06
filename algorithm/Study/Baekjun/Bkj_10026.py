import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    global visited, cnt
    visited[i][j] = 1
    deq.append([i, j])
    cnt += 1
    while deq:
        a = deq.popleft()
        a_i, a_j = a[0], a[1]
        for d in range(4):
            x = a_i + dx[d]
            y = a_j + dy[d]
            if 0 <= x < N and 0 <= y < N and visited[x][y] == 0 and MAP[a_i][a_j] == MAP[x][y]:
                visited[x][y] = 1
                deq.append([x, y])

N = int(input())
MAP = [list(str(input()))[:N] for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited = [[0]*N for _ in range(N)]
deq = deque()
cnt = 0
result = []

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j)
result.append(cnt)

for i in range(N):
    for j in range(N):
        visited[i][j] = 0
        if MAP[i][j] == 'G':
            MAP[i][j] = 'R'

cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j)
result.append(cnt)


print(*result)