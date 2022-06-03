import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [[0] * 600001 for _ in range(3)]
for i in range(3):
    dp[i][A[0] * (i + 1) + 300000] = 1
nums = [[A[0] * (i + 1)] for i in range(2)]
result = 0

for n in A[1:]:
    if dp[2][n + 300000]:
        result += 1
    if not dp[0][n + 300000]:
        dp[0][n + 300000] = 1
        nums[0].append(n)
    for i in range(1, 3):
        for num in nums[i - 1]:
            if not dp[i][num + n + 300000]:
                dp[i][num + n + 300000] = 1
                if i == 1:
                    nums[i].append(num + n)

print(result)