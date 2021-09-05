import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
MAP = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited = [[0]*n for _ in range(n)]
stack = deque()
result = 1

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            visited[i][j] = 1
            for d in range(4):
                x = i + dx[d]
                y = j + dy[d]
                if 0 <= x < n and 0 <= y < n and MAP[x][y] <= MAP[i][j]:
                    break
            else:
                stack.append([i, j])
                while stack:
                    a = stack.pop()
                    a_i, a_j = a[0], a[1]
                    for d in range(4):
                        x = a_i + dx[d]
                        y = a_j + dy[d]
                        if 0 <= x < n and 0 <= y < n and visited[x][y] <= visited[a_i][a_j] and MAP[x][y] > MAP[a_i][a_j]:
                            visited[x][y] = visited[a_i][a_j] + 1
                            result = max(visited[x][y], result)
                            stack.append([x, y])

print(result)