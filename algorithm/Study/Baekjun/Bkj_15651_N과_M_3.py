
def N_M(n, lst):
    if len(lst) == M:
        print(*lst)
        return
    for i in range(1, n + 1):
        N_M(n, lst + [i])

N, M = map(int, input().split())

N_M(N, [])