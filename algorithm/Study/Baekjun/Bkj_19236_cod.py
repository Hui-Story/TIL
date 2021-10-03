import copy

def shark_eat(shark_x, shark_y, fish, move, cnt):
    global result
    fish = copy.deepcopy(fish)
    move = copy.deepcopy(move)
    check = False
    for i in range(1, 4):
        nx = shark_x + dx[move[shark_x][shark_y]-1] * i
        ny = shark_y + dy[move[shark_x][shark_y]-1] * i
        if 0 <= nx < 4 and 0 <= ny < 4 and fish[nx][ny] != -1:
            target_fish, shark_move = fish[nx][ny], move[shark_x][shark_y]
            fish[shark_x][shark_y], move[shark_x][shark_y] = -1, -1
            fish[nx][ny] = 0
            fish_move(nx, ny, fish, move, cnt+target_fish)
            fish[shark_x][shark_y], move[shark_x][shark_y] = 0, shark_move
            fish[nx][ny] = target_fish
            check = True
    if not check:
        result = max(result, cnt)
        return

def fish_move(shark_x, shark_y, fish, move, cnt):
    fish = copy.deepcopy(fish)
    move = copy.deepcopy(move)
    for num in range(1, 17):
        for x in range(4):
            for y in range(4):
                if fish[x][y] == num:
                    for d_plus in range(8):
                        d = move[x][y] + d_plus
                        if d > 8:
                            d %= 8
                        nx = x + dx[d-1]
                        ny = y + dy[d-1]
                        if 0 <= nx < 4 and 0 <= ny < 4 and fish[nx][ny] != 0:
                            fish[nx][ny], fish[x][y] = fish[x][y], fish[nx][ny]
                            move[nx][ny], move[x][y] = d, move[nx][ny]
                            break
                    else:
                        move[x][y] = d
                    break
            else:
                continue
            break
    shark_eat(shark_x, shark_y, fish, move, cnt)


fish = [[-1]*4 for _ in range(4)]
move = [[-1]*4 for _ in range(4)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    inp = list(map(int, input().split()))
    for j in range(4):
        fish[i][j] = inp[j*2]
        move[i][j] = inp[j*2 + 1]

result = fish[0][0]
fish[0][0] = 0

fish_move(0, 0, fish, move, result)

print(result)