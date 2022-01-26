import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def input_to_edge():
    global edge_lst
    while True:
        inp = list(map(int, input().split()))
        for i in range(0, len(inp), 2):
            if not inp[i] and not inp[i + 1]:
                return True
            edge_lst.append((inp[i], inp[i + 1]))
        if edge_lst and edge_lst[0][0] < 0:
            return False


k = 1
while True:
    parents = defaultdict(int)
    childs = defaultdict(list)
    edge_lst = []
    node_lst = []
    if not input_to_edge():
        break
    if not edge_lst:
        print(f'Case {k} is a tree.')
        continue
    for u, v in edge_lst:
        if parents[v]:
            print(f'Case {k} is not a tree.')
            break
        parents[v] = u
        node_lst.append(u)
        node_lst.append(v)
        childs[u].append(v)
    else:
        root_check = 0
        node_lst = set(node_lst)
        deq = deque()
        for node in node_lst:
            if not parents[node]:
                root_check += 1
                deq.append(node)
        else:
            if root_check:
                while deq:
                    node = deq.popleft()
                    for child_node in childs[node]:
                        deq.append(child_node)
                        root_check += 1
                if root_check == len(node_lst):
                    print(f'Case {k} is a tree.')
                else:
                    print(f'Case {k} is not a tree.')
            else:
                print(f'Case {k} is not a tree.')
    k += 1