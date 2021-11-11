N = int(input())
numbers = list(int(input()) for _ in range(N))

# 가장 큰 수를 뒤로 보내면서 정렬
for i in range(len(numbers)):
    for j in range(1, len(numbers)-i):
        if numbers[j-1] > numbers[j]:
            numbers[j-1], numbers[j] = numbers[j], numbers[j-1]
        else:
            continue
for i in numbers:
    print(i)