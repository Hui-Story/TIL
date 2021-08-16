result = []

for i in range(1, 21):
    if i % 3 or i % 5:
        result.append(i**2)

print(result)