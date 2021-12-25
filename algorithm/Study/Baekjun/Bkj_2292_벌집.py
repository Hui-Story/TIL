N = int(input())

if N == 1:
    print(1)
else:
    num = 1
    step = 1
    while True:
        num += step * 6
        step += 1
        if N <= num:
            print(step)
            break