import sys
input = sys.stdin.readline

def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    print(factorial(M) // (factorial(M - N) * factorial(N)))