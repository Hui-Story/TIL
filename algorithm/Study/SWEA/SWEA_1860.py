def fish_bread():
    global M, K, lst, cnt_lst
    cnt = 0
    for i in range(0, max(lst)+1):
        if i != 0 and i % M == 0:
            cnt += K
        if cnt >= cnt_lst[i]:
            cnt -= cnt_lst[i]
        else:
            return 'Impossible'
    return 'Possible'

T = int(input())

for case in range(1, T+1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt_lst = [0] * 11112

    for i in lst:
        cnt_lst[i] += 1

    print('#{} {}'.format(case, fish_bread()))