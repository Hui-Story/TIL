import sys, collections
input = sys.stdin.readline

N, M, R = map(int, input().split())
deq = collections.deque()
deq.append(R)
edges = collections.defaultdict(list)
result = [0] * (N + 1)
result[R] = 1
for _ in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

step = 2
while deq:
    now = deq.popleft()
    now_edges = sorted(edges[now], reverse=True)
    for edge in now_edges:
        if not result[edge]:
            result[edge] = step
            step += 1
            deq.append(edge)

for i in result[1:]:
    print(i)