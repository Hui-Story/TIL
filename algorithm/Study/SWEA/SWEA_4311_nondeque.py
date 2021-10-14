def add_numbers(now_num, cnt):
    global numbers, used
    if len(now_num) == cnt:
        now_num = int(now_num)
        if used[now_num] == 100:
            used[now_num] = len(str(now_num))
            numbers.append(now_num)
        return
    for num in number_lst:
        add_numbers(now_num + str(num), cnt)

def op(num1, num2, oper):
    if oper == 1:
        return num1 + num2
    elif oper == 2:
        return num1 - num2
    elif oper == 3:
        return num1 * num2
    elif oper == 4:
        return num1 // num2


T = int(input())

for case in range(1, T+1):
    N, O, M = map(int, input().split())
    number_lst = list(map(int, input().split()))
    numbers = number_lst[:]
    operator = list(map(int, input().split()))
    target = int(input())
    used = [100] * 1000
    result = 100
    number_tmp = []
    for num in numbers:
        used[num] = 1
    for i in range(2, 4):
        add_numbers('', i)
    for num in numbers:
        number_tmp.append(num)
        if num == target:
            number_tmp.clear()
            result = used[num]
            break
    while number_tmp:
        number_lst = number_tmp[:]
        number_tmp.clear()
        for num1 in number_lst:
            for i in operator:
                for num2 in numbers:
                    if i == 4 and num2 == 0:
                        continue
                    num = op(num1, num2, i)
                    if num < 0 or num > 999 or (used[num1] + used[num2] + 2) > M:
                        continue
                    if num == target:
                        result = min(result, used[num1] + used[num2] + 2)
                        continue
                    if used[num] <= (used[num1] + used[num2] + 1):
                        continue
                    used[num] = used[num1] + used[num2] + 1
                    number_tmp.append(num)
    if result == 100:
        print(f'#{case} -1')
    else:
        print(f'#{case} {result}')