import sys
input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

D, N = MIIS()
ovens = list(MIIS())
pizza_doughs = list(MIIS())

min_diameter = 1000000000
for idx in range(D):
    if ovens[idx] < min_diameter:
        min_diameter = ovens[idx]
    ovens[idx] = min_diameter

idx = D - 1
possible_dough_count = 0
for pizza_dough in pizza_doughs:
    while idx >= 0:
        if ovens[idx] >= pizza_dough:
            idx -= 1
            possible_dough_count += 1
            break
        idx -= 1

if possible_dough_count == N:
    print(idx + 2)
else:
    print(0)