import sys
input = sys.stdin.readline

N, M = map(int, input().split())
for _ in range(N):
    input()
route = []
if N < M:
    for i in range(N):
        route.append([i, i])
    for i in range(N, M):
        route.append([N-1, i])
elif N > M:
    for i in range(M):
        route.append([i, i])
    for i in range(M, N):
        route.append([i, M-1])
else:
    route = [[i, i] for i in range(N)]

if len(route) % 2:
    print((len(route) + 1) * 2)
    for i in range(0, len(route)-1, 2):
        for _ in range(2):
            print(*route[i])
            print(*route[i+1])
    if N == M:
        for _ in range(2):
            print(N-1, M-2)
            print(*route[-1])
    else:
        for _ in range(2):
            print(N-2, M-2)
            print(*route[-1])
else:
    print(len(route) * 2)
    for i in range(0, len(route), 2):
        for _ in range(2):
            print(*route[i])
            print(*route[i+1])