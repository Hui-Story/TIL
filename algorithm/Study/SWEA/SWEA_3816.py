from collections import defaultdict

T = int(input())

for case in range(1, T+1):
    S1, S2 = list(map(str, input().split(' ')))

    dic = defaultdict(int)
    for i in S1:
        dic[i] += 1
    
    cnt = 0
    result = 0
    check = 0

    for i in range(len(S2)):
        if i >= len(S1):
            if dic[S2[i-len(S1)]] < 0:
                dic[S2[i-len(S1)]] += 1
                cnt -= 1
                check += 1
            else:
                dic[S2[i-len(S1)]] += 1
                cnt -= 1
        if dic[S2[i]] > 0:
            dic[S2[i]] -= 1
            cnt += 1
        else:
            dic[S2[i]] -= 1
            cnt += 1
            check -= 1
        if cnt == len(S1) and check == 0:
            result += 1

    print('#{} {}'.format(case, result))