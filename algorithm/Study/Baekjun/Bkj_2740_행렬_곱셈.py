import sys
input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

N, M = MIIS()
A = [list(MIIS()) for _ in range(N)]
M, K = MIIS()
B = [list(MIIS()) for _ in range(M)]

C = [[0] * K for _ in range(N)]

for n in range(N):
    for k in range(K):
        for m in range(M):
            C[n][k] += A[n][m] * B[m][k]

for c in C:
    print(*c)