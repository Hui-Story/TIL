N, K = map(int, input().split())

A, B = N // 2, N - (N // 2)
if A * B < K:
    print(-1)
else:
    result = ''
    for num in range(A, 0, -1):
        while K >= num:
            K -= num
            B -= 1
            result = 'B' + result
        result = 'A' + result
    print('B' * B + result)