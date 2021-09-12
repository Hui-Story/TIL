import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for case in range(t):
    n = int(input())
    start = list(map(int, input().split()))
    start.append(0)

    markets = []
    for _ in range(n):
        x, y = map(int, input().split())
        markets.append([x, y])
    visited = [0]*n

    festival = list(map(int, input().split()))

    deq = deque([start])
    result = 'sad'

    while deq:
        a = deq.popleft()
        a_i, a_j = a[0], a[1]
        if abs(festival[0]-a_i)+abs(festival[1]-a_j) <= 1000:
            result = 'happy'
            break
        for i in range(n):
            if visited[i] == 0 and abs(markets[i][0]-a_i)+abs(markets[i][1]-a_j) <= 1000:
                visited[i] = 1
                deq.append([markets[i][0], markets[i][1]])
    
    print(result)