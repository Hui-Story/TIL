n = int(input())

def Fib(n):
    val = [0, 1]
    val_2 = []
    if n < 0:
        for i in range(-1, n-1, -1):
            val_2.append(val[i+2] - val[i+1])
        return val_2[n]
    elif n == 0 or n == 1:
        return val[n]
    else:
        for i in range(2, n+1):
            val.append(val[i-1] + val[i-2])
        return val[n]

n = n-1 + n-2

if Fib(n) > 0:
    print(1)
    print(Fib(n))
elif Fib(n) == 0:
    print(0)
    print(Fib(n))
else:
    print(-1)
    print(-Fib(n))