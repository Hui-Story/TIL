import sys

N, M = map(int, sys.stdin.readline().split())

lst = [0] * (N+1)
result = []


def dfs(result: list, lst: list):
    global N, M
    if len(result) == M:
        print(*result)
        return
    for i in range(1, N+1):
        if result and i < result[-1]:
            continue
        elif lst[i] == False:
            result.append(i)
            lst[i] = True
            dfs(result, lst)
            result.pop()
            lst[i] = False

dfs([], [False]*(N+1))