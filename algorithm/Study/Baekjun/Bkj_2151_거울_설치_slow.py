import sys, heapq
input = sys.stdin.readline

N = int(input())
house = [str(input().strip()) for _ in range(N)]
visited = [[[10000, 10000, 10000, 10000] for _ in range(N)] for _ in range(N)]

dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
result = 10000

min_heap = []
for x in range(N):
    for y in range(N):
        if house[x][y] == '#':
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < N and 0 <= ny < N:
                    if house[nx][ny] != '*':
                        heapq.heappush(min_heap, (0, nx, ny, d))
            visited[x][y] = [0, 0, 0, 0]
            break
    else:
        continue
    break

while min_heap:
    cnt, x, y, dir = heapq.heappop(min_heap)
    if cnt > result:
        continue
    if cnt <= visited[x][y][dir]:
        visited[x][y][dir] = cnt
    else:
        continue
    if house[x][y] == '#':
        result = cnt
        break
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 <= nx < N and 0 <= ny < N:
        if house[nx][ny] != '*':
            heapq.heappush(min_heap, (cnt, nx, ny, dir))
    if house[x][y] == '!':
        for d in [(dir + 1) % 4, (dir + 3) % 4]:
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if house[nx][ny] != '*':
                    heapq.heappush(min_heap, (cnt + 1, nx, ny, d))

print(result)