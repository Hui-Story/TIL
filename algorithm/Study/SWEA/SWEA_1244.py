def change(cnt):
    global num
    if cnt == 0:
        number = ''
        for i in num:
            number += str(i)
        result.append(int(number))
        return
    for i in range(N-1):
        max_num = max(num[i+1:])
        if num[i] < max_num:
            if num.count(max_num) == 1:
                for i_r in range(N-1, i, -1):
                    if num[i_r] == max(num[i+1:]):
                        num[i], num[i_r] = num[i_r], num[i]
                        change(cnt-1)
                        return
            else:
                for i_r in range(N-1, i, -1):
                    if num[i_r] == max(num[i+1:]):
                        num[i], num[i_r] = num[i_r], num[i]
                        change(cnt-1)
                        num[i], num[i_r] = num[i_r], num[i]
                return

    for i in range(N-1):
        for j in range(i+1, N):
            if num[i] == num[j]:
                change(cnt-1)
                return
    
    num[-1], num[-2] = num[-2], num[-1]
    change(cnt-1)
    return


T = int(input())

for case in range(1, T+1):
    num, cnt = map(str, input().split())
    num, cnt = list(map(int, num)), int(cnt)
    N = len(num)
    result = []

    change(cnt)
    
    print('#{} {}'.format(case, max(result)))