n = int(input())
ranking = list(map(int, input().split()))

result = 0

for _ in range(n-1):
    now = len(ranking)
    idx = ranking.index(now)
    l = r = 256
    if idx < (now - 1):
        r = now - ranking[idx + 1]
    if idx > 0:
        l = now - ranking[idx - 1]
    result += min(l, r)
    del ranking[idx]

print(result)