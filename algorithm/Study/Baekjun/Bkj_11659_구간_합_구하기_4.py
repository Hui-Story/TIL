import sys
from itertools import accumulate
input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

N, M = MIIS()
a = list(MIIS())
prefix_sum = list(accumulate(a))

for _ in range(M):
    i, j = MIIS()
    if i > 1:
        print(prefix_sum[j-1] - prefix_sum[i-2])
    else:
        print(prefix_sum[j-1])