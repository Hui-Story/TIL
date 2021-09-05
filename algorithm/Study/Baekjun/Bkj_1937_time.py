import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(now):
    global visited, result
    i = now[0]
    j = now[1]
    for d in range(4):
        x = i + dx[d]
        y = j + dy[d]
        if 0 <= x < n and 0 <= y < n and visited[x][y] <= visited[i][j] and MAP[x][y] > MAP[i][j]:
            visited[x][y] = visited[i][j] + 1
            result = max(visited[x][y], result)
            dfs([x, y])
    return

n = int(input())
MAP = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited = [[0]*n for _ in range(n)]
result = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            visited[i][j] = 1
            for d in range(4):
                x = i + dx[d]
                y = j + dy[d]
                if 0 <= x < n and 0 <= y < n:
                    if MAP[x][y] <= MAP[i][j]:
                        break
                    else:
                        visited[x][y] = 1
            else:
                dfs([i, j])

print(result)