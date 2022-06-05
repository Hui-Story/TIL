import sys, heapq
input = sys.stdin.readline

N = int(input())
problems = sorted([tuple(map(int, input().split())) for _ in range(N)])
min_heap = []

for d, c in problems:
    heapq.heappush(min_heap, c)
    if d < len(min_heap):
        heapq.heappop(min_heap)

print(sum(min_heap))