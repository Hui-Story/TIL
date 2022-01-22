from collections import deque

N, K = map(int, input().split())

if N >= K:
    print(N - K)
    route = list(range(N, K - 1, -1))
    print(*route)
    exit()

dist = [[-1, 0] for _ in range(100001)]

deq = deque()
deq.append(N)
dist[N][0] = 0

while deq:
    now = deq.popleft()
    if now == K:
        print(dist[now][0])
        cnt = dist[now][0]
        route = []
        while cnt >= 0:
            route.append(now)
            now = dist[now][1]
            cnt -= 1
        route.reverse()
        print(*route)
        break
    if (now * 2) <= 100000 and dist[now * 2][0] == -1:
        dist[now * 2] = [dist[now][0] + 1, now]
        deq.append(now * 2)
    if now < 100000 and dist[now + 1][0] == -1:
        dist[now + 1] = [dist[now][0] + 1, now]
        deq.append(now + 1)
    if now > 0 and dist[now - 1][0] == -1:
        dist[now - 1] = [dist[now][0] + 1, now]
        deq.append(now - 1)