N = int(input())

visit = [[0] * N for _ in range(N)]
Map = [list(map(int, input())) for _ in range(N)]
answer = 0
answer_2 = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
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
                if 0 <= x < N and 0 <= y < N and Map[x][y] and not visit[x][y]:
                    stack.append([x, y])
                    visit[x][y] = 1
                    count += 1
        answer_2.append(count)
        answer += 1

print(answer)
for i in sorted(answer_2):
    print(i)