T = int(input())

for case in range(1, T+1):
    bit = str(input())
    now = '0'
    cnt = 0

    for i in bit:
        if i != now:
            cnt += 1
            now = i
    
    print('#{} {}'.format(case, cnt))