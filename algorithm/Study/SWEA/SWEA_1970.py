T = int(input())

for case in range(1, T+1):
    N = int(input())
    cash = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = [0] * 8

    for i in range(8):
        if N >= cash[i]:
            cnt = N // cash[i]
            result[i] += cnt
            N -= cash[i] * cnt
    
    print('#{}'.format(case))
    print(*result)