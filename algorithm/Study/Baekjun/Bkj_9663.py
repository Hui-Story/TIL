import sys
input = sys.stdin.readline

def N_Queen(j, used):
    global N, MAP, result
    if j == N:
        result += 1
        return
    for i in range(N):
        if used[i] == 0 and check(i, j):
            used[i] = 1
            MAP[i][j] = 1
            N_Queen(j+1, used)
            used[i] = 0
            MAP[i][j] = 0
        else:
            continue
    return

def check(i, j):
    global N, MAP
    for k in range(2):
        x, y = i, j
        for _ in range(N):
            x += dx[k]
            y += dy[k]
            if 0 <= x < N and 0 <= y < N and MAP[x][y] == 1:
                return False
            elif 0 <= x < N and 0 <= y < N and MAP[x][y] == 0:
                continue
            else:
                break
    return True

N = int(input())

used = [0] * N
MAP = [[0] * N for _ in range(N)]

dx = [1, -1]
dy = [-1, -1]
result = 0

N_Queen(0, used)
print(result)