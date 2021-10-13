import sys, math
input = sys.stdin.readline

def tornado(x, y, d):
    global result
    dust = grid[x][y]
    for t in range(10):
        # 토네이도의 방향에 따라 날아가는 모래의 상대좌표 수정
        if d == 0:
            nx = x + tx[t]
            ny = y + ty[t]
        elif d == 1:
            nx = x - ty[t]
            ny = y + tx[t]
        elif d == 2:
            nx = x - tx[t]
            ny = y - ty[t]
        elif d == 3:
            nx = x + ty[t]
            ny = y - tx[t]
        # 마지막 알파가 있는 위치에는 남은 모래가 이동
        if t == 9:
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                result += grid[x][y]
            else:
                grid[nx][ny] += grid[x][y]
            break
        grid[x][y] -= math.floor(dust * per[t])
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            result += math.floor(dust * per[t])
        else:
            grid[nx][ny] += math.floor(dust * per[t])
    # 남은 모래 제거
    grid[x][y] = 0


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
# 토네이도에 의해 날아가는 모래 위치
tx = [-1, 1, -1, 1, 0, -2, 2, -1, 1, 0]
ty = [-1, -1, 0, 0, -2, 0, 0, 1, 1, -1]
# 토네이도에 의해 날아가는 모래 비율
per = [0.1, 0.1, 0.07, 0.07, 0.05, 0.02, 0.02, 0.01, 0.01]

result = 0

# 중심 좌표
x = y = N // 2

for i in range(1, N):
    # 직선으로 움직이는 거리가 홀수인 경우 '좌-하' 이동
    if i % 2:
        for d in range(0, 2):
            for _ in range(i):
                x, y = x + dx[d], y + dy[d]
                tornado(x, y, d)
    # 직선으로 움직이는 거리가 짝수인 경우 '우-상' 이동
    else:
        for d in range(2, 4):
            for _ in range(i):
                x, y = x + dx[d], y + dy[d]
                tornado(x, y, d)
# 마지막 남은 직선 이동
for _ in range(N-1):
    x, y = x + dx[0], y + dy[0]
    tornado(x, y, 0)

print(result)