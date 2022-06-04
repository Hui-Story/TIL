N = int(input())

# (L, A) : (0, 0), (1, 0), (1, 1), (1, 2), (0, 1), (0, 2)
dp = [[0] * 6 for _ in range(N + 1)]
dp[0][0] = 1

for i in range(1, N + 1):
    # 출석
    for j in range(3):
        dp[i][0] += dp[i - 1][j]
    for j in range(3, 6):
        dp[i][3] += dp[i - 1][j]
    # 지각
    for j in range(3):
        dp[i][3] += dp[i - 1][j]
    # 결석
    for j in (0, 1, 3, 4):
        dp[i][j + 1] += dp[i - 1][j]

print(sum(dp[N]) % 1000000)