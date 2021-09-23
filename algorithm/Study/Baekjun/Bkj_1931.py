import sys
input = sys.stdin.readline

N = int(input().strip())
meet = [list(map(int, input().strip().split())) for _ in range(N)]

meet = sorted(meet, key=lambda x : x[1])

print(meet)