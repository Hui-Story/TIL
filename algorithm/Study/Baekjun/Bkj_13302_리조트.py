N, M = map(int, input().split())

if M:
    off = list(map(int, input().split()))
else:
    off = []

dp = [[2e+10]*(N+5) for _ in range((N//5)*2 + 4)]

dp[0][0] = 0

for j in range(N):
    for i in range((N//5)*2 + 2):
        if dp[i][j] >= 2e+9:
            continue
        if j+1 in off:
            dp[i][j+1] = min(dp[i][j+1], dp[i][j])
        if i >= 3:
            dp[i-3][j+1] = min(dp[i-3][j+1], dp[i][j])
        dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 10000)
        for d in range(1, 4):
            dp[i+1][j+d] = min(dp[i+1][j+d], dp[i][j] + 25000)
        for d in range(1, 6):
            dp[i+2][j+d] = min(dp[i+2][j+d], dp[i][j] + 37000)

print(min(list(zip(*dp))[N]))