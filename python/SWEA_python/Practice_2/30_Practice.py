fruit = ['   apple    ','banana','  melon']

result = {}

for word in fruit:
    result[word.strip()] = len(word.strip())

print(result)