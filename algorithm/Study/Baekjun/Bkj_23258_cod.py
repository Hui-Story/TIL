import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
graph = [[] for _ in range(300)]
for i in range(N):
    inp = list(map(int, input().split()))
    for j in range(N):
        if inp[j]:
            graph[i].append([j ,inp[j]])

dp = [[[0]*300 for _ in range(300)] for _ in range(300)]

for _ in range(Q):
    C, s, e = map(int, input().split())

