def search(x, y):
    global dp
    for d in range(2):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < N and ny < N and dp[x][y] + board[nx][ny] < dp[nx][ny]:
            dp[nx][ny] = dp[x][y] + board[nx][ny]
            search(nx, ny)


T = int(input())

for case in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    dp = [[2e+10]*N for _ in range(N)]
    dp[0][0] = board[0][0]

    dx = [1, 0]
    dy = [0, 1]

    search(0, 0)

    print('#{} {}'.format(case, dp[N-1][N-1]))