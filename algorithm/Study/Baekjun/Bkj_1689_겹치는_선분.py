import sys, heapq
input = sys.stdin.readline

N = int(input())
lines = sorted([tuple(map(int, input().split())) for _ in range(N)])

line_cnt = 0
max_line = 0
min_heap = []

for s, e in lines:
    while min_heap and s >= min_heap[0]:
        heapq.heappop(min_heap)
        line_cnt -= 1
    line_cnt += 1
    heapq.heappush(min_heap, e)
    max_line = max(max_line, line_cnt)

print(max_line)