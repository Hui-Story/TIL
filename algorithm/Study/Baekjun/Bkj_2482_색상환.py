N = int(input())
K = int(input())

if K > (N / 2):
    print(0)
    exit()

dp = [[i for i in range(2, N + 1)]] + [[0] * (N - 1) for _ in range(K - 1)]

for i in range(1, K):
    for j in range(2, N - 1):
        dp[i][j] = dp[i - 1][j - 2] + dp[i][j - 1]

print(dp[-1][-1] % 1000000003)