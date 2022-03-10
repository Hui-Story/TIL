M, N = map(int, input().split())

check_decimal = [False] + [True] * N
check_decimal[1] = False
decimal_lst = []

for num in range(2, N + 1):
    if check_decimal[num]:
        for i in range(num * 2, N + 1, num):
            check_decimal[i] = False

for num in range(M, N + 1):
    if check_decimal[num]:
        decimal_lst.append(num)

for num in decimal_lst:
    print(num)