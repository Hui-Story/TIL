for case in range(10):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    for j in range(100):
        if ladder[0][j] == 1:
            j_idx = j
            for i in range(100):
                if j_idx-1 >= 0 and ladder[i][j_idx-1] == 1:
                    while j_idx-1 >= 0 and ladder[i][j_idx-1] == 1:
                        j_idx -= 1
                elif j_idx+1 < 100 and ladder[i][j_idx+1] == 1:
                    while j_idx+1 < 100 and ladder[i][j_idx+1] == 1:
                        j_idx += 1
            if ladder[99][j_idx] == 2:
                print('#{} {}'.format(T, j))
                break