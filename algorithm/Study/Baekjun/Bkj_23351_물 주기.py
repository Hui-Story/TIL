import sys
input = sys.stdin.readline

N, K, A, B = map(int, input().split())
catnips = [K] * N
result = 1

idx = 0
while True:
    if idx + A < N:
        for i in range(idx, idx+A):
            catnips[i] += B
        idx += A
    else:
        for i in range(N-1, N-1-A, -1):
            catnips[i] += B
        idx = 0

    for i in range(N):
        if catnips[i] > 1:
            catnips[i] -= 1
        else:
            break
    else:
        result += 1
        continue
    break

print(result)