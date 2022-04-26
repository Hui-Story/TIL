import sys
input = sys.stdin.readline

T, W = map(int, input().split())
tree = [int(input()) for _ in range(T)]

dp = [[0] * (W + 2) for _ in range(T + 1)]

for i in range(1, T + 1):
    for j in range(1, W + 2):
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])
        if j % 2 == tree[i - 1] % 2:
            dp[i][j] += 1

print(max(dp[-1]))