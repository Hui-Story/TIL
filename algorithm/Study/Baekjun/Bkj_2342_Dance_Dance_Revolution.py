steps = list(map(int, input().split()))[:-1]

if not steps:
    print(0)
    exit()

dp = [[[500000] * 5 for _ in range(5)] for _ in range(len(steps) + 1)]
dp[0][0][0] = 0

for i in range(1, len(steps) + 1):
    point = steps[i - 1]
    for r in range(4):
        for c in range(r, 5):
            pre = dp[i - 1][r][c]
            if pre < 500000:
                for left, right in ((r, c), (c, r)):
                    if left == 0:
                        temp = 2
                    elif point == left:
                        temp = 1
                    elif point % 2 == left % 2:
                        temp = 4
                    else:
                        temp = 3
                    if point > right:
                        dp[i][right][point] = min(dp[i][right][point], pre + temp)
                    elif point < right:
                        dp[i][point][right] = min(dp[i][point][right], pre + temp)

result = 500000
for r in range(4):
    for c in range(r, 5):
        if dp[-1][r][c] < 500000:
            result = min(result, dp[-1][r][c])
print(result)