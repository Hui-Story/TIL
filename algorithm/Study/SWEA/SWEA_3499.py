T = int(input())

for case in range(1, T+1):
    N = int(input())
    cards = list(map(str, input().split()))

    result = []

    if len(cards) % 2:
        for i in range(N//2):
            result.append(cards[i])
            result.append(cards[i+(N//2)+1])
        result.append(cards[N//2])
    else:
        for i in range(N//2):
            result.append(cards[i])
            result.append(cards[i+(N//2)])
    
    print('#{} {}'.format(case, ' '.join(result)))