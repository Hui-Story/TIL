import sys
from typing import List

input = sys.stdin.readline

N, M = map(int, input().split())
MAP: List[str] = [input().strip() for _ in range(N)]
answer: int = 1

for x in range(N):
    for y in range(M):
        for d in range(min(N - x, M - y)):
            if MAP[x][y] == MAP[x + d][y] == MAP[x][y + d] == MAP[x + d][y + d]:
                answer = max(answer, (d + 1) * (d + 1))

print(answer)