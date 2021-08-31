import sys
input = sys.stdin.readline

M, N = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(M)]

dp = [[0]*(N+3) for _ in range(M+3)]

for i in range(2, M+2):
    for j in range(2, N+2):
        dp[i][j] = max(dp[i-2][j-2]+MAP[]