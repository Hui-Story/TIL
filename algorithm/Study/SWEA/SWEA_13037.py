def search(x, y, cnt):
    global result
    if x == y == N-1:
        cnt += board[x][y]
        result = min(result, cnt)
    cnt += board[x][y]
    for d in range(2):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < N and ny < N:
            search(nx, ny, cnt)

T = int(input())

for case in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = 2e+10

    dx = [1, 0]
    dy = [0, 1]

    search(0, 0, 0)

    print('#{} {}'.format(case, result))