import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def leaf_node(node):
    global N, result
    if len(dic[node]) == 0:
        result += 1
        return
    for i in dic[node]:
        leaf_node(i)
    return

N = int(input())
nodes = list(map(int, input().split()))
num = int(input())

dic = {}
result = 0

for i in range(N):
    dic[i] = []

for i in range(len(nodes)):
    if nodes[i] != -1 and i != num:
        dic[nodes[i]].append(i)

for i in range(N):
    if nodes[i] == -1 and i != num:
        leaf_node(i)

print(result)