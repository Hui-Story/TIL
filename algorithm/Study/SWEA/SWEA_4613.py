T = int(input())

for case in range(1, T+1):
    N, M = map(int, input().split())
    flag = [str(input()) for _ in range(N)]

    min_result = 2e+10

    for W in range(N-2):
        for B in range(W+1, N-1):
            for R in range(B+1, N):
                total = 0
                for i in range(N):
                    if i <= W:
                        total += M - flag[i].count('W')
                    elif i <= B:
                        total += M - flag[i].count('B')
                    else:
                        total += M - flag[i].count('R')
                    if total >= min_result:
                        break
                if total < min_result:
                    min_result = total

    print('#{} {}'.format(case, min_result))