lst = [12, 24, 35, 70, 88, 120, 155]

result = []

for i in range(len(lst)):
    if i % 2:
        result.append(lst[i])

print(result)