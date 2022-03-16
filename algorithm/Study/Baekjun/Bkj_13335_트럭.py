import sys
from collections import deque
input = sys.stdin.readline

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))
deq = deque([0] * w)
time = 0
load = 0

idx = 0
while idx < n:
    load -= deq.popleft()
    if load + trucks[idx] <= L:
        deq.append(trucks[idx])
        load += trucks[idx]
        idx += 1
    else:
        deq.append(0)
    time += 1

print(time + w)