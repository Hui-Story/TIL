import heapq, math

def Union(a, b, cost):
    global N, parent, result
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
        N -= 1
        result += cost
        parent[pb] = pa

def Find(ch):
    if parent[ch] == ch:
        return ch
    ret = Find(parent[ch])
    parent[ch] = ret
    return parent[ch]

def Kruskal():
    while N != 1:
        cost, a, b = heapq.heappop(heap)
        Union(a, b, cost)


T = int(input())

for case in range(1, T+1):
    N = int(input())
    parent = dict()
    for ch in range(N+1):
        parent[ch] = ch

    islands_x = list(map(int, input().split()))
    islands_y = list(map(int, input().split()))

    E = float(input())

    heap = []

    for a in range(N-1):
        for b in range(a+1, N):
            heapq.heappush(heap, ((islands_x[b]-islands_x[a])**2 + (islands_y[b]-islands_y[a])**2, a, b))

    result = 0

    Kruskal()

    print('#{} {}'.format(case, round(result * E)))