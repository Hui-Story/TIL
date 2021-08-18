import sys
sys.setrecursionlimit(10**9)

def dfs(now_i):
    global lst2, result
    for i in lst2[now_i]:
        if result[i]:
            continue
        else:
            result[i] = now_i
            dfs(i)


N = int(input())

# lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N-1)]

lst2 = [[] for _ in range(N+1)]
result = [0] * (N+1)

for line in range(N-1):
    i, j = map(int, sys.stdin.readline().split())
    lst2[i].append(j)
    lst2[j].append(i)

dfs(1)

for i in range(2, N+1):
    print(result[i])