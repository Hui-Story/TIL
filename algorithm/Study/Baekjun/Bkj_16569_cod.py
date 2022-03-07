import sys
input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

M, N, V = MIIS()
X, Y = MIIS()
MAP = [list(MIIS()) for _ in range(N)]
