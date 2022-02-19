from collections import defaultdict

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))
dict = defaultdict(int)
result = []

for card in cards:
    dict[card] += 1

for target in targets:
    result.append(dict[target])

print(*result)