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
                    balls.append(grid[x][y])
        else:
            for d in range(2, 4):
                for _ in range(i):
                    x = x + dx[d]
                    y = y + dy[d]
                    balls.append(grid[x][y])

def blizzard(d, s):
    global new_balls, remove_lst
    start = (d+1)*2 - 1
    for i in range(start, 8*(s - 1) + start, 8):
        if i == 1:
            for j in lst:
                remove_lst.append(j)
        else:
            for j in range(4):
                lst[j] += i
                remove_lst.append(lst[j])
    for i in range(len(balls)):
        if i == remove_lst[0]:
            remove_lst.popleft()
            continue
        new_balls.append(balls[i])
    remove_lst.clear()

def explode():
    pass

def change():
    pass

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
balls = []
new_balls = []
remove_lst = deque()

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

grid_to_1d(N//2, N//2)

for _ in range(M):
    d, s = map(int, input().split())