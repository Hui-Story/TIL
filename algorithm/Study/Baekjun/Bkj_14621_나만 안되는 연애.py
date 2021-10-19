import sys, heapq
input = sys.stdin.readline

def Union(a, b, cost):
    global N, parent, result
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
        N -= 1
        result += cost
        if pa < pb:
            parent[pb] = pa
        else:
            parent[pa] = pb

def Find(ch):
    if parent[ch] == ch:
        return ch
    ret = Find(parent[ch])
    parent[ch] = ret
    return parent[ch]

def Kruskal():
    while N != 1 and minheap:
        cost, a, b = heapq.heappop(minheap)
        Union(a, b, cost)


N, M = map(int, input().split())
university = list(map(str, input().split()))
parent = [i for i in range(N+1)]
minheap = []
result = 0

for _ in range(M):
    u, v, d = map(int, input().split())
    if university[u-1] != university[v-1]:
        heapq.heappush(minheap, (d, u, v))

Kruskal()

if N == 1:
    print(result)
else:
    print(-1)