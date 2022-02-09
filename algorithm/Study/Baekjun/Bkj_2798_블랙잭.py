import itertools

N, M = map(int, input().split())
cards = list(map(int, input().split()))
result = 0

card_comb = itertools.combinations(cards, 3)

for a, b, c in card_comb:
    temp = sum([a, b, c])
    if temp <= M:
        result = max(result, temp)

print(result)