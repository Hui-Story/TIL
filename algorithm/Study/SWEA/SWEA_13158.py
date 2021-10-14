from collections import deque

T = int(input())

for case in range(1, T+1):
    N, M = map(int, input().split())
    used = [0] * 1000001
    deq = deque()
    deq.append([N, 0])
    while deq:
        n, cnt = deq.popleft()
        if n == M:
            print('#{} {}'.format(case, cnt))
            break
        if n > 1000000 or used[n]:
            continue
        used[n] += 1
        deq.append([n+1, cnt+1])
        deq.append([n-1, cnt+1])
        deq.append([n*2, cnt+1])
        deq.append([n-10, cnt+1])