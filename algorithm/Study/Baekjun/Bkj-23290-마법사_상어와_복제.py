import sys

input = sys.stdin.readline
MIIS = lambda: map(int, input().split())

def fish_move():
    global new_grid

    for x in range(4):
        for y in range(4):
            for d in grid[x][y]:
                for _ in range(8):
                    dx, dy = dir[d]
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 4 and 0 <= ny < 4 and smell_grid[nx][ny] == 0 and (nx, ny) != (sx, sy):
                        new_grid[nx][ny].append(d)
                        break
                    d = (d + 7) % 8
                else:
                    new_grid[x][y].append(d)

def shark_move():
    global sx, sy, smell_grid, new_grid

    max_cnt = 0
    max_dir = (0, 0, 0, 0, 0, 0)

    for d1 in range(4):
        dx1, dy1 = dir2[d1]
        sx1, sy1 = sx + dx1, sy + dy1
        if 0 <= sx1 < 4 and 0 <= sy1 < 4:
            for d2 in range(4):
                dx2, dy2 = dir2[d2]
                sx2, sy2 = sx1 + dx2, sy1 + dy2
                if 0 <= sx2 < 4 and 0 <= sy2 < 4:
                    for d3 in range(4):
                        dx3, dy3 = dir2[d3]
                        sx3, sy3 = sx2 + dx3, sy2 + dy3
                        if 0 <= sx3 < 4 and 0 <= sy3 < 4:
                            now_cnt = 0
                            for x, y in set([(sx1, sy1), (sx2, sy2), (sx3, sy3)]):
                                now_cnt += len(new_grid[x][y])
                            if now_cnt >= max_cnt:
                                max_cnt = now_cnt
                                max_dir = ((sx1, sy1), (sx2, sy2), (sx3, sy3))
    
    for x, y in max_dir:
        if new_grid[x][y]:
            smell_grid[x][y] = 3
        new_grid[x][y].clear()
    
    sx, sy = max_dir[2]

def remove_smell():
    global smell_grid

    for x in range(4):
        for y in range(4):
            if smell_grid[x][y] > 0:
                smell_grid[x][y] -= 1



M, S = MIIS()
grid = [[[] for _ in range(4)] for _ in range(4)]
smell_grid = [[0] * 4 for _ in range(4)]
dir = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))
dir2 = ((0, 1), (1, 0), (0, -1), (-1, 0))

for _ in range(M):
    fx, fy, d = MIIS()
    grid[fx - 1][fy - 1].append(d - 1)

sx, sy = MIIS()
sx, sy = sx - 1, sy - 1

for _ in range(S):
    new_grid = [[[] for _ in range(4)] for _ in range(4)]

    fish_move()

    shark_move()

    remove_smell()

    for x in range(4):
        for y in range(4):
            grid[x][y].extend(new_grid[x][y][:])

print(sum([sum([len(i) for i in g]) for g in grid]))