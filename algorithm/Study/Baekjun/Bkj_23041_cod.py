N, M = map(int, input().split())

if N > M:
    N, M = M, N

if N == M:
    print((M**2)*2)
elif N == 0:
    print(M**2)
else:
    b, a = N, M
    while b != 0:
        r = a % b
        a = b
        b = r
    
    # if (N + M) % 2:
    #     print(N ** 2)
    # else:
    #     print((N ** 2) * a)