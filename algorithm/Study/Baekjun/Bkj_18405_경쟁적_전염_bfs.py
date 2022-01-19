import sys
input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

N, K = MIIS()
grid = [list(MIIS()) for _ in range(N)]
S, X, Y = MIIS()

dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)

virus = []
for x in range(N):
    for y in range(N):
        if grid[x][y]:
            virus.append((x, y, grid[x][y]))
virus.sort(key=lambda x : x[2])

idx = 0
for _ in range(S):
    virus_cnt = len(virus) - idx
    for _ in range(virus_cnt):
        x, y, num = virus[idx]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and not grid[nx][ny]:
                grid[nx][ny] = num
                virus.append((nx, ny, num))
        idx += 1

print(grid[X - 1][Y - 1])