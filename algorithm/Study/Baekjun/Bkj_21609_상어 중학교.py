from collections import deque
import copy

def auto_play():
    global grid, deq, result
    block_delete = []
    max_rainbow = 0
    for num in range(1, M+1):
        visited = [[0]*N for _ in range(N)]
        for x in range(N):
            for y in range(N):
                if num == grid[x][y] and not visited[x][y]:
                    visited[x][y] = 1
                    deq.append([x, y])
                    block_group = [[x, y]]
                    rainbow = 0
                    while deq:
                        qx, qy = deq.popleft()
                        for d in range(4):
                            nqx = qx + dx[d]
                            nqy = qy + dy[d]
                            if 0 <= nqx < N and 0 <= nqy < N and not visited[nqx][nqy]:
                                if grid[nqx][nqy] in [0, num]:
                                    if grid[nqx][nqy] == 0:
                                        rainbow += 1
                                    visited[nqx][nqy] = 1
                                    deq.append([nqx, nqy])
                                    block_group.append([nqx, nqy])
                    if len(block_group) > len(block_delete):
                        block_delete = copy.deepcopy(block_group)
                        max_rainbow = rainbow
                    elif len(block_group) == len(block_delete):
                        if rainbow > max_rainbow:
                            block_delete = copy.deepcopy(block_group)
                            max_rainbow = rainbow
                        elif rainbow == max_rainbow:
                            if block_delete[0][0] < x:
                                block_delete = copy.deepcopy(block_group)
                                max_rainbow = rainbow
                            elif block_delete[0][0] == x and block_delete[0][1] < y:
                                block_delete = copy.deepcopy(block_group)
                                max_rainbow = rainbow

    if len(block_delete) <= 1:
        return False

    result += len(block_delete)**2
    for x, y in block_delete:
        grid[x][y] = -2

    gravity()
    rotate()
    gravity()

    return True

def gravity():
    global grid
    for x in range(N-2, -1, -1):
        for y in range(N):
            if grid[x][y] not in [-1, -2]:
                move = 0
                for n in range(1, N):
                    nx = x + n
                    if nx < N and grid[nx][y] == -2:
                        move = n
                    else:
                        break
                if move:
                    grid[x][y], grid[x+move][y] = grid[x+move][y], grid[x][y]

def rotate():
    global grid
    new_grid = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_grid[i][j] = grid[j][N-1-i]
    grid = copy.deepcopy(new_grid)


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

deq = deque()
result = 0

while True:
    if not auto_play():
        break

print(result)