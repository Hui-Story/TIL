from collections import deque

N, M = map(int, input().split())

dx = [-2, -1, 1, 2]
dy = [1, 2, 2, 1]

deq = deque()
result = 0
check = False

deq.append([N-1, 0, 1])

while deq:
    a = deq.popleft()
    i, j, cnt = a[0], a[1], a[2]

    if cnt >= 5:
        if i == N-1 and j == 6:
            check = True
        continue

    result = max(result, cnt)

    for d in range(4):
        x = i + dx[d]
        y = j + dy[d]
        if 0 <= x < N and 0 <= y < M:
            deq.append([x, y, cnt+1])

if check:
    result = max(result, M-7+5)

print(result)