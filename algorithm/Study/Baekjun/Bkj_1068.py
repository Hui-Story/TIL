import sys
input = sys.stdin.readline

def leaf_node(node):
    global N, result
    if sum(arr[node]) == 0:
        result += 1
        return
    for i in range(N):
        if arr[node][i] == 1:
            leaf_node(i)
    return

N = int(input())
nodes = list(map(int, input().split()))
num = int(input())

arr = [[0] * N for _ in range(N)]
result = 0

for i in range(1, N):
    if i != num:
        arr[nodes[i]][i] = 1
if num != 0:
    leaf_node(0)
print(result)