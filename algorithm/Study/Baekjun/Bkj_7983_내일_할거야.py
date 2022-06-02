import sys
input = sys.stdin.readline

n = int(input())
homeworks = [tuple(map(int, input().split())) for _ in range(n)]
homeworks.sort(key=lambda x : x[1], reverse=True)

day = homeworks[0][1]
for d, t in homeworks:
    day = min(day, t) - d

print(day)