from math import factorial

N, K = map(int, input().split())

answer = factorial(N) // (factorial(K) * factorial(N - K))

print(answer % 10007)