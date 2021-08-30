def sudoku(lst):
 
    for i in range(9):
        check = [0] * 10
        for j in range(9):
            if check[lst[i][j]] == 0:
                check[lst[i][j]] += 1
            else:
                return 0
 
    for j in range(9):
        check = [0] * 10
        for i in range(9):
            if check[lst[i][j]] == 0:
                check[lst[i][j]] += 1
            else:
                return 0
 
    for i_s in range(0, 9, 3):
        for j_s in range(0, 9, 3):
            check = [0] * 10
            for i in range(i_s, i_s+3):
                for j in range(j_s, j_s+3):
                    if check[lst[i][j]] == 0:
                        check[lst[i][j]] += 1
                    else:
                        return 0
 
    return 1
 
T = int(input())
 
for case in range(1, T+1):
    lst = [list(map(int, input().split())) for _ in range(9)]
 
    print('#{} {}'.format(case, sudoku(lst)))