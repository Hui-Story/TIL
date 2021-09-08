import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    global MAP
    deq.append([i, j])
    while deq:
        a = deq.popleft()
        a_i, a_j = a[0], a[1]
        for d in range(4):
            x = a_i + dx[d]
            y = a_j + dy[d]
            if 0 <= x < H and 0 <= y < W and MAP[x][y] == '#':
                deq.append([x, y])
                MAP[x][y] = '.'


T = int(input())

for _ in range(T):
    H, W = map(int, input().split())
    MAP = [list(input())[:W] for _ in range(H)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    deq = deque()
    result = 0

    for i in range(H):
        for j in range(W):
            if MAP[i][j] == '#':
                bfs(i, j)
                result += 1
    
    print(result)