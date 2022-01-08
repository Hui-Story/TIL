import sys
input = sys.stdin.readline

M, N = map(int, input().split())
K = int(input())
MAP = [input().strip() for _ in range(M)]
dic = {'J': 0, 'O': 1, 'I': 2}

prefix_sum = [[[0, 0, 0] for _ in range(N+1)] for _ in range(M+1)]
for i in range(1, M+1):
    for j in range(1, N+1):
        prefix_sum[i][j][dic[MAP[i-1][j-1]]] = 1
        for k in range(3):
            prefix_sum[i][j][k] += prefix_sum[i][j-1][k]
            prefix_sum[i][j-1][k] += prefix_sum[i-1][j-1][k]
for i in range(1, M+1):
    for k in range(3):
        prefix_sum[i][N][k] += prefix_sum[i-1][N][k]
        
for _ in range(K):
    a, b, c, d = map(int, input().split())
    print(prefix_sum[c][d][0] - prefix_sum[a-1][d][0] - prefix_sum[c][b-1][0] + prefix_sum[a-1][b-1][0],
          prefix_sum[c][d][1] - prefix_sum[a-1][d][1] - prefix_sum[c][b-1][1] + prefix_sum[a-1][b-1][1],
          prefix_sum[c][d][2] - prefix_sum[a-1][d][2] - prefix_sum[c][b-1][2] + prefix_sum[a-1][b-1][2])