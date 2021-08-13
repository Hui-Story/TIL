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
        if lst[i] == 0:
            result.append(i)
            lst[i] = 1
            dfs(result, lst)
            result.pop()
            lst[i] = 0

dfs(result, lst)