import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def Union(a, b):
    pa = Find(a)
    pb = Find(b)
    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb

def Find(ch):
    if parent[ch] == ch:
        return ch
    parent[ch] = Find(parent[ch])
    return parent[ch]


N = int(input())

parent = dict()
for ch in range(1, N+1):
    parent[ch] = ch

result = []

for _ in range(N-2):
    a, b = map(int, input().split())
    Union(a, b)

for i in range(1, N+1):
    if i == Find(i):
        result.append(i)
    if len(result) == 2:
        break

print(*result)