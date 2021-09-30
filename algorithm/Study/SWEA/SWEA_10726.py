T = int(input())

for case in range(1, T+1):
    N, M = map(int, input().split())

    M_bin = bin(M)[2:].zfill(N)
    M_bin = M_bin[::-1]

    for i in range(N):
        if M_bin[i] != '1':
            print('#{} OFF'.format(case))
            break
    else:
        print('#{} ON'.format(case))