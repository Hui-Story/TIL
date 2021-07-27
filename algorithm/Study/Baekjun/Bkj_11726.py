n = int(input())

dp = [1, 1, 0]
for i in range(2, n+1):
    dp[2] = dp[0] + dp[1]
    dp[0] = dp[1]
    dp[1] = dp[2]

if n == 1:
    print(1)
elif n > 1:
    print(dp[2] % 10007)