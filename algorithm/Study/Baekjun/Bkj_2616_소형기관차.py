from itertools import accumulate

N = int(input())
passengers = list(accumulate(map(int, input().split())))
max_train = int(input())

prefix_sum = passengers[:]
dp = [[0] * (N - max_train + 1) for _ in range(3)]

for i in range(max_train, N):
    passengers[i] -= prefix_sum[i - max_train]

for i in range(3):
    if not i:
        for j in range(N - max_train + 1):
            dp[i][j] = max(dp[i][j - 1], passengers[j + max_train - 1])
    else:
        for j in range(max_train * i, N - max_train + 1):
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - max_train] + passengers[j + max_train - 1])

print(dp[-1][-1])