import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def Union(a, b):
    pa = Find(a)
    pb = Find(b)
    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb

def Find(ch):
    if parent[ch] == ch:
        return ch
    parent[ch] = Find(parent[ch])
    return parent[ch]


N = int(input())

# 섬의 부모 노드를 자기 자신으로 초기화
parent = [i for i in range(N+1)]

result = []

# 남아있는 다리들을 연결
for _ in range(N-2):
    a, b = map(int, input().split())
    Union(a, b)

# 집합 중에서 루트 노드를 탐색 (부모 노드가 자기 자신)
for i in range(1, N+1):
    if i == parent[i]:
        result.append(i)
    if len(result) == 2:
        break

print(*result)