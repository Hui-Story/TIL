import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dist = [[100000] * n for _ in range(n)]

for _ in range(m):
    u, v, d = map(int, input().split())
    u, v = u-1, v-1
    if d:
        dist[u][v] = 0
        dist[v][u] = 0
    else:
        dist[u][v] = 0
        dist[v][u] = 1

for x in range(n):
    dist[x][x] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            temp = dist[i][k] + dist[k][j]
            if dist[i][j] > temp:
                dist[i][j] = temp
            # if i == j:
            #     dist[i][j] = 0
            # else:
            #     dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for _ in range(int(input())):
    s, e = map(int, input().split())
    print(dist[s-1][e-1])