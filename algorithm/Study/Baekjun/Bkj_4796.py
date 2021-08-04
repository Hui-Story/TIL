case = 0
while True:
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break
    else:
        case += 1
        count = 0
        while V:
            if V >= P:
                V -= P
                count += L
            elif V >= L:
                V = 0
                count += L
            else:
                count += V
                V = 0
        print(f'Case {case}: {count}')