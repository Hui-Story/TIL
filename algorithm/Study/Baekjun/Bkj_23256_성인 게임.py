import sys
input = sys.stdin.readline

T = int(input())
dp = [[4, 3]]
cnt = 1

for _ in range(T):
    N = int(input())
    while cnt < N:
        dp.append([(2*dp[cnt-1][0]+4*dp[cnt-1][1])%1000000007, (dp[cnt-1][0]+3*dp[cnt-1][1])%1000000007])
        cnt += 1
    print(sum(dp[N-1])%1000000007)