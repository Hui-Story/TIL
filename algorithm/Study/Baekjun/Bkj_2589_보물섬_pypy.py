from collections import deque

def bfs(start):
    global result, visited
    deq.append(start)
    while deq:
        x, y, cnt = deq.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and MAP[nx][ny] == 'L':
                visited[nx][ny] = 1
                result = max(result, cnt+1)
                deq.append([nx, ny, cnt+1])

N, M = map(int, input().split())
MAP = [list(str(input())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

result = 0

for i in range(N*M-2):
    s = [i // M, i % M, 0]
    if MAP[s[0]][s[1]] == 'L':
        visited = [[0]*M for _ in range(N)]
        visited[s[0]][s[1]] = 1
        deq = deque()
        bfs(s)

print(result)