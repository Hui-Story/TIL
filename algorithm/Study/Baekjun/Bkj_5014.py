import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())
floor_lst = [0] * F
floor_lst[S-1] = 1
D = -D

def link(F, S, G, U, D):
    if G == S:
        print(0)
        return
    else:
        q = deque([[U, S, 1]])
        q.append([D, S, 1])

    while q:
        search_lst = q.popleft()
        order = search_lst[0]
        floor = search_lst[1]
        count = search_lst[2]
        if floor + order == G:
            print(count)
            return
        elif 0 < floor+order <= F and floor_lst[floor+order-1] == 0:
            floor_lst[floor+order-1] = 1
            q.append([U, floor+order, count+1])
            q.append([D, floor+order, count+1])

    print('use the stairs')
    return


link(F, S, G, U, D)