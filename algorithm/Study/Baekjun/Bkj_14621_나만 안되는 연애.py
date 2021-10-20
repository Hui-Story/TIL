import sys
input = sys.stdin.readline

def Union(a, b, cost):
    global N, parent, result
    pa = Find(a)
    pb = Find(b)
    # 같은 집합이 아닌 경우 연결하고, N 을 감소시키면서 도로의 개수를 카운트
    if pa != pb:
        N -= 1
        result += cost
        if pa < pb:
            parent[pb] = pa
        else:
            parent[pa] = pb

def Find(ch):
    if parent[ch] != ch:
        parent[ch] = Find(parent[ch])
    return parent[ch]

# 도로의 개수가 N-1 개가 될 때까지 탐색
# 모든 학교를 연결하지 못하는 경우를 고려하여 탐색할 수 있는 도로가 없으면 탐색 중지
def Kruskal():
    i = 0
    while N != 1 and i < len(edges):
        cost, a, b = edges[i]
        Union(a, b, cost)
        i += 1


N, M = map(int, input().split())
university = list(map(str, input().split()))
parent = [i for i in range(N+1)]  # 부모 노드를 자기 자신으로 초기화
edges = []
result = 0

for _ in range(M):
    u, v, d = map(int, input().split())
    # 학교가 각각 남초, 여초 대학교라면 간선 리스트에 추가
    if university[u-1] != university[v-1]:
        edges.append((d, u, v))

edges.sort(key=lambda x : x[0])

Kruskal()

# 도로의 개수가 N-1 개인 경우 (N 이 1 까지 감소) 모두 연결
if N == 1:
    print(result)
else:
    print(-1)