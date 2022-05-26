import sys
input = sys.stdin.readline

N = int(input())
x, y = map(int, input().split())
result = 0

for i in range(N - 1):
    nx, ny = map(int, input().split())
    if x <= ny <= y:
        continue
    elif nx <= y:
        y = ny
    else:
        result += y - x
        x, y = nx, ny

print(result + (y - x))