def func(D, K):
    global a, b
    if D == 3:
        return [1, K-1]
    else:
        for num1 in range(1, 100001):
            if (K - num1*a) % b == 0:
                num2 = int((K - num1*a) / b)
                return [num1, num2]

D, K = map(int, input().split())

a = b = 1

for _ in range(4, D+1):
    a, b = b, a+b

for i in func(D, K):
    print(i)