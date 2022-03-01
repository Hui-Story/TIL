import sys
input = sys.stdin.readline

N = int(input())
vertexs = [tuple(map(int, input().split())) for _ in range(N)]
area = 0

for i in range(1, N):
    area += vertexs[i - 1][0] * vertexs[i][1] - vertexs[i - 1][1] * vertexs[i][0]
area += vertexs[-1][0] * vertexs[0][1] - vertexs[-1][1] * vertexs[0][0]

print(round(abs(area) / 2, 1))