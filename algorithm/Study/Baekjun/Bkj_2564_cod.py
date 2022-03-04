import sys
input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

W, V = MIIS()
N = int(input())
shops = [tuple(MIIS()) for _ in range(N)]
sd, si = MIIS()

result = 0

for d, i in shops:
    pass

print(result)