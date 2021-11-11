import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
N = int(input())

result = 0

for _ in range(N):
    score = 0
    for _ in range(3):
        a, b, c = map(int, input().split())
        score += A * a + B * b + C * c
    result = max(result, score)

print(result)