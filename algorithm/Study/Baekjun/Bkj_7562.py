import sys
from collections import deque
input = sys.stdin.readline

def bfs(knight):
    global visited
    visited[knight[0]][knight[1]] = 1
    deq = deque([knight])
    while deq:
        a = deq.popleft()
        i, j = a[0], a[1]
        for d in range(8):
            x = i + dx[d]
            y = j + dy[d]
            if 0 <= x < l and 0 <= y < l and visited[x][y] == 0:
                visited[x][y] = visited[i][j] + 1
                if [x, y] == target:
                    return visited[x][y]
                deq.append([x, y])
    return


T = int(input())

for case in range(T):
    l = int(input())
    knight = list(map(int, input().split()))
    target = list(map(int, input().split()))

    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]

    visited = [[0]*l for _ in range(l)]

    if knight == target:
        print(0)
    else:
        print(bfs(knight)-1)