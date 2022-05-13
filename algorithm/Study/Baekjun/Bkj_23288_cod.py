import sys, collections
input = sys.stdin.readline

N, M, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
SMAP = [[0] * M for _ in range(N)]
dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)

deq = collections.deque()

for i in range(N):
    for j in range(M):
        if not SMAP[i][j]:
            num = MAP[i][j]
            fill_lst = []
            deq.append((i, j))
            SMAP[i][j] = 1
            while deq:
                x, y = deq.popleft()
                fill_lst.append((x, y))
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < N and 0 <= ny < M and not SMAP[nx][ny] and MAP[nx][ny] == num:
                        SMAP[nx][ny] = 1
                        deq.append((nx, ny))
            cnt = len(fill_lst)
            for x, y in fill_lst:
                SMAP[x][y] = num * cnt