import copy

def play(cnt, bricks):
    if cnt >= N:
        score(bricks)
        return
    check = False
    for y in range(W):
        for x in range(H):
            if bricks[x][y]:
                shoot(x, y, bricks, cnt)
                check = True
                break
    if not check:
        play(cnt+1, bricks)

def shoot(x, y, bricks, cnt):
    now_bricks = copy.deepcopy(bricks)
    break_brick(x, y, now_bricks)
    gravity(now_bricks)
    play(cnt+1, now_bricks)

def break_brick(x, y, bricks):
    re = bricks[x][y]
    bricks[x][y] = 0
    if re > 1:
        for d in range(4):
            for r in range(1, re):
                nx = x + dx[d]*r
                ny = y + dy[d]*r
                if 0 <= nx < H and 0 <= ny < W and bricks[nx][ny]:
                    break_brick(nx, ny, bricks)

def gravity(bricks):
    for x in range(H-1, -1, -1):
        for y in range(W):
            for g in range(1, H+1):
                if x+g >= H or bricks[x+g][y]:
                    bricks[x][y], bricks[x+g-1][y] = bricks[x+g-1][y], bricks[x][y]
                    break

def score(bricks):
    global result
    cnt = 0
    for i in range(H):
        for j in range(W):
            if bricks[i][j]:
                cnt += 1
    result = min(result, cnt)


T = int(input())

for case in range(1, T+1):
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    result = 2e+10
    play(0, bricks)

    print('#{} {}'.format(case, result))