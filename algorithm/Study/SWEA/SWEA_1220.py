for case in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0

    for j in range(N):
        now = 2
        for i in range(N):
            if arr[i][j] == 1:
                now = 1
            elif arr[i][j] == 2 and now == 1:
                now = 2
                cnt += 1
    
    print('#{} {}'.format(case, cnt))