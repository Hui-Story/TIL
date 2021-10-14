import sys
from collections import deque
input = sys.stdin.readline

def grid_to_1d(x, y):
    for i in range(1, N):
        if i % 2:
            for d in range(2):
                for _ in range(i):
                    x = x + dx[d]
                    y = y + dy[d]
                    if grid[x][y] == 0:
                        return
                    balls.append(grid[x][y])
        else:
            for d in range(2, 4):
                for _ in range(i):
                    x = x + dx[d]
                    y = y + dy[d]
                    if grid[x][y] == 0:
                        return
                    balls.append(grid[x][y])
    for i in range(N-1):
        x = x + dx[0]
        y = y + dy[0]
        if grid[x][y] == 0:
            return
        balls.append(grid[x][y])

def blizzard(d, s):
    global balls, new_balls, remove_lst

    new_balls = []
    d_idx = di[d-1]
    ds = di[d-1] + 1
    for i in range(ds, 8*(s-1) + ds + 1, 8):
        if i == di[d-1] + 1:
            remove_lst.append(d_idx)
        else:
            d_idx += i
            remove_lst.append(d_idx)

    for i in range(len(balls)):
        if remove_lst and i == remove_lst[0]:
            remove_lst.popleft()
            continue
        new_balls.append(balls[i])
    
    balls = []
    remove_lst.clear()

def explode():
    global balls, new_balls, remove_lst, result

    check = False
    non_explode_balls = deque()
    cnt = 0
    for i in range(len(new_balls)):
        if i == 0:
            cnt += 1
            non_explode_balls.append(new_balls[i])
            continue
        if new_balls[i] == non_explode_balls[-1]:
            cnt += 1
            non_explode_balls.append(new_balls[i])
        else:
            if cnt >= 4:
                check = True
                result += cnt * non_explode_balls[-1]
                for _ in range(cnt):
                    non_explode_balls.pop()
            cnt = 1
            non_explode_balls.append(new_balls[i])
    if cnt >= 4:
        check = True
        result += cnt * non_explode_balls[-1]
        for _ in range(cnt):
            non_explode_balls.pop()

    new_balls = list(non_explode_balls)[:]

    if check:
        explode()

def change():
    global balls, new_balls

    cnt = 0
    for i in range(len(new_balls)):
        if len(balls) >= (N**2 - 2):
            break
        if i == 0:
            cnt += 1
            continue
        if new_balls[i] == new_balls[i-1]:
            cnt += 1
        else:
            balls.append(cnt)
            balls.append(new_balls[i-1])
            cnt = 1
    if len(balls) < (N**2 - 2):
        balls.append(cnt)
        balls.append(new_balls[-1])


N, M = map(int, input().strip().split())
grid = [list(map(int, input().strip().split())) for _ in range(N)]
balls = []
new_balls = []
remove_lst = deque()
result = 0

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
di = [6, 2, 0, 4]


grid_to_1d(N//2, N//2)

for _ in range(M):
    d, s = map(int, input().strip().split())
    blizzard(d, s)
    explode()
    if new_balls:
        change()

print(result)