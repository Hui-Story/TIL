import sys
input = sys.stdin.readline

def dfs(x, y, cnt):
    global alphabet_check, result
    result = max(result, cnt)
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < R and 0 <= ny < C:
            alphabet = ord(MAP[nx][ny]) - 65
            if not alphabet_check[alphabet]:
                alphabet_check[alphabet] = 1
                dfs(nx, ny, cnt + 1)
                alphabet_check[alphabet] = 0


R, C = map(int, input().split())
MAP = [input().strip() for _ in range(R)]
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
alphabet_check = [0] * 26
alphabet_check[ord(MAP[0][0]) - 65] = 1
result = 0

dfs(0, 0, 1)

print(result)