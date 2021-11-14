import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
priority_lst = [0] * (M + 1)
now_priority = M
load_space = []
result = 0

deq = deque()

for _ in range(N):
    P, W = map(int, input().split())
    priority_lst[P] += 1
    deq.append([P, W])

while deq and M:
    if not priority_lst[now_priority]:
        now_priority -= 1
        load_space = []
        continue
    P, W = deq.popleft()
    result += W
    if P == now_priority:
        for container in load_space:
            if container < W:
                result += container * 2
        load_space.append(W)
        priority_lst[P] -= 1
    else:
        deq.append([P, W])
    
print(result)