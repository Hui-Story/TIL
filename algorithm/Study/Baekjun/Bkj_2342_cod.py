steps = list(map(int, input().split()))[:-1]

if not steps:
    print(0)
    exit()

dp = [[[500000] * 5 for _ in range(5)] for _ in range(len(steps))]
same_check = True

for i in range(1, len(steps)):
    if same_check and steps[i] != steps[i-1]:
        same_check = False
        dp[i][min(steps[i], steps[i-1])][max(steps[i], steps[i-1])] = 4 + (i - 1)
        continue
    point = steps[i]
    for r in range(1, 4):
        for c in range(r, 5):
            if dp[i-1][r][c] < 500000:
                pre = dp[i-1][r][c]
                for left, right in ((r, c), (c, r)):
                    if point == left:
                        temp = 1
                    elif point % 2 == left % 2:
                        temp = 4
                    else:
                        temp = 3
                    if point > right:
                        dp[i][right][point] = min(dp[i][right][point], pre + temp)
                    elif point < right:
                        dp[i][point][right] = min(dp[i][right][point], pre + temp)

if same_check:
    print(2 + len(steps) - 1)
else:
    for i in dp:
        for j in i:
            print(j)
        print()
    result = 500000
    for r in range(1, 4):
        for c in range(r, 5):
            if dp[-1][r][c] < 500000:
                result = min(result, dp[-1][r][c])
    print(result)