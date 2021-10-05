T = int(input())

for case in range(1, T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w.sort(reverse=True)
    t.sort(reverse=True)
    used = [0]*M
    result = 0
    
    for container in w:
        for ti in range(M):
            if not used[ti] and t[ti] >= container:
                used[ti] = 1
                result += container
                break
    
    print('#{} {}'.format(case, result))