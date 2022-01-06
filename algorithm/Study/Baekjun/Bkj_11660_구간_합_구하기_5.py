import sys
from itertools import accumulate
input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

N, M = MIIS()
table = [list(MIIS()) for _ in range(N)]
prefix_sum = [list(accumulate(table[i])) for i in range(N)]

for i in range(1, N):
    for j in range(N):
        prefix_sum[i][j] += prefix_sum[i-1][j]

for _ in range(M):
    x1, y1, x2, y2 = MIIS()
    result = prefix_sum[x2-1][y2-1]
    if x1 >= 2:
        result -= prefix_sum[x1-2][y2-1]
    if y1 >= 2:
        result -= prefix_sum[x2-1][y1-2]
    if x1 >= 2 and y1 >= 2:
        result += prefix_sum[x1-2][y1-2]
    print(result)