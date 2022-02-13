import sys
input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

def Union(a, b):
    global N, total_cost
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
        total_cost -= c
        N -= 1
        if pa < pb:
            parent[pb] = pa
        else:
            parent[pa] = pb

def Find(ch):
    if parent[ch] != ch:
        parent[ch] = Find(parent[ch])
    return parent[ch]


N, M = MIIS()
parent = [i for i in range(N + 1)]
total_cost = 0
roads = []
for _ in range(M):
    a, b, c = MIIS()
    total_cost += c
    roads.append((a, b, c))
roads.sort(key=lambda x : x[2])

for a, b, c in roads:
    Union(a, b)
    if N == 1:
        print(total_cost)
        break
else:
    print(-1)