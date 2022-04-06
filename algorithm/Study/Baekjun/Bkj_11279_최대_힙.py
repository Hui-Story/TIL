import sys, heapq
input = sys.stdin.readline

maxheap = []

N = int(input())

for _ in range(N):
    x = int(input())
    if x:
        heapq.heappush(maxheap, -x)
    else:
        if maxheap:
            print(-heapq.heappop(maxheap))
        else:
            print(0)