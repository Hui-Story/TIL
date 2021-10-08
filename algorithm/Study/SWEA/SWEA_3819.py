T = int(input())

for case in range(1, T+1):
    N = int(input().rstrip())
    A = []
    cnt = 0
    result = -2e+10
    cnt_idx = -1

    for idx in range(N):
        i = int(input())
        A.append(i)
        cnt += i
        if cnt > result:
            result = cnt
            cnt_idx = idx
        if cnt < 0:
            cnt = 0
    
    cnt = 0
    for i in range(N-1, cnt_idx, -1):
        cnt += A[i]
        if cnt > result:
            result = cnt
        if cnt < 0:
            cnt = 0

    print('#{} {}'.format(case, result))