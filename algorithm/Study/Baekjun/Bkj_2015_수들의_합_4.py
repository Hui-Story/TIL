from itertools import accumulate
from collections import defaultdict

N, K = map(int, input().split())
A = list(accumulate(map(int, input().split())))
prefix_sum = defaultdict(int)

result = 0

for i in range(N):
    if A[i] == K:
        result += 1
    result += prefix_sum[A[i] - K]
    prefix_sum[A[i]] += 1

print(result)