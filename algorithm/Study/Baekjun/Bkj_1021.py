import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
num_lst = list(map(int, input().split()))

deq = deque()
for i in range(1, N+1):
    deq.append(i)

result = 0

for num in num_lst:
    idx = deq.index(num)
    if idx <= len(deq)-idx:
        deq.rotate(-idx)
        result += idx
        deq.popleft()
    else:
        deq.rotate(len(deq)-idx)
        result += (len(deq)-idx)
        deq.popleft()

print(result)