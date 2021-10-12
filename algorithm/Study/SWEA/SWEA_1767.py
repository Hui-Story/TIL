import copy

def connect(cells, cnt):
    if cnt >= len(cell_lst):
        score(cells)
        return
    now_cells = copy.deepcopy(cells)
    x, y = cell_lst[cnt]
    check = False
    for d in range(4):
        for r in range(1, N):
            nx = x + dx[d]*r
            ny = y + dy[d]*r
            if 0 <= nx < N and 0 <= ny < N and now_cells[nx][ny] != 0:
                break
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                now_cells[x][y] = 2
                for w in range(1, r):
                    now_cells[x + dx[d]*w][y + dy[d]*w] = -1
                check = True
                connect(now_cells, cnt+1)
                now_cells[x][y] = 1
                for w in range(1, r):
                    now_cells[x + dx[d]*w][y + dy[d]*w] = 0
                break
    if not check:
        connect(now_cells, cnt+1)

def score(cells):
    global max_core, result
    core_cnt = 0
    wire_cnt = 0
    for i in range(N):
        for j in range(N):
            if cells[i][j] == 2:
                core_cnt += 1
            elif cells[i][j] == -1:
                wire_cnt += 1
    if core_cnt > max_core:
        max_core = core_cnt
        result = wire_cnt
    elif core_cnt == max_core and wire_cnt < result:
        result = wire_cnt


T = int(input())

for case in range(1, T+1):
    N = int(input())
    cells = [list(map(int, input().split())) for _ in range(N)]
    cell_lst = []

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    max_core = 0
    result = 2e+10

    for i in range(N):
        for j in range(N):
            if cells[i][j] == 1:
                if i == 0 or i == N-1 or j == 0 or j == N-1:
                    cells[i][j] = 2
                else:
                    cell_lst.append([i, j])

    connect(cells, 0)

    print('#{} {}'.format(case, result))