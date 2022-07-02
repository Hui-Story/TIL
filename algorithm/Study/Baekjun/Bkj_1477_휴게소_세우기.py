import sys

input = sys.stdin.readline
MIIS = lambda: map(int, input().split())

N, M, L = MIIS()
rest_areas = [0] + list(MIIS()) + [L]
rest_areas.sort()

start, end = 1, L - 1
result = 0
while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in range(1, N + 2):
        dist = rest_areas[i] - rest_areas[i - 1]
        if dist > mid:
            cnt += (dist - 1) // mid
    if cnt > M:
        start = mid + 1
    else:
        end = mid - 1
        result = mid
print(result)