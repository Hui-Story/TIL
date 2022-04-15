import sys, heapq
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if heap:
            a, b = heapq.heappop(heap)
            print(a * b)
        else:
            print(0)
    else:
        if x > 0:
            heapq.heappush(heap, (x, 1))
        else:
            heapq.heappush(heap, (-x, -1))