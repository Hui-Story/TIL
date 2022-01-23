import sys
input = sys.stdin.readline

def explode():
    global field, visited
    explode_check = False
    for j in range(6):
        for i in range(11, -1, -1):
            if field[i][j] != '.' and not visited[i][j]:
                visited[i][j] = 1
                if check(i, j, field[i][j]):
                    explode_check = True
    return explode_check

def check(i, j, color):
    global field, visited
    idx = cnt = 0
    que = []
    que.append((i, j))
    while idx < len(que):
        x, y = que[idx]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny] and field[nx][ny] == color:
                visited[nx][ny] = 1
                que.append((nx, ny))
        idx += 1
        cnt += 1
    if cnt >= 4:
        for x, y in que:
            field[x][y] = '.'
        return True
    else:
        return False

def drop():
    global field
    for j in range(6):
        h = 11
        for i in range(11, -1, -1):
            color = field[i][j]
            if color != '.':
                field[i][j] = '.'
                field[h][j] = color
                h -= 1


field = [list(input().strip()) for _ in range(12)]

dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
visited = [[0] * 6 for _ in range(12)]
result = 0

while explode():
    drop()
    visited = [[0] * 6 for _ in range(12)]
    result += 1

print(result)