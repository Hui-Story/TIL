import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def binary(start):
    global tree, parents
    for i in dic[start]:
        if i:
          binary(i)
    print(start)
    return

tree = []
parents = [0] * (1000001)
dic = {}

while True:
    try:
        tree.append(int(input()))
    except:
        break

parents[tree[0]] += 1000001

for i in tree:
    dic[i] = []

max_node = 0

for i in range(len(tree)-1):
    if tree[i] > max_node:
        max_node = tree[i]
    if tree[i] > tree[i+1]:
        dic[tree[i]].append(tree[i+1])
        parents[tree[i+1]] = tree[i]
    else:
        node = tree[i]
        parent = parents[node]
        while True:
            if parent > tree[i+1]:
                if dic[node]:
                    dic[node].append(tree[i+1])
                else:
                    dic[node].append(0)
                    dic[node].append(tree[i+1])
                parents[tree[i+1]] = node
                break
            elif parent < node < tree[i+1]:
                if tree[i+1] > max_node:
                    if dic[max_node]:
                        dic[max_node].append(tree[i+1])
                    else:
                        dic[max_node].append(0)
                        dic[max_node].append(tree[i+1])
                    parents[tree[i+1]] = node
                    break
                else:
                    node = parents[node]
                    parent = parents[node]
            else:
                node = parents[node]
                parent = parents[node]

binary(tree[0])