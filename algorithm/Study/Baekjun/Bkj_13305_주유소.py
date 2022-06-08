import sys
input = sys.stdin.readline

N = int(input())
roads = list(map(int, input().split()))
oil_costs = list(map(int, input().split()))

min_cost = oil_costs[0]
result = 0
for i in range(N - 1):
    if min_cost > oil_costs[i]:
        min_cost = oil_costs[i]
    result += min_cost * roads[i]

print(result)