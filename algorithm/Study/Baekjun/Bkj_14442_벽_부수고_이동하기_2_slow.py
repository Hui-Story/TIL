import sys, collections
input = sys.stdin.readline

N, M, K = map(int, input().split())
MAP = [input().strip() for _ in range(N)]
visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)

deq = collections.deque()
deq.append((0, 0, 0))

while deq:
    x, y, cnt = deq.popleft()
    if x == N - 1 and y == M - 1:
        print(visited[x][y][cnt])
        exit()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < M:
            if MAP[nx][ny] == '1':
                if cnt == K or visited[nx][ny][cnt + 1]:
                    continue
                visited[nx][ny][cnt + 1] = visited[x][y][cnt] + 1
                deq.append((nx, ny, cnt + 1))
            else:
                if visited[nx][ny][cnt]:
                    continue
                visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                deq.append((nx, ny, cnt))

print(-1)