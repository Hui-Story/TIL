def search(now, cnt):
    global visited, result
    if cnt >= result:
        return
    if sum(visited) == N:
        result = min(result, cnt+battery[now][0])
        return
    for i in range(N):
        if i != now and not visited[i]:
            visited[i] = 1
            search(i, cnt+battery[now][i])
            visited[i] = 0


T = int(input())

for case in range(1, T+1):
    N = int(input())
    battery = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    visited[0] = 1
    result = 2e+10

    search(0, 0)

    print('#{} {}'.format(case, result))