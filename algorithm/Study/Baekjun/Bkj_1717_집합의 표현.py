import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def Union(a, b):
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
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


n, m = map(int, input().split())
parent = [0] * (n+1)

for ch in range(n+1):
    parent[ch] = ch

for _ in range(m):
    order, a, b = map(int, input().split())
    if order == 0:
        Union(a, b)
    elif order == 1:
        if Find(a) == Find(b):
            print('YES')
        else:
            print('NO')