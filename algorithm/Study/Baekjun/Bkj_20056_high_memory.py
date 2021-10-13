import sys, copy
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 파이어볼 이동
def fire_move(grid, cnt):
    global new_grid
    # K 번 이동한 후 질량 합산
    if cnt >= K:
        score(grid)
        return
    new_grid = [[[] for _ in range(N)] for _ in range(N)]  # 이동한 파이어볼을 저장할 grid
    for x in range(N):
        for y in range(N):
            # 칸이 N 에서 1 로 넘어가는 것을 고려하여 이동한 파이어볼을 저장
            for f in grid[x][y]:
                fs, fd = f[1], f[2]
                nx = (x + dx[fd]*fs) % N
                ny = (y + dy[fd]*fs) % N
                new_grid[nx][ny].append(f)

    merge_fire(new_grid)
    fire_move(new_grid, cnt+1)

# 2 개 이상의 파이어볼 합치기
def merge_fire(grid):
    for x in range(N):
        for y in range(N):
            # 파이어볼이 2 개 이상 있을 경우
            if len(grid[x][y]) >= 2:
                m = s = num_check = cnt = 0  # 총 질량, 속력, 홀/짝 여부, 갯수 카운트
                for f in grid[x][y]:
                    fm, fs, fd = f[0], f[1], f[2]
                    m += fm
                    s += fs
                    cnt += 1
                    # 홀/짝이 함께 존재하는 경우 num_check는 3
                    if num_check != 3:
                        if fd % 2:
                            if num_check == 2:
                                num_check = 3
                            else:
                                num_check = 1
                        else:
                            if num_check == 1:
                                num_check = 3
                            else:
                                num_check = 2
                # 합쳐지는 파이어볼 지우기
                grid[x][y].clear()
                # 질량이 0 이 아닌 경우 나누어진 파이어볼 생성
                if m >= 5:
                    divide_fire(grid, num_check, m//5, s//cnt, x, y)

# 파이어볼 4 개로 나누기
def divide_fire(grid, num_check, m, s, x, y):
    # 홀/짝 함께 존재
    if num_check == 3:
        for d in range(1, 8, 2):
            grid[x][y].append([m, s, d])
    # 모두 홀수이거나 모두 짝수
    else:
        for d in range(0, 7, 2):
            grid[x][y].append([m, s, d])

# 남은 파이어볼의 질량을 합산
def score(grid):
    global result
    for x in range(N):
        for y in range(N):
            for f in grid[x][y]:
                result += f[0]


N, M, K = map(int, input().split())
grid = [[[] for _ in range(N)] for _ in range(N)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

result = 0

# grid에 파이어볼의 'm, s, d' 입력 (3 차원 배열)
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    grid[r-1][c-1].append([m, s, d])

fire_move(grid, 0)

print(result)