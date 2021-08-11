import sys

N = int(input())
lst = [list(map(int, input().split())) for _ in range(4)]
check = [0] * (N+1)
check[1] = 1
result = []
count = 0
now_place = 1

def dfs(check: list, result: list, cost, count, now_place):
    global N, lst
    if count == N-1:
        if lst[now_place-1][0] == 0:
            return
        else:
            cost += lst[now_place-1][0]
            result.append(cost)
            return
    for i in range(1, N+1):
        if check[i] == 0 and lst[now_place-1][i-1] != 0:
            cost += lst[now_place-1][i-1]
            check[i] = 1
            now_place = i
            count += 1
            dfs(check, result, cost, count, now_place)
            check[i] = 0

dfs(check, result, 0, count, now_place)
print(min(result))