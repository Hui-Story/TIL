import sys
input = sys.stdin.readline

T = int(input())

for case in range(T):
    N = int(input())

    dp = [[0]*(N+1) for _ in range(N+1)]

    for i in range(1, N+1):
        if i == 1 or i == 2:
            dp[i][i] = 1
        else:
            for j in range(1, N+1):
                if i == j:
                    dp[i][j] = 1
                else:
                    for k in range(j+1, (i-j+1)//2):
                        dp[i][j] += dp[i-j][k]
                    dp[i][j] += 1
    for i in range(1, N+1):
        print(dp[i])
                    
    print(sum(dp[N]) % 100999)