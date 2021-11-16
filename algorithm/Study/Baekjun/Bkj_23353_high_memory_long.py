import sys
input = sys.stdin.readline

def search(x, y, d):
    global dp, result
    while True:
        bx = x - dx[d]
        by = y - dy[d]
        if 0 <= x < N and 0 <= y < N:
            if board[x][y] == 1:
                dp[x][y] = [dp[bx][by][0] + 1, dp[bx][by][1]]
            elif board[x][y] == 2:
                if board[bx][by] == 1:
                    dp[x][y] = [dp[bx][by][0] - dp[bx][by][1] + 1, dp[bx][by][0] - dp[bx][by][1] + 1]
                    result = max(result, dp[bx][by][0])
                else:
                    dp[x][y] = [1, 1]
                    result = max(result, dp[bx][by][0])
            elif board[x][y] == 0:
                if board[bx][by]:
                    result = max(result, dp[bx][by][0])
            dp[bx][by] = [0, 0]
        else:
            result = max(result, dp[bx][by][0])
            dp[bx][by] = [0, 0]
            break
        x += dx[d]
        y += dy[d]


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, 0] for _ in range(N)] for _ in range(N)]

dx = (0, 1, 1, 1)
dy = (1, 1, 0, -1)

result = 0

for i in range(N):
    if board[i][0]:
        dp[i][0][0] = 1
        if board[i][0] == 2:
            dp[i][0][1] = 1
    search(i, 1, 0)

for j in range(N):
    if board[0][j]:
        dp[0][j][0] = 1
        if board[0][j] == 2:
            dp[0][j][1] = 1
    search(1, j, 2)

for i in range(N):
    if board[i][0]:
        dp[i][0][0] = 1
        if board[i][0] == 2:
            dp[i][0][1] = 1
    search(i+1, 1, 1)
for j in range(1, N):
    if board[0][j]:
        dp[0][j][0] = 1
        if board[0][j] == 2:
            dp[0][j][1] = 1
    search(1, j+1, 1)

for i in range(N):
    if board[i][N-1]:
        dp[i][N-1][0] = 1
        if board[i][N-1] == 2:
            dp[i][N-1][1] = 1
    search(i+1, N-2, 3)
for j in range(N-1):
    if board[0][j]:
        dp[0][j][0] = 1
        if board[0][j] == 2:
            dp[0][j][1] = 1
    search(1, j-1, 3)

print(result)