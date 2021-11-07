import sys
input = sys.stdin.readline

def Union(a, b):
    global parent, red_group_size
    pa = Find(a)
    pb = Find(b)
    if pa < pb:
        red_group_size[pa] += red_group_size[pb]
        red_group_size[pb] = 0
        parent[pb] = pa
    else:
        red_group_size[pb] += red_group_size[pa]
        red_group_size[pa] = 0
        parent[pa] = pb

def Find(ch):
    if parent[ch] != ch:
        parent[ch] = Find(parent[ch])
    return parent[ch]


N = int(input())
edge_lst = []
for _ in range(N-1):
    a, b = map(int, input().split())
    edge_lst.append([a, b])
color = 'N' + str(input())

parent = [i for i in range(N+1)]
red_group_size = [1]*(N+1)
black_nodes = []

for i in range(N-1):
    a, b = edge_lst[i]
    if color[a] == 'R' and color[b] == 'R':
        Union(a, b)
    elif color[a] == 'B' and color[b] == 'R':
        black_nodes.append([a, b])
    elif color[a] == 'R' and color[b] == 'B':
        black_nodes.append([b, a])

result = 0

for a, b in black_nodes:
    result += red_group_size[Find(b)]

print(result)