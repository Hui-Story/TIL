word = input().split()

result = []

for i in range(len(word)-1, -1, -1):
    result.append(word[i])

print(*result)