def oper(num_i, now):
    global operator, max_result, min_result, cnt
    if sum(operator) == 0:
        max_result = max(max_result, now)
        min_result = min(min_result, now)
        return
    num = numbers[num_i+1]
    for i in range(4):
        if operator[i]:
            if i == 0:
                now_2 = now + num
            elif i == 1:
                now_2 = now - num
            elif i == 2:
                now_2 = now * num
            else:
                if now < 0:
                    now_2 = -(-(now) // num)
                else:
                    now_2 = now // num
            operator[i] -= 1
            oper(num_i+1, now_2)
            operator[i] += 1

N = int(input())
numbers = list(map(int, input().split()))
operator = list(map(int, input().split()))

max_result = -2e+10
min_result = 2e+10
cnt = 0

oper(0, numbers[0])

print(max_result)
print(min_result)