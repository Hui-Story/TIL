import sys
input = sys.stdin.readline

N, M = map(int, input().split())
MAP = [str(input()) for _ in range(N)]

dp = [[-1]*M for _ in range(N)]

O_exist = False
result = []

for j in range(M):
    for i in range(N):
        if MAP[i][j] == 'R':
            start = [i, j]
            dp[i][j] = 0
        elif MAP[i][j] == 'O':
            O_exist = True

if O_exist:
    for j in range(start[1], M-1):
        for i in range(N):
            if dp[i][j] != -1:
                if MAP[i][j+1] == '.':
                    if dp[i][j] > dp[i][j+1]:
                        dp[i][j+1] = dp[i][j]
                elif MAP[i][j+1] == 'C':
                    if dp[i][j]+1 > dp[i][j+1]:
                        dp[i][j+1] = dp[i][j]+1
                elif MAP[i][j+1] == 'O':
                    if dp[i][j] > dp[i][j+1]:
                        dp[i][j+1] = dp[i][j]
                        result.append(dp[i][j])
                if 0 <= i-1:
                    if MAP[i-1][j+1] == '.':
                        if dp[i][j] > dp[i-1][j+1]:
                            dp[i-1][j+1] = dp[i][j]
                    elif MAP[i-1][j+1] == 'C':
                        if dp[i][j]+1 > dp[i-1][j+1]:
                            dp[i-1][j+1] = dp[i][j]+1
                    elif MAP[i-1][j+1] == 'O':
                        if dp[i][j] > dp[i-1][j+1]:
                            dp[i-1][j+1] = dp[i][j]
                            result.append(dp[i][j])
                if i+1 < N:
                    if MAP[i+1][j+1] == '.':
                        if dp[i][j] > dp[i+1][j+1]:
                            dp[i+1][j+1] = dp[i][j]
                    elif MAP[i+1][j+1] == 'C':
                        if dp[i][j]+1 > dp[i+1][j+1]:
                            dp[i+1][j+1] = dp[i][j]+1
                    elif MAP[i+1][j+1] == 'O':
                        if dp[i][j] > dp[i+1][j+1]:
                            dp[i+1][j+1] = dp[i][j]
                            result.append(dp[i][j])
    if result:
        print(max(result))
    else:
        print(-1)
else:
    print(-1)