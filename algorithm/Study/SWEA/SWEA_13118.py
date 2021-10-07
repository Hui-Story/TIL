def bus(num, cnt):
    global result
    if cnt > result:
        return
    now = battery[num]
    for i in range(1, now+1):
        if num+i == N-1:
            result = min(result, cnt)
            return
        bus(num+i, cnt+1)


T = int(input())

for case in range(1, T+1):
    inp = list(map(int, input().split()))
    N = inp[0]
    battery = inp[1:]
    result = 2e+10

    bus(0, 0)

    print('#{} {}'.format(case, result))