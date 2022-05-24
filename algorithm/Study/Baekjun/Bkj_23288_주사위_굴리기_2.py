import sys, collections
input = sys.stdin.readline

# 위치에 따른 점수 계산
def init_SMAP():
    global SMAP, deq
    for i in range(N):
        for j in range(M):
            if not SMAP[i][j]:
                num = MAP[i][j]
                fill_lst = []
                deq.append((i, j))
                SMAP[i][j] = 1
                while deq:
                    x, y = deq.popleft()
                    fill_lst.append((x, y))
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < N and 0 <= ny < M and not SMAP[nx][ny] and MAP[nx][ny] == num:
                            SMAP[nx][ny] = 1
                            deq.append((nx, ny))
                cnt = len(fill_lst)
                for x, y in fill_lst:
                    SMAP[x][y] = num * cnt

# 주사위 위치 이동 체크
def move_dice():
    global x, y, d_idx
    x += dx[d_idx]
    y += dy[d_idx]
    if 0 <= x < N and 0 <= y < M:
        return
    x -= dx[d_idx] * 2
    y -= dy[d_idx] * 2
    d_idx = (d_idx + 2) % 4

# 주사위 배열 회전
def turn_dice(d: int):
    global dice
    if d == 0:
        dice[2] = dice[2][1:] + [dice[2][1]]
        dice[0][2] = dice[2][0]
        dice[4][2] = dice[2][0]
    elif d == 1:
        for i in range(4):
            dice[i][2] = dice[i + 1][2]
        dice[4][2] = dice[0][2]
        dice[2][0] = dice[0][2]
        dice[2][4] = dice[0][2]
    elif d == 2:
        dice[2] = [dice[2][3]] + dice[2][:4]
        dice[0][2] = dice[2][0]
        dice[4][2] = dice[2][0]
    elif d == 3:
        for i in range(4, 0, -1):
            dice[i][2] = dice[i - 1][2]
        dice[0][2] = dice[4][2]
        dice[2][0] = dice[0][2]
        dice[2][4] = dice[0][2]

# 점수 계산
def get_score(x: int, y: int):
    global result
    result += SMAP[x][y]

# 다음 회전 방향 체크
def check_d_idx(x: int, y: int):
    global d_idx
    if dice[2][2] > MAP[x][y]:
        d_idx = (d_idx + 1) % 4
    elif dice[2][2] < MAP[x][y]:
        d_idx -= 1
        if d_idx < 0:
            d_idx = 3

N, M, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
SMAP = [[0] * M for _ in range(N)]
d_idx = 0
dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
dice = [[0, 0, 1, 0, 0],
        [0, 0, 2, 0, 0],
        [1, 4, 6, 3, 1],
        [0, 0, 5, 0, 0],
        [0, 0, 1, 0, 0]]
result = 0

deq = collections.deque()

x = y = 0
init_SMAP()
for _ in range(K):
    move_dice()
    get_score(x, y)
    turn_dice(d_idx)
    check_d_idx(x, y)

print(result)