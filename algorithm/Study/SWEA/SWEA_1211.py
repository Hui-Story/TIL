for case in range(10):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    min_cnt = 2e+10

    for j in range(100):
        if ladder[0][j] == 1:
            j_idx = j
            cnt = 0
            for i in range(100):
                cnt += 1
                if j_idx-1 >= 0 and ladder[i][j_idx-1] == 1:
                    while j_idx-1 >= 0 and ladder[i][j_idx-1] == 1:
                        j_idx -= 1
                        cnt += 1
                elif j_idx+1 < 100 and ladder[i][j_idx+1] == 1:
                    while j_idx+1 < 100 and ladder[i][j_idx+1] == 1:
                        j_idx += 1
                        cnt += 1
            if cnt < min_cnt:
                min_cnt = cnt
                min_idx = j
    print('#{} {}'.format(T, min_idx))