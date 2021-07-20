n = int(input())

def Fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fib(n-2) + Fib(n-1)

print(Fib(n))