from itertools import combinations

N, L, R, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
result = 0

for i in range(2, N + 1):
    A_comb = list(combinations(A, i))
    for comb in A_comb:
        total_score = sum(comb)
        if L <= total_score and total_score <= R and (comb[-1] - comb[0]) >= X:
            result += 1

print(result)