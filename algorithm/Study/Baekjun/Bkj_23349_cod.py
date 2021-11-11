import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    name, place, *time = map(str, input().strip().split())