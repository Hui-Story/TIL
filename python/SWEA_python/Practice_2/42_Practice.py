words = str(input())

result = ''

for i in range(len(words)):
    if i % 2 == 0:
        result += words[i]

print(result)