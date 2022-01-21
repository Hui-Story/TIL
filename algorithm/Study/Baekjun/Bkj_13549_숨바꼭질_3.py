from collections import deque

N, K = map(int, input().split())

if N >= K:
    print(N - K)
    exit()

dist = [-1] * 100001

deq = deque()
deq.append(N)
dist[N] = 0

while deq:
    now = deq.popleft()
    if now == K:
        print(dist[now])
        break
    if (now * 2) <= 100000 and dist[now * 2] == -1:
        dist[now * 2] = dist[now]
        deq.appendleft(now * 2)
    if now < 100000 and dist[now + 1] == -1:
        dist[now + 1] = dist[now] + 1
        deq.append(now + 1)
    if now > 0 and dist[now - 1] == -1:
        dist[now - 1] = dist[now] + 1
        deq.append(now - 1)