import sys, math
input = sys.stdin.readline

def Union(a, b, d):
    global n, result
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
        result += d
        n -= 1
        if pa < pb:
            parent[pb] = pa
        else:
            parent[pa] = pb

def Find(ch):
    if parent[ch] != ch:
        parent[ch] = Find(parent[ch])
    return parent[ch]


n = int(input())
stars = []
parent = [i for i in range(n)]
dist = []
result = 0

for i in range(n):
    x, y = map(float, input().split())
    for j in range(len(stars)):
        x2, y2 = stars[j]
        dist.append((math.sqrt((x2 - x) * (x2 - x) + (y2 - y) * (y2 - y)), i, j))
    stars.append((x, y))

dist.sort(key=lambda x : x[0])

for d, a, b in dist:
    Union(a, b, d)
    if n <= 1:
        break

print(result)