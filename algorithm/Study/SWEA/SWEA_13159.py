
def Union(a, b):
    global N
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
    inp = list(map(int, input().split()))
    parent = dict()
    for ch in range(1, N+1):
        parent[ch] = ch

    for i in range(M):
        Union(inp[i*2], inp[i*2+1])
    
    print('#{} {}'.format(case, N))