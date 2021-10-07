
def dfs(x, y, now):
    global result
    if len(now) == 7:
        result.append(now)
        return
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, now + grid[nx][ny])


T = int(input())

for case in range(1, T+1):
    grid = [list(map(str, input().split())) for _ in range(4)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    result = []

    for i in range(4):
        for j in range(4):
            dfs(i, j, grid[i][j])
    
    print('#{} {}'.format(case, len(set(result))))