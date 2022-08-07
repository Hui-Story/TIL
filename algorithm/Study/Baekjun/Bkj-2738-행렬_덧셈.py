import sys

input = sys.stdin.readline
MIIS = lambda: map(int, input().split())

N, M = MIIS()
A = [list(MIIS()) for _ in range(N)]
B = [list(MIIS()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        A[i][j] += B[i][j]

for Ai in A:
    print(*Ai)