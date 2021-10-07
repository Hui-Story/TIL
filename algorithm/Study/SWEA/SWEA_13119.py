def produce(now, cnt):
    global result
    if cnt >= result:
        return
    if now == N:
        result = min(result, cnt)
        return
    for i in range(N):
        if not factory[i]:
            factory[i] = 1
            produce(now+1, cnt+arr[now][i])
            factory[i] = 0


T = int(input())

for case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    factory = [0] * N
    result = 2e+10

    produce(0, 0)

    print('#{} {}'.format(case, result))