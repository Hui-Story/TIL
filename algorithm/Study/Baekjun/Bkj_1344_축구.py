A = int(input()) / 100
B = int(input()) / 100

fact = [1] * 19
for i in range(1, 19):
    fact[i] = fact[i - 1] * i

PA = 0
PB = 0
for n in (0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18):
    PA += ((A ** n) * ((1 - A) ** (18 - n)) * (fact[18] / (fact[18 - n] * fact[n])))
    PB += ((B ** n) * ((1 - B) ** (18 - n)) * (fact[18] / (fact[18 - n] * fact[n])))

print(1 - PA * PB)