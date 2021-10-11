import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 상어 이동
def shark_move(move_cnt):
    global grid, direction, shark_lst, shark_cnt, new_shark_lst

    reduce_mark()  # 남아있던 냄새 지우기
    add_mark()  # 냄새 남기기

    # 남아있는 상어가 1마리인 경우 move_cnt를 리턴
    if shark_cnt == 1:
        return move_cnt
    # 시간이 1000초 지나서 2마리 이상 남아있다면 -1을 리턴
    if move_cnt >= 1000:
        return -1

    shark_cnt = 0
    # 저장된 상어의 위치에서 이동
    for num, x, y in shark_lst:
        # 저장된 위치에 해당하는 상어가 없을 경우 continue
        if grid[x][y] != num:
            continue
        # 빈 공간부터 탐색한 후 이동할 곳 이 없을 경우 본인의 냄새가 있는 곳으로 이동
        if not move_to_empty(num, x, y):
            move_to_self(num, x, y)
    
    # 상어의 위치 저장
    shark_lst = new_shark_lst[:]
    new_shark_lst.clear()

    return (shark_move(move_cnt+1))

# 빈 공간으로 이동
def move_to_empty(num, x, y):
    global new_shark_lst, shark_cnt
    # 우선순위에 따라 탐색
    for d in direction_lst[num][direction[x][y]-1]:
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N and mark[nx][ny] == 0:
            grid[x][y], direction[x][y] = 0, 0
            # 다른 상어가 없을 경우 이동 (상어 카운트 O)
            if grid[nx][ny] == 0:
                grid[nx][ny], direction[nx][ny] = num, d
                new_shark_lst.append([num, nx, ny])
                shark_cnt += 1
            # 번호가 더 큰 상어가 있을 경우 밀어내고 이동 (상어 카운트 X)
            elif grid[nx][ny] > num:
                grid[nx][ny], direction[nx][ny] = num, d
                new_shark_lst.append([num, nx, ny])
            return True
    return False

# 본인의 냄새가 있는 공간으로 이동
def move_to_self(num, x, y):
    global new_shark_lst, shark_cnt
    # 우선순위에 따라 탐색
    for d in direction_lst[num][direction[x][y]-1]:
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N and mark[nx][ny] == num:
            grid[x][y], direction[x][y] = 0, 0
            grid[nx][ny], direction[nx][ny] = num, d
            new_shark_lst.append([num, nx, ny])
            shark_cnt += 1
            return

# 냄새 지우기
def reduce_mark():
    global mark_cnt
    for x in range(N):
        for y in range(N):
            if mark_cnt[x][y] > 1:
                mark_cnt[x][y] -= 1
            elif mark_cnt[x][y] == 1:
                mark_cnt[x][y] = 0
                mark[x][y] = 0

# 냄새 남기기
def add_mark():
    for num, x, y in shark_lst:
        mark[x][y] = num
        mark_cnt[x][y] = k


N, M, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]  # 상어가 있는 격자
direction_inp = list(map(int, input().split()))
direction = [[0]*N for _ in range(N)]  # 상어의 현재 방향
mark = [[0]*N for _ in range(N)]  # 남아있는 상어의 냄새
mark_cnt = [[0]*N for _ in range(N)]  # 상어의 냄새가 지워지기까지 남은 시간

shark_lst = []  # 상어의 위치 저장
shark_cnt = M  # 남아있는 상어의 숫자 저장
new_shark_lst = []
direction_lst = [[[0]*4 for _ in range(4)] for _ in range(M + 1)]  # 상어의 방향에 따른 우선순위

# 상어의 초기 방향과 위치 저장
for x in range(N):
    for y in range(N):
        if grid[x][y]:
            direction[x][y] = direction_inp[grid[x][y] - 1]
            shark_lst.append([grid[x][y], x, y])

# 우선순위 리스트로 저장
for num in range(1, M+1):
    for d in range(4):
        direction_lst[num][d] = list(map(int, input().split()))

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

print(shark_move(0))