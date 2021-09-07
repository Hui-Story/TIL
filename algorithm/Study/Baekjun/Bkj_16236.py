import sys
from collections import deque
input = sys.stdin.readline

def bfs(now, start):
    global MAP, visited, shark
    deq = deque([now, start])
    visited[now[0]][now[1]] = 1
    fish_lst = []
    fish_cnt = 2e+10
    while deq:
        a = deq.popleft()
        cnt = deq.popleft()
        if cnt > fish_cnt:
            break
        i, j = a[0], a[1]
        for d in range(4):
            x = i + dx[d]
            y = j + dy[d]
            if 0 <= x < N and 0 <= y < N and visited[x][y] == 0 and MAP[x][y] <= shark_size:
                visited[x][y] = visited[i][j] + 1
                if MAP[x][y] != 0 and MAP[x][y] < shark_size:
                    fish_lst.append([x, y])
                    fish_cnt = cnt
                deq.append([x, y])
                deq.append(cnt+1)
    if fish_lst:
        fish_lst.sort()
        shark = list(fish_lst[0])
        MAP[shark[0]][shark[1]] = 0
        return visited[shark[0]][shark[1]] - 1
    else:
        return 0


N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

result = 0
shark_size = 2
eat_fish = 0

for i in range(N):
    for j in range(N):
        if MAP[i][j] == 9:
            shark = [i, j]
            MAP[i][j] = 0
            break

while True:
    if eat_fish == shark_size:
        eat_fish = 0
        shark_size += 1

    visited = [[0]*N for _ in range(N)]
    move = bfs(shark, 0)

    if move == 0:
        break
    else:
        result += move
        eat_fish += 1

print(result)