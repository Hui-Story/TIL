import sys

input = sys.stdin.readline

N = int(input())
answer = 0

for _ in range(N):
    answer += int(input())

print(answer - (N - 1))