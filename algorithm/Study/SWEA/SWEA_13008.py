from collections import deque

T = int(input())

def bfs(locate):
    global result, now, now_locate
    visited[locate[0]][locate[1]] = 1
    deq.append(locate)
    while deq:
        i, j, cnt = deq.popleft()
        if MAP[i][j] == str(now):
            now += 1
            now_locate = [i, j, 0]
            result += cnt
            return
        for d in range(4):
            x = i + dx[d]
            y = j + dy[d]
            if 0 <= x < H and 0 <= y < W and MAP[x][y] != '#' and not visited[x][y]:
                visited[x][y] = 1
                deq.append([x, y, cnt+1])


for case in range(1, T+1):
    H, W, N = map(int, input().split())
    MAP = [list(str(input())) for _ in range(H)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    deq = deque()
    result = 0
    now = 1
    now_locate = [0, 0, 0]

    while now <= N:
        visited = [[0]*W for _ in range(H)]
        bfs(now_locate)
        deq.clear()

    print(f'#{case} {result}')