import sys
input = sys.stdin.readline

def fsum(i, j):
    pass

def fmodify(i, k):
    pass

N, M = map(int, input().split())

for _ in range(M):
    f, a, b = map(int, input().split())
    if f:
        fmodify(a, b)
    else:
        fsum(a, b)