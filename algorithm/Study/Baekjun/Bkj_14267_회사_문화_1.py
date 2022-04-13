import sys
input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

n, m = MIIS()
superior = list(MIIS())
compliments = [0] * n

for _ in range(m):
    i, w = MIIS()
    compliments[i - 1] += w

for i in range(1, n):
    compliments[i] += compliments[superior[i] - 1]

print(*compliments)