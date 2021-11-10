
def bitwise_operation(a, b):
    while a & (a - 1) and b & (b - 1):
        a, b = a & b, a | b
    for n in [a, b]:
        if n & (n - 1):
            remain_lst.append(n)
        else:
            power_lst.append(n)


N = int(input())
numbers = list(map(int, input().split()))

power_lst = []
remain_lst = []

while len(numbers) > 1:
    for i in range(0, len(numbers), 2):
        if i+1 < len(numbers):
            bitwise_operation(numbers[i], numbers[i+1])
        else:
            if numbers[i] & (numbers[i] - 1):
                remain_lst.append(numbers[i])
            else:
                power_lst.append(numbers[i])
    numbers = remain_lst[:]
    remain_lst = []

if numbers:
    power_lst.append(numbers[0])

for i in range(len(power_lst)-2):
    if power_lst[i] != power_lst[i+1]:
        print(0)
        break
else:
    result = 1
    for i in power_lst:
        result = result * (i % (10**9 + 7))
    print(result)