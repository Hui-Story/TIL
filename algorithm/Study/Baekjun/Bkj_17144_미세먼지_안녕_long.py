import sys
input = sys.stdin.readline


def dust_diffusion():
    global grid
    new_grid = [[0]*C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if grid[x][y] >= 5:
                dust = int(grid[x][y] / 5)
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] >= 0:
                        new_grid[x][y] -= dust
                        new_grid[nx][ny] += dust
    for x in range(R):
        for y in range(C):
            grid[x][y] += new_grid[x][y]


def air_cleaning(air_cleaner):
    global grid
    ax_1, ax_2 = air_cleaner
    for x in range(ax_1-1, 0, -1):
        grid[x][0] = grid[x-1][0]
    for x in range(ax_2+1, R-1):
        grid[x][0] = grid[x+1][0]
    for y in range(C-1):
        grid[0][y] = grid[0][y+1]
        grid[R-1][y] = grid[R-1][y+1]
    for x in range(ax_1):
        grid[x][C-1] = grid[x+1][C-1]
    for x in range(R-1, ax_2, -1):
        grid[x][C-1] = grid[x-1][C-1]
    for y in range(C-1, 1, -1):
        grid[ax_1][y] = grid[ax_1][y-1]
        grid[ax_2][y] = grid[ax_2][y-1]
    grid[ax_1][1], grid[ax_2][1] = 0, 0


dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

R, C, T = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]

for x in range(R-3):
    if grid[x][0] == -1:
        air_cleaner = [x, x+1]
        break

for _ in range(T):
    dust_diffusion()
    air_cleaning(air_cleaner)

result = 0
for arr in grid:
    result += sum(arr)
print(result + 2)