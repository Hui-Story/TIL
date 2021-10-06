import copy

# 상어 이동
def shark_eat(shark_x, shark_y, fish, move, cnt):
    global result
    fish = copy.deepcopy(fish)
    move = copy.deepcopy(move)
    check = False  # 상어가 이동했는지 확인
    # 방향으로 1 ~ 3 칸 이동하는 경우 모두 탐색
    for i in range(1, 4):
        nx = shark_x + dx[move[shark_x][shark_y]-1] * i
        ny = shark_y + dy[move[shark_x][shark_y]-1] * i
        # 빈 공간이 아닌 경우 이동
        if 0 <= nx < 4 and 0 <= ny < 4 and fish[nx][ny] != -1:
            target_fish, shark_move = fish[nx][ny], move[shark_x][shark_y]
            fish[shark_x][shark_y], move[shark_x][shark_y] = -1, -1
            fish[nx][ny] = 0
            # 이동한 경우에 따라서 분기
            fish_move(nx, ny, fish, move, cnt+target_fish)
            fish[shark_x][shark_y], move[shark_x][shark_y] = 0, shark_move
            fish[nx][ny] = target_fish
            check = True
    # 이동할 수 없으면 현재 점수를 비교
    if not check:
        result = max(result, cnt)
        return

# 물고기 이동
def fish_move(shark_x, shark_y, fish, move, cnt):
    fish = copy.deepcopy(fish)
    move = copy.deepcopy(move)
    # 물고기 번호 순서대로 이동
    for num in range(1, 17):
        for x in range(4):
            for y in range(4):
                if fish[x][y] == num:
                    # 반시계 방향으로 45도씩 회전하며 델타탐색
                    for d_plus in range(8):
                        d = move[x][y] + d_plus
                        if d > 8:
                            d %= 8
                        nx = x + dx[d-1]
                        ny = y + dy[d-1]
                        # 상어가 없는 경우 (빈 공간 or 물고기) 이동
                        if 0 <= nx < 4 and 0 <= ny < 4 and fish[nx][ny] != 0:
                            fish[nx][ny], fish[x][y] = fish[x][y], fish[nx][ny]
                            move[nx][ny], move[x][y] = d, move[nx][ny]
                            break
                    # 이동하지 못한 경우 방향만 변경
                    else:
                        move[x][y] = d
                    break
            else:
                continue
            break
    # 물고기 이동 후 상어 이동 시작
    shark_eat(shark_x, shark_y, fish, move, cnt)


fish = [[-1]*4 for _ in range(4)]  # 물고기의 번호
move = [[-1]*4 for _ in range(4)]  # 물고기의 방향

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    inp = list(map(int, input().split()))
    for j in range(4):
        fish[i][j] = inp[j*2]
        move[i][j] = inp[j*2 + 1]

# 상어 초기 위치 설정
result = fish[0][0]
fish[0][0] = 0

# 상어가 들어간 후 물고기 이동으로 시작
fish_move(0, 0, fish, move, result)

print(result)