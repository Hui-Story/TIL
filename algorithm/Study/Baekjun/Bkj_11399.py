import sys

N = int(input())
P = map(int, sys.stdin.readline().split())

sort_P = sorted(P, reverse=True)

for i in range(1, len(sort_P)+1):
    sort_P[i-1] *= i

print(sum(sort_P))