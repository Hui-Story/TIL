
def fib(n):
    global result
    if n == 1 or n == 2:
        result[0] += 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fibonacci(n):
    global result
    f = [0] * 41
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        result[1] += 1
        f[i] = f[i - 1] + f[i - 2]

n = int(input())
result = [0, 0]

fib(n)
fibonacci(n)
print(*result)