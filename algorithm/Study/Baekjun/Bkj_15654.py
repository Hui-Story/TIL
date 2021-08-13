import sys

N, M = map(int, sys.stdin.readline().split())
num_lst = list(map(int, sys.stdin.readline().split()))
num_lst.sort()

lst = [0] * N
result = []

def dfs(result: list, lst: list):
    global N, M, num_lst
    if len(result) == M:
        print(*result)
        return
    for i in range(0, len(num_lst)):
        if lst[i] == 0:
            result.append(num_lst[i])
            lst[i] = 1
            dfs(result, lst)
            result.pop()
            lst[i] = 0

dfs(result, lst)