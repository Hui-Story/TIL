import sys
input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

N, K = MIIS()
grid = [list(MIIS()) for _ in range(N)]
S, X, Y = MIIS()
X, Y = X - 1, Y - 1

cnt = 10001
num = 1001
for x in range(N):
    for y in range(N):
        if grid[x][y]:
            dist = abs(X - x) + abs(Y - y)
            if cnt > dist:
                cnt = dist
                num = grid[x][y]
            elif cnt == dist:
                num = min(num, grid[x][y])

if cnt <= S:
    print(num)
else:
    print(0)