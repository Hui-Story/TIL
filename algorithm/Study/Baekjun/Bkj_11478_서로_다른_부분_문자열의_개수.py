import collections

S = input()
LS = len(S)
dict = collections.defaultdict(int)
result = 0

for i in range(1, LS + 1):
    for j in range(LS + 1 - i):
        NS = S[j : j + i]
        if not dict[NS]:
            dict[NS] = 1
            result += 1

print(result)