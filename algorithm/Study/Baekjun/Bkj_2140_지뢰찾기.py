import sys
input = sys.stdin.readline

N = int(input())
MAP = [list(input().strip()) for _ in range(N)]

if N <= 2:
    print(0)
    exit()

if N >= 5:
    result = (N - 4) * (N - 4)
else:
    result = 0
dx, dy = (-1, -1, -1, 0, 1, 1, 1, 0), (-1, 0, 1, 1, 1, 0, -1, -1)

for x in range(N):
    for y in range(N):
        if MAP[x][y] != '#' and MAP[x][y] != '*' and MAP[x][y] != '':
            bomb_cnt = int(MAP[x][y])
            for d in range(8):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < N and 0 <= ny < N:
                    if MAP[nx][ny] == '*':
                        bomb_cnt -= 1
                    elif MAP[nx][ny] == '#':
                        bx, by = nx, ny
            if bomb_cnt:
                MAP[bx][by] = '*'
                result += 1
            else:
                if MAP[bx][by] == '#':
                    MAP[bx][by] = ''

print(result)