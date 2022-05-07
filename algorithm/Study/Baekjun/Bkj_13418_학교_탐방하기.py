import sys
input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

def Union(a, b, c, i):
    global N
    pa = Find(a, i)
    pb = Find(b, i)
    if pa != pb:
        N -= 1
        cnt[i] += (c + 1) % 2
        if pa < pb:
            parent[pb][i] = pa
        else:
            parent[pa][i] = pb

def Find(ch, i):
    if parent[ch][i] != ch:
        parent[ch][i] = Find(parent[ch][i], i)
    return parent[ch][i]

N, M = MIIS()
parent = [[i, i] for i in range(N + 1)]
cnt = [0, 0]
roads = []
for _ in range(M + 1):
    a, b, c = MIIS()
    roads.append((a, b, c))
roads.sort(key=lambda x : x[2])

N *= 2
for i in range(M + 1):
    if not N:
        break
    Union(*roads[i], 0)
    Union(*roads[-(i + 1)], 1)

print(cnt[0] * cnt[0] - cnt[1] * cnt[1])