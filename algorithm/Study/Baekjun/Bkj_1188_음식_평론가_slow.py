N, M = map(int, input().split())
result = 0

while True:
    N = N % M
    if not N:
        break
    if M % N:
        result += N
        M = M - N
    else:
        result += (M - N)
        break

print(result)