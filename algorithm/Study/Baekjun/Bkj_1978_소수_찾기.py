N = int(input())
numbers = list(map(int, input().split()))

result = 0

for num in numbers:
    if num == 1:
        continue
    for i in range(2, num):
        if not num % i:
            break
    else:
        result += 1

print(result)