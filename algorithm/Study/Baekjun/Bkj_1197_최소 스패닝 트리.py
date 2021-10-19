import sys, heapq
input = sys.stdin.readline

def Union(a, b, cost):
    global V, parent, result
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
        V -= 1
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
    while V != 1:
        cost, a, b = heapq.heappop(minheap)
        Union(a, b, cost)


V, E = map(int, input().split())
parent = [i for i in range(V+1)]
minheap = []
result = 0

for _ in range(E):
    A, B, C = map(int, input().split())
    heapq.heappush(minheap, (C, A, B))

Kruskal()

print(result)