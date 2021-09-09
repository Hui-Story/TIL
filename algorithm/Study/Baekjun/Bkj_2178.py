import sys
from collections import deque
from typing import Mapping
input = sys.stdin.readline

def bfs(i, j):
    global visited, deq
    deq.append([i, j])
    visited[i][j] = 1
    while deq:
        a = deq.popleft()
        a_i, a_j = a[0], a[1]
        for d in range(4):
            x = a_i + dx[d]
            y = a_j + dy[d]
            if 0 <= x < N and 0 <= y < M and MAZE[x][y] == '1' and visited[x][y] == 0:
                visited[x][y] = visited[a_i][a_j] + 1
                deq.append([x, y])


N, M = map(int, input().split())
MAZE = [list(str(input()))[:M] for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

deq = deque()

bfs(0, 0)

print(visited[N-1][M-1])