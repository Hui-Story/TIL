import sys
from collections import deque

N = int(input())
numbers = sys.stdin.readline().split()

deq = deque(numbers)
deq_2 = deque(range(1, N+1))
result = []

while deq:
    number = int(deq.popleft())
    result.append(int(deq_2.popleft()))
    if number > 0: 
        deq.rotate(-number+1)
        deq_2.rotate(-number+1)
    else:
        deq.rotate(-number)
        deq_2.rotate(-number)

print(*result)