import sys
input = sys.stdin.readline

for _ in range(int(input())):
    K = int(input())
    files = list(map(int, input().split()))
    cost_dp = [[3e+9] * K for _ in range(K)]
    sum_dp = [[0] * K for _ in range(K)]

    for i in range(K):
        for j in range(K - i):
            if not i:
                cost_dp[j][j] = 0
                sum_dp[j][j] = files[j]
                continue
            s, e = j, j + i
            for k in range(s, e):
                sum_dp[s][e] = sum_dp[s][k] + sum_dp[k + 1][e]
                cost_dp[s][e] = min(cost_dp[s][e], cost_dp[s][k] + cost_dp[k + 1][e] + sum_dp[s][e])
    print(cost_dp[0][-1])