import sys
from collections import defaultdict
input = sys.stdin.readline

def dfs(x, y, cnt):
    global alphabet_check, result
    result = max(result, cnt)
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < R and 0 <= ny < C:
            alphabet = MAP[nx][ny]
            if not alphabet_check[alphabet]:
                alphabet_check[alphabet] = 1
                dfs(nx, ny, cnt + 1)
                alphabet_check[alphabet] = 0


R, C = map(int, input().split())
MAP = [input().strip() for _ in range(R)]
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
alphabet_check = defaultdict(int)
alphabet_check[MAP[0][0]] = 1
result = 0

dfs(0, 0, 1)

print(result)