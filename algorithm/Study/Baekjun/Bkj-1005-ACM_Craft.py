import sys
from typing import List
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline
II = lambda: int(input())
MIIS = lambda: map(int, input().split())

def dfs(n: int) -> None:
    global answer, pre_cnt
    for i in pre_builds[n]:
        pre_cnt[i] -= 1
        answer[i] = max(answer[i], answer[n] + D[i])
        if not pre_cnt[i]:
            dfs(i)


T: int = II()

for _ in range(T):
    N, K = MIIS()
    D: List[int] = [0] + list(MIIS())
    answer: List[int] = D[:]
    pre_builds: List[List[int]] = [[] for _ in range(N + 1)]
    pre_cnt: List[int] = [0] * (N + 1)

    for _ in range(K):
        X, Y = MIIS()
        pre_builds[X].append(Y)
        pre_cnt[Y] += 1
    
    for i in range(1, N + 1):
        if pre_cnt[i] == 0:
            pre_builds[0].append(i)
    
    for n in pre_builds[0]:
        dfs(n)

    W: int = II()
    print(answer[W])