import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

case = 0

def tree(now, parent):
    global dic, used, istree
    for i in dic[now]:
        if used[i] == 0:
            used[i] = 1
            tree(i, now)
        elif used[i] == 1 and i != parent:
            istree = False


while True:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    case += 1
    dic = {}
    used = [0] * (N + 1)
    result = 0

    for i in range(1, N + 1):
        dic[i] = []

    for _ in range(M):
        a, b = map(int, input().split())
        dic[a].append(b)
        dic[b].append(a)

    for i in range(1, N + 1):
        if len(dic[i]) == 0:
            result += 1
        elif used[i] == 0:
            used[i] = 1
            istree = True
            tree(i, 0)
            if istree:
                result += 1

    if result == 0:
        print('Case {}: No trees.'.format(case))
    elif result == 1:
        print('Case {}: There is one tree.'.format(case))
    else:
        print('Case {}: A forest of {} trees.'.format(case, result))