from collections import deque

N, K = map(int, input().split())
deq = deque(range(1, N + 1))
result = []

while deq:
    deq.rotate(-(K - 1))
    result.append(str(deq.popleft()))

print('<' + ', '.join(result) + '>')