import sys, heapq

input = sys.stdin.readline

N = int(input())
homeworks = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x : x[0])

max_heap = []
score = 0

day = homeworks[-1][0]

while day:
    while homeworks and (homeworks[-1][0] == day):
        d, w = homeworks.pop()
        heapq.heappush(max_heap, -w)
    if max_heap:
        score -= heapq.heappop(max_heap)
    day -= 1

print(score)