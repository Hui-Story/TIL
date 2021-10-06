from collections import deque
import copy

# 오토 플레이
def auto_play():
    global grid, deq, result
    block_delete = []  # 최종적으로 제거할 블록 리스트
    max_rainbow = 0  # 레인보우 최대 갯수
    # 일반 블록 1번부터 그룹 탐색
    for num in range(1, M+1):
        visited = [[0]*N for _ in range(N)]
        for x in range(N):
            for y in range(N):
                # 탐색하는 번호에 해당하고 탐색하지 않은 경우
                if num == grid[x][y] and not visited[x][y]:
                    visited[x][y] = 1
                    deq.append([x, y])
                    block_group = [[x, y]]  # 현재 블록이 포함되는 그룹 초기화
                    rainbow = 0  # 현재 그룹의 레인보우 갯수 초기화
                    # bfs로 그룹 탐색
                    while deq:
                        qx, qy = deq.popleft()
                        for d in range(4):
                            nqx = qx + dx[d]
                            nqy = qy + dy[d]
                            if 0 <= nqx < N and 0 <= nqy < N and not visited[nqx][nqy]:
                                # 검은색 블록이 아닌 경우 그룹에 추가
                                if grid[nqx][nqy] in [0, num]:
                                    # 레인보우인 경우 카운트
                                    if grid[nqx][nqy] == 0:
                                        rainbow += 1
                                    visited[nqx][nqy] = 1
                                    deq.append([nqx, nqy])
                                    block_group.append([nqx, nqy])
                    # 현재 그룹이 최대 크기인 경우
                    if len(block_group) > len(block_delete):
                        block_delete = copy.deepcopy(block_group)
                        max_rainbow = rainbow
                    # 현재 그룹이 최대 그룹과 크기가 같은 경우
                    elif len(block_group) == len(block_delete):
                        # 레인보우 갯수가 더 많은 경우
                        if rainbow > max_rainbow:
                            block_delete = copy.deepcopy(block_group)
                            max_rainbow = rainbow
                        # 레인보우 갯수가 같은 경우
                        elif rainbow == max_rainbow:
                            # 현재 행이 더욱 큰 경우
                            if block_delete[0][0] < x:
                                block_delete = copy.deepcopy(block_group)
                                max_rainbow = rainbow
                            # 행이 같고 현재 열이 더욱 큰 경우
                            elif block_delete[0][0] == x and block_delete[0][1] < y:
                                block_delete = copy.deepcopy(block_group)
                                max_rainbow = rainbow

    # 가장 큰 그룹의 블록이 부족한 경우 (그룹이 없는 경우)
    if len(block_delete) <= 1:
        return False

    # 점수를 계산하고 그룹의 블록 제거
    result += len(block_delete)**2
    for x, y in block_delete:
        grid[x][y] = -2

    gravity()  # 중력 작용
    rotate()  # 90도 반시계 회전
    gravity()  # 중력 작용

    return True

# 중력 작용
def gravity():
    global grid
    # 격자의 아래부터 탐색
    for x in range(N-2, -1, -1):
        for y in range(N):
            # 검은색 블록이나 빈 공간이 아닌 경우
            if grid[x][y] not in [-1, -2]:
                move = 0
                for n in range(1, N):
                    nx = x + n
                    if nx < N and grid[nx][y] == -2:
                        move = n
                    else:
                        break
                # 움직일 공간이 있을 경우 중력 적용
                if move:
                    grid[x][y], grid[x+move][y] = grid[x+move][y], grid[x][y]

# 90도 반시계 회전
def rotate():
    global grid
    new_grid = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_grid[i][j] = grid[j][N-1-i]
    grid = copy.deepcopy(new_grid)


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

deq = deque()
result = 0

# 블록 그룹이 없어질 때 까지 오토 플레이
while True:
    if not auto_play():
        break

print(result)