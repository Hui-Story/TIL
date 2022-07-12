import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    K, *foods = map(str, input().strip())