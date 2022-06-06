import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    result = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        d1 = (((x1 - cx) ** 2) + ((y1 - cy) ** 2)) ** 0.5
        d2 = (((x2 - cx) ** 2) + ((y2 - cy) ** 2)) ** 0.5
        if (r < d1) != (r < d2):
            result += 1
    print(result)