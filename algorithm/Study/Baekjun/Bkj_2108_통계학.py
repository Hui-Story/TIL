import sys
input = sys.stdin.readline

N = int(input())
numbers = []
number_count = [0] * 8001
for _ in range(N):
    number = int(input())
    number_count[number + 4000] += 1
    numbers.append(number)
numbers.sort()

max_cnt = 1
max_num = []
for i in range(8001):
    if number_count[i] == max_cnt:
        if len(max_num) <= 1:
            max_num.append(i - 4000)
    elif number_count[i] > max_cnt:
        max_cnt = number_count[i]
        max_num = [i - 4000]

print(round(sum(numbers) / N))
print(numbers[N // 2])
print(max_num[-1])
print(numbers[-1] - numbers[0])