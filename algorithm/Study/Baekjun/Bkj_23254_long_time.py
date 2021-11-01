import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
maxheap = []

for i in range(M):
    ar, bi = 100-a[i], -b[i]
    heapq.heappush(maxheap, [bi, ar, i])

N = 24*N
while N and maxheap:
    bi, ar, i = heapq.heappop(maxheap)
    bi = -bi
    rem = ar % bi
    quot = ar // bi
    if N >= quot:
        N -= quot
        a[i] += quot*bi
    else:
        a[i] += N*bi
        N = 0
    if rem:
        heapq.heappush(maxheap, [-rem, rem, i])

print(sum(a))