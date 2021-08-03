import sys
from collections import deque

N = int(input())

deq = deque()

for i in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        deq.append(int(order[1]))
    elif order[0] == 'pop':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif order[0] == 'size':
        print(len(deq))
    elif order[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif order[0] == 'back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])