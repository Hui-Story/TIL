result = []

for i in range(10):
    if i == 0 or i == 1:
        result.append(1)
    else:
        result.append(result[i-2] + result[i-1])

print(result)