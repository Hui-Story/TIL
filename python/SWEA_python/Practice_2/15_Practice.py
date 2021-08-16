import math

lst = list(map(int, input().split(',')))

result = []

for i in lst:
    result.append(str(round(2*math.pi*i, 2)))

print(', '.join(result))