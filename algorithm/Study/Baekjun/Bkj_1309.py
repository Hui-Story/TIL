N = int(input())

dp = [3, 7, 0]
for i in range(2, N):
    dp[2] = dp[0] + dp[1]*2
    dp[0] = dp[1]
    dp[1] = dp[2]

if N == 1:
    print(3)
elif N == 2:
    print(7)
elif N > 2:
    print(dp[2] % 9901)