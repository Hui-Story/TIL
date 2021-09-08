import sys
input = sys.stdin.readline

# 계수 정렬 (counting sort)
count = {}

N = int(input())

for _ in range(N):
    count[int(input())] = 1

for num in sorted(count.keys()):
    print(num)