arr = list(map(str, input().split()))

result = []

for word in arr:
    if word not in result:
        result.append(word)

result.sort()

print(','.join(result))