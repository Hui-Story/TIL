import sys, bisect

input = sys.stdin.readline

n = int(input())
array: list[int] = list(map(int, input().split()))

dp: list[int] = [array[0]]

for i in range(n):
    if array[i] > dp[-1]:
        dp.append(array[i])
    else:
        idx = bisect.bisect_left(dp, array[i])
        dp[idx] = array[i]

print(len(dp))