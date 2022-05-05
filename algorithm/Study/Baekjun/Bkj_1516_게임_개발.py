import sys
input = sys.stdin.readline

def dfs(n):
    global result
    for i in pre_lst[n]:
        pre_cnt[i] -= 1
        result[i] = max(result[i], result[n] + times[i])
        if not pre_cnt[i]:
            dfs(i)

N = int(input())
times = [0]
pre_lst = [[] for _ in range(N + 1)]
pre_cnt = [0] * (N + 1)
for i in range(1, N + 1):
    info = list(map(int, input().split()))
    times.append(info[0])
    if len(info) == 2:
        pre_lst[0].append(i)
        continue
    for j in info[1:]:
        if j != -1:
            pre_lst[j].append(i)
            pre_cnt[i] += 1
result = times[:]

for n in pre_lst[0]:
    dfs(n)

for i in result[1:]:
    print(i)