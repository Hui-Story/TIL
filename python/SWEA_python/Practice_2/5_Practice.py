lst = []

for i in range(2, 10):
    result = []
    for j in range(1, 10):
        if (i*j) % 3 and (i*j) % 7:
            result.append(i*j)
    lst.append(result)

print(lst)