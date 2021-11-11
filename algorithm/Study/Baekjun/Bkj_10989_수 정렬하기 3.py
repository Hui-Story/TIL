import sys, collections
input = sys.stdin.readline

# 계수 정렬 (counting sort)
count = collections.defaultdict(int)

N = int(input())

for _ in range(N):
    count[int(input())] += 1

for num in sorted(count.keys()):
    for _ in range(count[num]):
        print(num)