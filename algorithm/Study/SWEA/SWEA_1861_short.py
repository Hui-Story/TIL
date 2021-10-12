
def dfs(x, y):
    global memo, max_room_num, max_move
    check = False
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N and rooms[x][y] == rooms[nx][ny] + 1 and not memo[nx][ny]:
            memo[nx][ny] = memo[x][y] + 1
            dfs(nx, ny)
            check = True
    if not check:
        if memo[x][y] > max_move:
            max_room_num = rooms[x][y]
            max_move = memo[x][y]
        elif memo[x][y] == max_move and rooms[x][y] < max_room_num:
            max_room_num = rooms[x][y]


T = int(input())

for case in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    memo = [[0]*N for _ in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    max_room_num = 0
    max_move = 0

    for x in range(N):
        for y in range(N):
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < N and 0 <= ny < N:
                    if rooms[x][y] == rooms[nx][ny] - 1:
                        break
            else:
                memo[x][y] = 1
                dfs(x, y)

    print('#{} {} {}'.format(case, max_room_num, max_move))