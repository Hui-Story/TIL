N = int(input())
numbers = list(int(input()) for _ in range(N))

for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i] < numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
        else:
            continue

print(numbers)