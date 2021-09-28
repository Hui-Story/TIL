from collections import deque

T = int(input().strip())

for case in range(1, T+1):
    N, M = map(int, input().strip().split())
    Network = [list(map(int, input().strip().split())) for _ in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    visited = [[0]*M for _ in range(N)]
    virus = False
    result = 0
    deq = deque()

    for i in range(N):
        for j in range(M):
            if not Network[i][j] or visited[i][j]:
                continue
            deq.append([i, j])
            visited[i][j] = 1
            while deq:
                a = deq.popleft()
                a_i, a_j = a[0], a[1]
                if Network[a_i][a_j] == 2:
                    virus = True
                
                for d in range(4):
                    x = a_i + dx[d]
                    y = a_j + dy[d]
                    if 0 <= x < N and 0 <= y < M and Network[x][y] and not visited[x][y]:
                        deq.append([x, y])
                        visited[x][y] = 1
            if virus:
                result += 1
                virus = False

    print('#{} {}'.format(case, result))
