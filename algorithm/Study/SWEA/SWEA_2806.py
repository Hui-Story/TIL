def n_queen(x):
    global result
    if x == N:
        result += 1
        return
    for y in range(N):
        if not used[y]:
            i = 1
            for i in range(N):
                for d in range(2):
                    nx = x + dx[d] * i
                    ny = y + dy[d] * i
                    if 0 <= nx and 0 <= ny < N:
                        if chess[nx][ny] == 1:
                            break
                else:
                    continue
                break
            else:
                used[y] = 1
                chess[x][y] = 1
                n_queen(x+1)
                used[y] = 0
                chess[x][y] = 0


T = int(input())

for case in range(1, T+1):
    N = int(input())
    chess = [[0] * N for _ in range(N)]
    used = [0] * N

    dx = [-1, -1]
    dy = [-1, 1]
    result = 0

    n_queen(0)

    print('#{} {}'.format(case, result))