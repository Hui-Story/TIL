
def baby_jin():
    global players
    for i in range(12):
        if not i % 2:
            players[0][cards[i]] += 1
            if check_run(0):
                return 1
            if check_triplet(0):
                return 1
        else:
            players[1][cards[i]] += 1
            if check_run(1):
                return 2
            if check_triplet(1):
                return 2
    return 0

def check_run(num):
    cnt = 0
    for i in players[num]:
        if i:
            cnt += 1
        else:
            cnt = 0
        if cnt == 3:
            return True
    return False


def check_triplet(num):
    for i in players[num]:
        if i == 3:
            return True
    return False


T = int(input())

for case in range(1, T+1):
    cards = list(map(int, input().split()))
    players = [[0] * 10, [0] * 10]

    print('#{} {}'.format(case, baby_jin()))