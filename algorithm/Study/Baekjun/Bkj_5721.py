import sys
input = sys.stdin.readline

while True:
    M, N = map(int, input().split())
    if M == N == 0:
        break

    dp = [[0]*2 + list(map(int, input().split())) for _ in range(M)]

    dp2 = [0]*(M+2)

    for i in range(M):
        for j in range(2, N+2):
            dp[i][j] = max(dp[i][j-2]+dp[i][j], dp[i][j-1])
        dp2[i+2] += dp[i][N+1]

    for i in range(2, M+2):
        dp2[i] = max(dp2[i-2]+dp2[i], dp2[i-1])
    
    print(dp2[M+1])