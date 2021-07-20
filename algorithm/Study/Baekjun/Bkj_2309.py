N = list(int(input()) for _ in range(9))

all = 0

for i in range(0, 9):
    all += N[i]

for i in range(0, 9):
    for j in range(0, 9):
        if (i < j) and ((all - N[i] - N[j]) == 100):
            del N[j]
            del N[i]
            N.sort()
            for k in N:
                print(k)
            break
    if len(N) < 9:
        break