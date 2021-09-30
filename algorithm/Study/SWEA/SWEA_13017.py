T = int(input())

for case in range(1, T+1):
    N = float(input())
    
    i = 1
    now = 0
    result = ''

    while True:
        if i >= 13:
            result = 'overflow'
            break
        if now + 2**(-i) <= N:
            now += 2**(-i)
            result += '1'
        else:
            result += '0'

        if now == N:
            break

        i += 1

    print('#{} {}'.format(case, result))