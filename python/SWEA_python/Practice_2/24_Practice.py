lst1 = [1,3,6,78,35,55]
lst2 = [12,24,35,24,88,120,155]

result = []

for i in lst1:
    if i in lst2:
        result.append(i)

print(result)