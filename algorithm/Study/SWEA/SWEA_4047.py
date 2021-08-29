def card():
    global S, dic
    for i in range(0, len(S), 3):
        card = S[i]
        num = int(S[(i+1):(i+3)])
        if dic[card][num] == 1:
            dic[card][num] = 0
        else:
            print('#{} ERROR'.format(case))
            return

    print('#{} {} {} {} {}'.format(case, sum(dic['S'])-1, sum(dic['D'])-1, sum(dic['H'])-1, sum(dic['C'])-1))


T = int(input())

for case in range(1, T+1):
    S = str(input())

    dic = {}

    dic['S'] = [1] * 14
    dic['D'] = [1] * 14
    dic['H'] = [1] * 14
    dic['C'] = [1] * 14

    card()