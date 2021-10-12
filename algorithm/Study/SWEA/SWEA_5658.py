T = int(input())

for case in range(1, T+1):
    N, K = map(int, input().split())
    inp = str(input())
    result = set()

    for r in range(N//4):
        for i in range(r, N+r, N//4):
            num = ''
            for s in range(N//4):
                num += inp[(i+s) % N]
            result.add(int(num, 16))

    result = sorted(list(result))
    print('#{} {}'.format(case, result[-K]))