
def Union(a, b):
    global parent
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
        parent[pb] = pa

def Find(ch):
    if parent[ch] == ch:
        return ch
    ret = Find(parent[ch])
    parent[ch] = ret
    return parent[ch]


T = int(input())

for case in range(1, T+1):
    V, E = map(int, input().split())
    edge_lst = [list(map(int, input().split())) for _ in range(E)]
    edge_lst.sort(key = lambda x : x[2])

    parent = dict()
    for ch in range(V+1):
        parent[ch] = ch

    result = 0
    
    for edge in edge_lst:
        if Find(edge[0]) != Find(edge[1]):
            result += edge[2]
            Union(edge[0], edge[1])

    print('#{} {}'.format(case, result))