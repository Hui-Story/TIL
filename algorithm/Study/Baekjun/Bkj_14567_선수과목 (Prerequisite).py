import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pre = [[] for _ in range(N+1)]
subject = [0] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())
    pre[B].append(A)

for idx in range(1, len(pre)):
    if not pre[idx]:
        subject[idx] = 1
    else:
        for sub in pre[idx]:
            subject[idx] = max(subject[idx], subject[sub]+1)

print(*subject[1:])