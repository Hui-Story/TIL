
def tour(x, y, r, l):
    global result
    for _ in range(r):
        x = x + dx[0]
        y = y + dy[0]
        if 0 <= x < N and 0 <= y < N and not dessert[cafe[x][y]]:
            dessert[cafe[x][y]] = 1
        else:
            return
    for _ in range(l):
        x = x + dx[1]
        y = y + dy[1]
        if 0 <= x < N and 0 <= y < N and not dessert[cafe[x][y]]:
            dessert[cafe[x][y]] = 1
        else:
            return
    for _ in range(r):
        x = x + dx[2]
        y = y + dy[2]
        if 0 <= x < N and 0 <= y < N and not dessert[cafe[x][y]]:
            dessert[cafe[x][y]] = 1
        else:
            return
    for _ in range(l-1):
        x = x + dx[3]
        y = y + dy[3]
        if 0 <= x < N and 0 <= y < N and not dessert[cafe[x][y]]:
            dessert[cafe[x][y]] = 1
        else:
            return
    result = max(result, (r+l)*2)


T = int(input())

for case in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]

    dx = [1, 1, -1, -1]
    dy = [1, -1, -1, 1]

    result = -1

    for x in range(N):
        for y in range(N):
            for r in range(1, N-1):
                for l in range(1, N-1):
                    if (l+r) < N:
                        dessert = [0] * 101
                        dessert[cafe[x][y]] = 1
                        tour(x, y, r, l)

    print('#{} {}'.format(case, result))