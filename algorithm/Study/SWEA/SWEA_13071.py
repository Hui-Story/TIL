T = int(input())

for case in range(1, T+1):
    N = int(input())
    work = [list(map(int, input().split())) for _ in range(N)]
    work = sorted(work, key=lambda x : (x[1], x[0]))

    cnt = 0
    idx = 0
    time = 0

    while idx < N:
        if work[idx][0] >= time:
            cnt += 1
            time = work[idx][1]
        idx += 1
    
    print('#{} {}'.format(case, cnt))