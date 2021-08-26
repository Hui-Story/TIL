N = int(input())

papers = [list(map(int, input().split())) for _ in range(N)]

MAP = [[0]*100 for _ in range(100)]

result = 0

for paper in papers:
    for i in range(paper[0], paper[0]+10):
        for j in range(paper[1], paper[1]-10, -1):
            MAP[i][j] = 1

for i in range(100):
    result += sum(MAP[i])

print(result)