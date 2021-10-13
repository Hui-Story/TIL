import sys
input = sys.stdin.readline

# 구름 이동
def move_cloud(d, s):
    global grid, pre_cloud
    for i in range(len(clouds)):
        clouds[i][0] = (clouds[i][0] + dx[d-1]*s) % N
        clouds[i][1] = (clouds[i][1] + dy[d-1]*s) % N
        grid[clouds[i][0]][clouds[i][1]] += 1
        pre_cloud[clouds[i][0]][clouds[i][1]] += 1

# 물복사
def copy_water():
    for x, y in clouds:
        for d in range(1, 8, 2):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny]:
                grid[x][y] += 1

# 구름 생성
def create_cloud():
    for x in range(N):
        for y in range(N):
            # 이전에 구름이 존재하지 않았을 경우
            if grid[x][y] >= 2 and not pre_cloud[x][y]:
                grid[x][y] -= 2
                clouds.append([x, y])
            # 이전에 존재했던 구름 초기화
            if pre_cloud[x][y]:
                pre_cloud[x][y] = 0


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]  # 구름의 위치 저장
pre_cloud = [[0]*N for _ in range(N)]  # 이전에 존재했던 구름 위치 저장

result = 0

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(M):
    d, s = map(int, input().split())
    move_cloud(d, s)
    copy_water()
    clouds.clear()  # 이전의 구름 삭제
    create_cloud()

# 물의 양 합산
for i in grid:
    result += sum(i)

print(result)