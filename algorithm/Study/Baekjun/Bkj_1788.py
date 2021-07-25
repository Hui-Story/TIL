n = int(input())

Fib = [0, 1, 0]
if n > 1:
    for i in range(2, n+1):
        Fib[2] = (Fib[0] + Fib[1]) % 1000000000
        Fib[0] = Fib[1]
        Fib[1] = Fib[2]
elif n < 0:
    Fib = [1, 0, 0]
    for i in range(-1, n-1, -1):
        if (Fib[0] - Fib[1]) < 0:
            Fib[2] = (Fib[0] - Fib[1]) % -1000000000
        else:
            Fib[2] = (Fib[0] - Fib[1]) % 1000000000
        Fib[0] = Fib[1]
        Fib[1] = Fib[2]

if n == 0:
    print(0)
    print(0)
elif n == 1:
    print(1)
    print(1)
else:
    if Fib[2] < 0:
        print(-1)
        print(-Fib[2])
    elif Fib[2] == 0:
        print(0)
        print(Fib[2])
    elif Fib[2] > 0:
        print(1)
        print(Fib[2])