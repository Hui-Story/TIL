import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
dist = [[[0 for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
    inp = list(map(int, input().split()))
    for j in range(1, N+1):
        if inp[j-1]:
            dist[i][j][0] = inp[j-1]
        elif i != j:
            dist[i][j][0] = 2e+10

for k in range(1, N+1):
    for i in range(1, N):
        for j in range(i+1, N+1):
            dist[i][j][k] = min(dist[i][j][k-1], dist[i][k][k-1] + dist[k][j][k-1])
            dist[j][i][k] = min(dist[i][j][k-1], dist[i][k][k-1] + dist[k][j][k-1])

for _ in range(Q):
    C, s, e = map(int, input().split())
    if dist[s][e][C-1] != 2e+10:
        print(dist[s][e][C-1])
    else:
        print(-1)