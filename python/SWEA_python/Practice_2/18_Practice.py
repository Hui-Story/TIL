input_lst = list(map(int, input().split(', ')))

result = []

for i in input_lst:
    if i % 2:
        result.append(str(i))

result2 = ', '.join(result)

print(result2)