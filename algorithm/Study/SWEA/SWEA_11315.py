def omok():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'o':
                for d in range(4):
                    cnt = 1
                    for k in range(1, N):
                        x = i + dx[d]*k
                        y = j + dy[d]*k
                        if 0 <= x < N and 0 <= y < N:
                            if board[x][y] == 'o':
                                cnt += 1
                            else:
                                cnt = 0
                        else:
                            break
                        if cnt >= 5:
                            return 'YES'
    return 'NO'

T = int(input())

dx = [1, 0, 1, -1]
dy = [0, 1, 1, 1]

for case in range(1, T+1):
    N = int(input())
    board = [str(input()) for _ in range(N)]

    print('#{} {}'.format(case, omok()))