N = int(input())

papers = [list(map(int, input().split())) for _ in range(N)]

MAP = [[0]*100 for _ in range(100)]

result = 0

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for paper in papers:
    for i in range(paper[0], paper[0]+10):
        for j in range(100-paper[1]-1, (100-paper[1]-1)-10, -1):
            MAP[i][j] = 1

for i in range(100):
    for j in range(100):
        for d in range(4):
            if MAP[i][j] == 0:
                x = i + dx[d]
                y = j + dy[d]
                if 0 <= x < 100 and 0 <= y < 100 and MAP[x][y] == 1:
                    result += 1
            elif MAP[i][j] == 1:
                x = i + dx[d]
                y = j + dy[d]
                if 0 <= x < 100 and 0 <= y < 100:
                    continue
                else:
                    result += 1

print(result)