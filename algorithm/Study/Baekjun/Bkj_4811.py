import sys
input = sys.stdin.readline

while True:
    N = int(input())
    dp = [[0]*(N+1) for _ in range(N+1)]
    if N == 0:
        break
    for i in range(1, N+1):
        for j in range(0, i+1):
            if j == 0:
                dp[i][j] = 1
            elif j == 1:
                dp[i][j] = i
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp[N][N])