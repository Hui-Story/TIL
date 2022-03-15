import sys
input = sys.stdin.readline

N, K = map(int, input().split())
scores = list(map(int, input().split()))
result = 0

start, end = 0, 20 * N

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    total_score = 0
    for score in scores:
        total_score += score
        if total_score >= mid:
            total_score = 0
            cnt += 1
    if cnt >= K:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)