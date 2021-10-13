
def play(x, y, d):
    global result
    cnt = 0
    x += dx[d]
    y += dy[d]
    while True:
        if x < 0 or x >= N or y < 0 or y >= N:
            d = (d+2) % 4
            cnt += 1
        elif (x, y) == (sx, sy) or board[x][y] == -1:
            result = max(result, cnt)
            return
        elif board[x][y] in range(1, 6):
            d = direction[board[x][y]][d]
            cnt += 1
        elif board[x][y] in range(6, 11):
            x, y = wormhole(x, y, board[x][y])
        x += dx[d]
        y += dy[d]

def wormhole(x, y, num):
    for wx, wy in wormhole_lst[num-6]:
        if wx != x or wy != y:
            return wx, wy


direction = [
    [],
    [3, 2, 0, 1],
    [2, 0, 3, 1],
    [2, 3, 1, 0],
    [1, 3, 0, 2],
    [2, 3, 0, 1]
]


T = int(input())

for case in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    wormhole_lst = [[] for _ in range(5)]

    for i in range(N):
        for j in range(N):
            if board[i][j] in [6, 7, 8, 9, 10]:
                wormhole_lst[board[i][j]-6].append([i, j])

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    result = 0

    for x in range(N):
        for y in range(N):
            if board[x][y] == 0:
                sx, sy = x, y
                for d in range(4):
                    play(x, y, d)

    print('#{} {}'.format(case, result))