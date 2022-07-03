import sys, heapq
from typing import List

input = sys.stdin.readline

def dijkstra(MAP: List[str]) -> int:
    distance = [[float('inf')] * n for _ in range(n)]
    distance[0][0] = 0
    min_heap = []
    heapq.heappush(min_heap, (0, 0, 0))

    while min_heap:
        now_dist, x, y = heapq.heappop(min_heap)

        if distance[x][y] < now_dist:
            continue

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                dist = distance[x][y] + (int(MAP[nx][ny]) + 1) % 2
                if dist < distance[nx][ny]:
                    distance[nx][ny] = dist
                    heapq.heappush(min_heap, (dist, nx, ny))

    return distance[n - 1][n - 1]

n: int = int(input())
MAP: List[str] = [list(input().strip()) for _ in range(n)]
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)

answer = dijkstra(MAP)

print(answer)