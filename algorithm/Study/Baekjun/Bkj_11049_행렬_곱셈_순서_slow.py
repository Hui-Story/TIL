import sys
input = sys.stdin.readline

N = int(input())

dp = [[3e+9] * N for _ in range(N)]
matrix = []
for i in range(N):
    r, c = map(int, input().split())
    if not i:
        matrix.append(r)
        matrix.append(c)
    else:
        matrix.append(c)

for i in range(N):
    for j in range(N-i):
        if not i:
            dp[j][j] = 0
            continue
        s, e = j, j + i
        for k in range(s, e):
            dp[s][e] = min(dp[s][e], dp[s][k] + dp[k + 1][e] + (matrix[s] * matrix[k + 1] * matrix[e + 1]))

print(dp[0][N-1])