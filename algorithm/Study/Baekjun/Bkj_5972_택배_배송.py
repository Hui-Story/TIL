import sys, heapq
input = sys.stdin.readline


def dijkstra():
    global dist
    min_heap = []
    heapq.heappush(min_heap, (dist[1], 1))

    while min_heap:
        now_dist, now_barn = heapq.heappop(min_heap)
        if dist[now_barn] < now_dist:
            continue
        for next_barn, next_dist in road[now_barn]:
        # for next_barn, next_dist in road[now_barn].items():
            new_dist = now_dist + next_dist
            if new_dist < dist[next_barn]:
                dist[next_barn] = new_dist
                heapq.heappush(min_heap, (new_dist, next_barn))


N, M = map(int, input().split())

dist = [float('inf')] * (N+1)
dist[1] = 0
road = [[] for _ in range(N+1)]
# road = dict()
# for i in range(1, N+1):
#     road[i] = {}

for _ in range(M):
    A, B, C = map(int, input().split())
    road[A].append((B, C))
    road[B].append((A, C))
    # if road[A].get(B) and road[A][B] <= C:
    #     continue
    # else:
    #     road[A][B] = C
    #     road[B][A] = C

dijkstra()

print(dist[N])