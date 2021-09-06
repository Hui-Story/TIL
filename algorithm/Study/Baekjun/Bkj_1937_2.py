import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(i, j):
    global visited, result
    if visited[i][j] != 0:
        return visited[i][j]
    else:
        visited[i][j] = 1
        for d in range(4):
            x = i + dx[d]
            y = j + dy[d]
            if 0 <= x < n and 0 <= y < n and MAP[i][j] < MAP[x][y]:
                visited[i][j] = max(visited[i][j], dfs(x, y)+1)
        return visited[i][j]

n = int(input())
MAP = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited = [[0]*n for _ in range(n)]
result = 0

for i in range(n):
    for j in range(n):
        result = max(result, dfs(i, j))

print(result)