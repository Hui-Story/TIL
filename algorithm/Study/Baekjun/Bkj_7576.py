import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
q = deque()
for y in range(M):
    for x in range(N):
        if box[y][x] == 1:
            q.append([x, y])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while True:
    if q:
        i, j = q.popleft()
    else:
        print(-1)
        break

    for d in range(4):
        x = i + dx[d]
        y = j + dy[d]
        if (0 <= x < N) and (0 <= y < M) and box[y][x] == 0:
            q.append([x, y])
            box[y][x] = box[j][i] + 1
    if not q:
        count = 0
        for y in range(M):
            for x in range(N):
                if box[y][x] == 0:
                    count += 1
        if count >= 1:
            print(-1)
        elif count == 0:
            print(box[j][i] - 1)
        break