import sys
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[10000000] * V for _ in range(V)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c

for k in range(V):
    for i in range(V):
        for j in range(V):
            dist = graph[i][k] + graph[k][j]
            if dist < graph[i][j]:
                graph[i][j] = dist

result = 20000000
for i in range(V):
    for j in range(i+1, V):
        cycle_dist = graph[i][j] + graph[j][i]
        if cycle_dist < 10000000:
            result = min(result, cycle_dist)

if result != 20000000:
    print(result)
else:
    print(-1)