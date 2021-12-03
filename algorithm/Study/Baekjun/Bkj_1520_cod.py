import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(M)]

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

deq = deque()
deq.append([0, 0])

while deq:
    x, y = deq.popleft()
    