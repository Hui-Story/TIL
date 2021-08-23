words = str(input())

result ={}

for word in words:
    result[word] = 0

for word in words:
    result[word] += 1

for key in result.keys():
    print('{},{}'.format(key, result[key]))