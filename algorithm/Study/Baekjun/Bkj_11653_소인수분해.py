N = int(input())

i = 2
while N > 1:
    if not N % i:
        N = N / i
        print(i)
    else:
        i += 1