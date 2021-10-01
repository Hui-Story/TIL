def N_M(cnt, max_num):
    if cnt == M:
        print(*result)
        return
    for i in range(1, N+1):
        if i >= max_num:
            result.append(i)
            N_M(cnt+1, i)
            result.pop()

N, M = map(int, input().split())

result = []

N_M(0, 1)