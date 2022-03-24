import sys
input = sys.stdin.readline

numbers = [0, 0] + [1] * 246911
for num in range(1, 246913):
    if numbers[num]:
        for i in range(num * 2, 246913, num):
            numbers[i] = 0

while True:
    n = int(input())
    if n == 0:
        break
    print(sum(numbers[n + 1:(n * 2) + 1]))