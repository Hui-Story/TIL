
def dfs(x, y, cnt, sx, sy):
    global max_room_num, max_move
    check = False
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N and rooms[x][y] == rooms[nx][ny] - 1:
            dfs(nx, ny, cnt+1, sx, sy)
            check = True
    if not check:
        if cnt > max_move:
            max_room_num = rooms[sx][sy]
            max_move = cnt
        elif cnt == max_move and rooms[sx][sy] < max_room_num:
            max_room_num = rooms[sx][sy]


T = int(input())

for case in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    max_room_num = 0
    max_move = 0

    for i in range(N):
        for j in range(N):
            dfs(i, j, 1, i, j)

    print('#{} {} {}'.format(case, max_room_num, max_move))