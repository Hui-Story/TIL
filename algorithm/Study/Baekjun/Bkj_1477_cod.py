from heapq import *

N, M, L = map(int, input().split())
rest_areas = [0] + list(map(int, input().split())) + [L]
rest_areas.sort()
max_heap = []
for i in range(1, N+2):
    heappush(max_heap, -(rest_areas[i] - rest_areas[i-1] - 1))

for _ in range(M):
    temp = -heappop(max_heap)
    if temp % 2:
        a = b = temp // 2
    else:
        a, b = temp // 2, (temp // 2) - 1
    if a:
        heappush(max_heap, -a)
    if b:
        heappush(max_heap, -b)
    print(max_heap)

print(-max_heap[0] + 1)