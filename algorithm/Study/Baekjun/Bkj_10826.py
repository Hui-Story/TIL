n = int(input())

Fib_list = [0, 1, 0]
for i in range(2, n+1):
    Fib_list[2] = Fib_list[0] + Fib_list[1]
    Fib_list[0] = Fib_list[1]
    Fib_list[1] = Fib_list[2]

if n == 0:
    print(0)
elif n == 1:
    print(1)
elif n > 1:
    print(Fib_list[2])