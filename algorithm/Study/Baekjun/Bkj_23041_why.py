N, M = map(int, input().split())

if N > M:
    N, M = M, N

b, a = N, M
while b != 0:
    r = a % b
    a = b
    b = r

if (N // a + M // a) % 2:
    print(a ** 2)
else:
    print((a ** 2) * 2)