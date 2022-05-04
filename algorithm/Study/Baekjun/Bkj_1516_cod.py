import sys
input = sys.stdin.readline

def dfs(n, cnt):
    global result
    result[n] = max(result[n], cnt + times[n])
    for i in pre_lst[n]:
        dfs(i, result[n])

N = int(input())
times = [0]
pre_lst = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    info = list(map(int, input().split()))
    times.append(info[0])
    if len(info) == 2:
        pre_lst[0].append(i)
        continue
    for j in info[1:]:
        if j != -1:
            pre_lst[j].append(i)
result = times[:]

for n in pre_lst[0]:
    dfs(n, 0)

for i in result[1:]:
    print(i)