import sys
from collections import deque
input = sys.stdin.readline

def bfs_virus():
    global MAP, deq
    cnt = 0
    infect = []
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 2:
                deq.append([i, j])
            elif MAP[i][j] == 0:
                cnt += 1
    while deq:
        a = deq.popleft()
        a_i, a_j = a[0], a[1]
        for d in range(4):
            x = a_i + dx[d]
            y = a_j + dy[d]
            if 0 <= x < N and 0 <= y < M and MAP[x][y] == 0:
                MAP[x][y] = 2
                deq.append([x, y])
                infect.append([x, y])
                cnt -= 1
    for i in infect:
        MAP[i[0]][i[1]] = 0
    return cnt


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

deq = deque()
result = 0

for wall_1 in range(N*M-2):
    wall_1_i = wall_1 // M
    wall_1_j = wall_1 % M
    if MAP[wall_1_i][wall_1_j] != 0:
        continue
    else:
        MAP[wall_1_i][wall_1_j] = 1
        for wall_2 in range(wall_1+1, N*M-1):
            wall_2_i = wall_2 // M
            wall_2_j = wall_2 % M
            if MAP[wall_2_i][wall_2_j] != 0:
                continue
            else:
                MAP[wall_2_i][wall_2_j] = 1
                for wall_3 in range(wall_2+1, N*M):
                    wall_3_i = wall_3 // M
                    wall_3_j = wall_3 % M
                    if MAP[wall_3_i][wall_3_j] != 0:
                        continue
                    else:
                        MAP[wall_3_i][wall_3_j] = 1
                        safe_area = bfs_virus()
                        if safe_area > result:
                            result = safe_area
                        MAP[wall_3_i][wall_3_j] = 0
                MAP[wall_2_i][wall_2_j] = 0
        MAP[wall_1_i][wall_1_j] = 0

print(result)