import sys, heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    slimes = list(map(int, input().split()))
    heapq.heapify(slimes)
    energy = 1
    while len(slimes) >= 2:
        a = heapq.heappop(slimes)
        b = heapq.heappop(slimes)
        energy *= (a * b)
        heapq.heappush(slimes, a * b)
    print(energy % 1000000007)