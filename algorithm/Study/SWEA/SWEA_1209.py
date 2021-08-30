for case in range(1, 11):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]
    sum_lst = []
    for j in range(100):
        total = 0
        for i in range(100):
            total += lst[j][i]
        sum_lst.append(total)
    for i in range(100):
        total = 0
        for j in range(100):
            total += lst[j][i]
        sum_lst.append(total)
    total = 0
    for i in range(100):
        total += lst[i][i]
    sum_lst.append(total)
    total = 0
    for i in range(100):
        total += lst[i][100-i-1]
    sum_lst.append(total)
    print('#{} {}'.format(case, max(sum_lst)))
