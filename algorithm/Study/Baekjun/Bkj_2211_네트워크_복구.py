import sys, math, heapq
input = sys.stdin.readline

def dijkstra(graph, start):
    global pre_nodes
    distance = [math.inf] * (N + 1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        now_dist, now_node = heapq.heappop(queue)

        if distance[now_node] < now_dist:
            continue

        for new_node, new_dist in graph[now_node]:
            dist = distance[now_node] + new_dist
            if dist < distance[new_node]:
                distance[new_node] = dist
                pre_nodes[new_node] = now_node
                heapq.heappush(queue, (dist, new_node))


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
pre_nodes = [0] * (N + 1)
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

dijkstra(graph, 1)

print(N - 1)
for i in range(2, N + 1):
    print(i, pre_nodes[i])