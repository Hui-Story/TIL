T = int(input())
n = list(int(input()) for _ in range(T))

for i in n:
    dp = [0, 1, 2, 4]
    if i <= 3:
        print(dp[i])
    else:
        for j in range(4, i+1):
            dp.append(dp[j-3] + dp[j-2] + dp[j-1])
        print(dp[i])