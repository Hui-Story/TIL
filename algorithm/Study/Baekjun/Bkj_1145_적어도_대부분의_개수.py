numbers = list(map(int, input().split()))

min_num = min(numbers)
while True:
    cnt = 0
    for i in range(len(numbers)):
        if min_num % numbers[i] == 0:
            cnt += 1
    if cnt >= 3:
        print(min_num)
        break
    min_num += 1