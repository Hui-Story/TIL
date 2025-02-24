import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def Union(a: int, b: int, cost: int) -> None:
    global V, parent, result
    pa = Find(a)
    pb = Find(b)
    # 같은 집합이 아닌 경우 연결하고, V 를 줄이면서 간선의 개수를 카운트
    if pa != pb:
        V -= 1
        result += cost
        if pa < pb:
            parent[pb] = pa
        else:
            parent[pa] = pb


def Find(ch: int) -> int:
    if parent[ch] != ch:
        parent[ch] = Find(parent[ch])
    return parent[ch]


# cost 가 낮은 순서대로 Union 을 진행
def Kruskal() -> None:
    i = 0
    # 간선을 V-1 개 연결하고 나면 중지
    while V != 1:
        cost, a, b = edges[i]
        Union(a, b, cost)
        i += 1


if __name__ == "__main__":
    V, E = MIIS()
    parent: list[int] = [i for i in range(V + 1)]  # 부모 노드를 자기 자신으로 초기화
    edges: list[tuple[int, int, int]] = []
    result: int = 0

    for _ in range(E):
        A, B, C = MIIS()
        edges.append((C, A, B))

    edges.sort(key=lambda x: x[0])  # C 에 대해 오름차순으로 정렬

    Kruskal()

    print(result)
