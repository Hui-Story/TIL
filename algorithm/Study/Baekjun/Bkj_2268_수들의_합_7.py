import sys, math
input = sys.stdin.readline

def find_index(node, start, end):
    global node_index
    if start == end:
        node_index[start] = node
    else:
        find_index(node * 2, start, (start + end) // 2)
        find_index(node * 2 + 1, (start + end) // 2 + 1, end)

def query(node, start, end, left, right):
    global tree
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    lsum = query(node * 2, start, (start + end) // 2, left, right)
    rsum = query(node * 2 + 1, (start + end) // 2 + 1, end, left, right)
    return lsum + rsum

def update(node):
    global tree
    while node:
        tree[node] = tree[node * 2] + tree[node * 2 + 1]
        node //= 2

N, M = map(int, input().split())
h = math.ceil(math.log2(N))
tree_size = 1 << (h + 1)
tree = [0] * tree_size
node_index = [0] * (N + 1)

find_index(1, 1, N)

for _ in range(M):
    f, a, b = map(int, input().split())
    if f == 0:
        if a > b:
            a, b = b, a
        print(query(1, 1, N, a, b))
    else:
        tree[node_index[a]] = b
        update(node_index[a] // 2)