import sys
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
    if parent[ch] != ch:
        parent[ch] = Find(parent[ch])
    return parent[ch]

N = int(input())
M = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
route = list(map(int, input().split()))
parent = [i for i in range(N)]

if M < 2:
    print('YES')
    exit()

for i in range(N):
    for j in range(i + 1, N):
        if table[i][j]:
            Union(i, j)

check = Find(route[0] - 1)
route = set(route)
for r in route:
    if Find(r - 1) != check:
        print('NO')
        break
else:
    print('YES')