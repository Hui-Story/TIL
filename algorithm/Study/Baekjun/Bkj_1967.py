import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def tree(now, total):
    global N, dic, used, max_total, max_idx
    cnt = 0
    for i in dic[now]:
        if used[i[0]] == 0:
            used[i[0]] = 1
            tree(i[0], total+i[1])
            used[i[0]] = 0
            cnt += 1
    if cnt == 0 and total > max_total:
        max_total = total
        max_idx = now

N = int(input())

dic = {}
used = [0] * (N+1)
used[1] = 1
max_total = 0
max_idx = 0

for i in range(1, N+1):
    dic[i] = []

for _ in range(N-1):
    a, b, c = map(int, input().split())
    dic[a].append([b, c])
    dic[b].append([a, c])

if N != 1:
    tree(1, 0)

    used[1] = 0
    used[max_idx] = 1
    max_total = 0

    tree(max_idx, 0)

print(max_total)