import sys
input = sys.stdin.readline

R, C = map(int, input().split())
MAP = [list(input().strip()) for _ in range(R)]

dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)

for x in range(R):
    for y in range(C):
        if MAP[x][y] == 'W':
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < R and 0 <= ny < C and MAP[nx][ny] == 'S':
                    print(0)
                    exit()
        elif MAP[x][y] == '.':
            MAP[x][y] = 'D'

print(1)
for x in range(R):
    print(''.join(MAP[x]))