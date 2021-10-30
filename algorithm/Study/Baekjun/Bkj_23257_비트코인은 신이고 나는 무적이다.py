import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(lambda x : abs(int(x)), input().split()))
dp = [[-1]*2048 for _ in range(101)]
dp[0][0] = 0

for i in range(M):
    for j in range(2048):
        if dp[i][j] == -1:
            continue
        for a in A:
            tmp = j^a
            dp[i+1][tmp] = tmp

print(max(dp[M]))