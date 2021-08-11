M, N, K = map(int, input().split())
rec_lst = [list(map(int, input().split())) for _ in range(K)]

visit = [[0] * N for _ in range(M)]
Map = [[1] * N for _ in range(M)]

for rec in rec_lst:
    for i in range(rec[0], rec[2]):
        for j in range(rec[1], rec[3]):
            if Map[j][i] == 1:
                Map[j][i] = 0

answer = 0
answer_2 = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(M):
    for j in range(N):
        if not Map[i][j] or visit[i][j]:
            continue
        stack = [[i, j]]
        visit[i][j] = 1
        count = 1
        while stack:
            p, q = stack.pop()

            for d in range(4):
                x = p + dx[d]
                y = q + dy[d]
                if 0 <= x < M and 0 <= y < N and Map[x][y] and not visit[x][y]:
                    stack.append([x, y])
                    visit[x][y] = 1
                    count += 1
        answer_2.append(count)
        answer += 1

print(answer)
print(*sorted(answer_2))