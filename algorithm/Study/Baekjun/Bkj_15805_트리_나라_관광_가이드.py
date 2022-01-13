N = int(input())

tour = list(map(int, input().split()))
parent = [-1] * (max(tour) + 1)
parent[tour[0]] = 0

for i in range(1, N-1):
    if parent[tour[i]] == -1:
        parent[tour[i]] = tour[i - 1]
parent[tour[0]] = -1

print(len(parent))
print(*parent)