import sys
from typing import List

input = sys.stdin.readline
graph = List[List[bool]]

def dragon_curve(x: int, y: int, d: int, g: int) -> None:
    global MAP

    MAP[x][y] = True
    curve: List[int] = [d]

    for _ in range(g):
        for i in range(len(curve) - 1, -1, -1):
            curve.append((curve[i] + 1) % 4)

    for i in range(len(curve)):
        x += dx[curve[i]]
        y += dy[curve[i]]
        if 0 <= x <= 100 and 0 <= y <= 100:
            MAP[x][y] = True

def solve(MAP: graph) -> int:
    answer: int = 0
    for x in range(100):
        for y in range(100):
            if MAP[x][y] and MAP[x + 1][y] and MAP[x][y + 1] and MAP[x + 1][y + 1]:
                answer += 1
    return answer

N: int = int(input())
MAP: graph = [[False] * 101 for _ in range(101)]
dx, dy = (1, 0, -1, 0), (0, -1, 0, 1)

for _ in range(N):
    x, y, d, g = map(int, input().split())
    dragon_curve(x, y, d, g)

print(solve(MAP))