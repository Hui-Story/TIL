
def Union(a, b):
    global N, parent
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
        N -= 1
        parent[pb] = pa

def Find(ch):
    if parent[ch] == ch:
        return ch
    ret = Find(parent[ch])
    parent[ch] = ret
    return parent[ch]


T = int(input())

for case in range(1, T+1):
    N, M = map(int, input().split())

    parent = dict()
    for ch in range(1, N+1):
        parent[ch] = ch
    
    for _ in range(M):
        a, b = map(int, input().split())
        Union(a, b)

    print('#{} {}'.format(case, N))