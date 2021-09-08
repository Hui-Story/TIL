import sys
input = sys.stdin.readline

N = int(input())

T = []
P = []
dp = [0]*(N+1)
for _ in range(N):
    T_i, P_i = map(int, input().split())
    T.append(T_i)
    P.append(P_i)

for i in range(N-1, -1, -1):
    if T[i] == 1:
        dp[i] = P[i] + dp[i+1]
    elif T[i] <= N-i:
        dp[i] = max(dp[i+1], P[i]+dp[i+T[i]])
    else:
        dp[i] = dp[i+1]

print(dp[0])