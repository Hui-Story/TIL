from collections import deque

N, K = map(int, input().split())

if N >= K:
    print(N - K)
    print(1)
    exit()

dist = [[-1, 0] for _ in range(100001)]

deq = deque()
deq.append(N)
dist[N][0] = 0
dist[N][1] = 1

min_time = 100001
cnt = 0

while deq:
    now = deq.popleft()
    now_dist, now_cnt = dist[now]
    if now == K:
        if now_dist > min_time:
            break
        min_time = now_dist
        cnt += now_cnt
    if (now * 2) <= 100000:
        next_dist = dist[now * 2][0]
        if next_dist == -1:
            dist[now * 2][0] = now_dist + 1
            dist[now * 2][1] += now_cnt
            deq.append(now * 2)
        elif next_dist == now_dist + 1:
            dist[now * 2][1] += now_cnt
    if now < 100000:
        next_dist = dist[now + 1][0]
        if next_dist == -1:
            dist[now + 1][0] = now_dist + 1
            dist[now + 1][1] = now_cnt
            deq.append(now + 1)
        elif next_dist == now_dist + 1:
            dist[now + 1][1] += now_cnt
    if now > 0:
        next_dist = dist[now - 1][0]
        if next_dist == -1:
            dist[now - 1][0] = now_dist + 1
            dist[now - 1][1] = now_cnt
            deq.append(now - 1)
        elif next_dist == now_dist + 1:
            dist[now - 1][1] += now_cnt

print(min_time)
print(cnt)