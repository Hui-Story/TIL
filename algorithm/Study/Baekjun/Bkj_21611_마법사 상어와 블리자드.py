import sys
from collections import deque
input = sys.stdin.readline

# 그리드를 1차원 배열으로 변환
def grid_to_1d(x, y):
    for i in range(1, N):
        if i % 2:
            for d in range(2):
                for _ in range(i):
                    x = x + dx[d]
                    y = y + dy[d]
                    # 비어있는 경우 탐색을 중단하고 리턴
                    if grid[x][y] == 0:
                        return
                    balls.append(grid[x][y])
        else:
            for d in range(2, 4):
                for _ in range(i):
                    x = x + dx[d]
                    y = y + dy[d]
                    if grid[x][y] == 0:
                        return
                    balls.append(grid[x][y])
    for i in range(N-1):
        x = x + dx[0]
        y = y + dy[0]
        if grid[x][y] == 0:
            return
        balls.append(grid[x][y])

# 얼음 파편 던지기
def blizzard(d, s):
    global balls, new_balls, remove_lst

    new_balls = []
    d_idx = di[d-1]  # 상어와 인접한 칸 중 방향에 해당하는 인덱스
    ds = di[d-1] + 1  # 계차수열의 첫째항

    # d_idx 부터 일반항이 'ds + 8n'인 계차수열을 remove_lst에 입력
    for i in range(ds, 8*(s-1) + ds + 1, 8):
        if i == di[d-1] + 1:
            remove_lst.append(d_idx)
        else:
            d_idx += i
            remove_lst.append(d_idx)

    # remove_lst에 해당하는 인덱스는 얼음 파편에 의해 파괴된 구슬을 표시
    for i in range(len(balls)):
        # remove_lst에 저장된 인덱스를 제외하고 new_balls에 저장
        if remove_lst and i == remove_lst[0]:
            remove_lst.popleft()
            continue
        new_balls.append(balls[i])
    
    balls = []
    remove_lst.clear()

def explode():
    global balls, new_balls, remove_lst, result

    check = False  # 연속하여 폭팔한 구슬이 있는지 확인
    non_explode_balls = deque()  # 폭팔하지 않고 남은 구슬
    cnt = 0
    for i in range(len(new_balls)):
        if i == 0:
            cnt += 1
            non_explode_balls.append(new_balls[i])
            continue
        if new_balls[i] == non_explode_balls[-1]:
            cnt += 1
            non_explode_balls.append(new_balls[i])
        else:
            # 이전의 구슬과 번호가 다르면서, 이전 구슬 번호가 4번 이상 나온 경우
            if cnt >= 4:
                # 파괴된 구슬을 결과값에 합산하고, non_explode_balls에서 pop
                check = True
                result += cnt * non_explode_balls[-1]
                for _ in range(cnt):
                    non_explode_balls.pop()
            cnt = 1
            non_explode_balls.append(new_balls[i])
    # 마지막 구슬이 연속된 구슬인 경우 처리
    if cnt >= 4:
        check = True
        result += cnt * non_explode_balls[-1]
        for _ in range(cnt):
            non_explode_balls.pop()

    # 남은 구슬을 new_balls에 복사
    new_balls = list(non_explode_balls)[:]

    # 폭팔한 구슬이 있다면 다시 연속하는 구슬을 탐색
    if check:
        explode()

# 구슬 변환
def change():
    global balls, new_balls

    cnt = 0
    for i in range(len(new_balls)):
        # 구슬이 그리드의 갯수를 넘어가는 경우 break
        if len(balls) >= (N**2 - 2):
            break
        if i == 0:
            cnt += 1
            continue
        if new_balls[i] == new_balls[i-1]:
            cnt += 1
        else:
            balls.append(cnt)
            balls.append(new_balls[i-1])
            cnt = 1
    # 그리드에 공간이 남아있는 경우 마지막 구슬 처리
    if len(balls) < (N**2 - 2):
        balls.append(cnt)
        balls.append(new_balls[-1])


N, M = map(int, input().strip().split())
grid = [list(map(int, input().strip().split())) for _ in range(N)]
balls = []  # 그리드를 1차원 배열으로 입력할 리스트
new_balls = []  # 구슬의 변화를 임시로 저장
remove_lst = deque()  # 삭제되는 구슬
result = 0

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
di = [6, 2, 0, 4]  # 상어를 중심으로 1차원 배열에서 '상하좌우'에 해당하는 인덱스


grid_to_1d(N//2, N//2)  # 중심부터 나선 방향으로 그리드를 1차원 배열으로 변환

for _ in range(M):
    d, s = map(int, input().strip().split())
    blizzard(d, s)  # 얼음 파편
    explode()  # 연속된 구슬 폭파
    # 구슬이 남아있을 경우 변화
    if new_balls:
        change()

print(result)