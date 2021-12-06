T = int(input())

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
turn = {
    0 : 1,
    1 : 0,
    2 : 3,
    3 : 2,
}

for case in range(1, T+1):
    N, M, K = map(int, input().split())
    MAP = [[[] for _ in range(N)] for _ in range(N)]
    microbes = []
    new_microbes = []
    merge_microbe = []
    for _ in range(K):
        x, y, cnt, d = map(int, input().split())
        MAP[x][y].append([cnt, d-1])
        microbes.append([x, y])
    for _ in range(M):
        for x, y in microbes:
            cnt, d = MAP[x][y][0]
            nx = x + dx[d]
            ny = y + dy[d]
            if MAP[nx][ny] and [nx, ny] not in merge_microbe:
                merge_microbe.append([nx, ny])
            if nx == 0 or nx == N-1 or ny == 0 or ny == N-1:
                MAP[x][y][0][0] = MAP[x][y][0][0] // 2
                MAP[x][y][0][1] = turn[MAP[x][y][0][1]]
            if MAP[x][y][0][0]:
                new_microbes.append((nx, ny))
                MAP[nx][ny].append(MAP[x][y][0][:])
            MAP[x][y] = MAP[x][y][1:]
        microbes = list(set(new_microbes))
        new_microbes.clear()
        for x, y in merge_microbe:
            if len(MAP[x][y]) >= 2:
                MAP[x][y].sort(key=lambda x : x[0], reverse=True)
                new_cnt, new_d = 0, MAP[x][y][0][1]
                for cnt, d in MAP[x][y]:
                    new_cnt += cnt
                MAP[x][y].clear()
                MAP[x][y].append([new_cnt, new_d])
        merge_microbe.clear()
    result = 0
    for x, y in microbes:
        result += MAP[x][y][0][0]
    print('#{} {}'.format(case, result))