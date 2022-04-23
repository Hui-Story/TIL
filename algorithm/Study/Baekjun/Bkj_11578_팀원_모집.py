import sys, itertools
input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

N, M = MIIS()
members = [0] * M
solution = (1 << N) - 1

for i in range(M):
    O, *problems = MIIS()
    for problem in problems:
        members[i] |= 1 << (problem - 1)

for i in range(1, M + 1):
    combi = list(itertools.combinations(range(0, M), i))
    for c in combi:
        bit = 0
        for num in c:
            bit |= members[num]
        if bit == solution:
            print(len(c))
            exit()

print(-1)