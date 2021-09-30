T = int(input())

for case in range(1, T+1):
    N, S = map(str, input().split())

    print('#{} '.format(case), end='')

    for i in S:
        print(bin(int(i, 16))[2:].zfill(4), end='')
    print()