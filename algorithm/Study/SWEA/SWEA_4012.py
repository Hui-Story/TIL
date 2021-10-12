from collections import deque

def cook(cnt, now):
    global A, B
    if cnt >= (N // 2):
        for i in range(N):
            if used[i]:
                A.append(i)
            else:
                B.append(i)
        score()
        A.clear()
        B.clear()
        return
    for i in range(now, N):
        used[i] += 1
        cook(cnt+1, i+1)
        used[i] -= 1

def score():
    global differ, result
    differ = 0
    for i in A:
        for j in A:
            differ += S[i][j]
    for i in B:
        for j in B:
            differ -= S[i][j]
    result = min(result, abs(differ))


T = int(input().rstrip())

for case in range(1, T+1):
    N = int(input().rstrip())
    S = [list(map(int, input().rstrip().split())) for _ in range(N)]
    used = [0] * N

    A = deque()
    B = deque()
    differ = 0
    result = 2e+10

    cook(0, 0)

    print('#{} {}'.format(case, result))