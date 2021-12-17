import sys
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
            child_cnt[pa] += 1
            used_roads.append((pa, cost))
        else:
            parent[pa] = pb
            child_cnt[pb] += 1
            used_roads.append((pb, cost))

def Find(ch):
    if parent[ch] != ch:
        parent[ch] = Find(parent[ch])
    return parent[ch]

def Kruskal():
    i = 0
    while N != 1 and i < len(roads):
        cost, a, b = roads[i]
        Union(a, b, cost)
        i += 1


N, M = map(int, input().split())
parent = [i for i in range(N+1)]
child_cnt = [0] * (N+1)
roads = []
used_roads = []
result = 0

for _ in range(M):
    A, B, C = map(int, input().split())
    roads.append((C, A, B))

roads.sort(key=lambda x : x[0])

Kruskal()
used_roads.sort(key=lambda x : x[1], reverse=True)
for house, cost in used_roads:
    if child_cnt[house] == 1 or parent[house] == house:
        result -= cost
        break
    continue

print(result)