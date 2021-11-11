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

# 뒤에서부터 dp 를 시행하여 앞으로 P 값을 누적시켜 나감
for i in range(N-1, -1, -1):
    # 하루만에 끝나는 경우 바로 추가
    if T[i] == 1:
        dp[i] = P[i] + dp[i+1]
    # 주어진 기간 내에 끝나는 경우
    elif T[i] <= N-i:
        # '시행한 경우, 시행하지 않은 경우'에서 큰 값을 결정
        dp[i] = max(dp[i+1], P[i]+dp[i+T[i]])
    else:
        dp[i] = dp[i+1]

print(dp[0])