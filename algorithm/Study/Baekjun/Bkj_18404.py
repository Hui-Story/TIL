import sys
from collections import deque
input = sys.stdin.readline

def bfs(knight):
    global visited
    deq = deque([knight])
    cnt = 0
    while deq:
        if cnt >= len(targets):
            return
        a = deq.popleft()
        i, j = a[0], a[1]
        for d in range(8):
            x = i + dx[d]
            y = j + dy[d]
            if 0 <= x < N and 0 <= y < N and visited[x][y] <= -1:
                visited[x][y] = visited[i][j] + 1
                if visited[x][y] == -2:
                    cnt += 1
                deq.append([x, y])
    return


N, M = list(map(int, input().split()))
knight = list(map(int, input().split()))

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

visited = [[-1]*N for _ in range(N)]
targets = []
result = []

for _ in range(M):
    i, j = map(int, input().split())
    visited[i-1][j-1] = -2
    targets.append([i-1, j-1])

visited[knight[0]-1][knight[1]-1] = 0
bfs([knight[0]-1, knight[1]-1])

for target in targets:
    result.append(visited[target[0]][target[1]])

print(*result)