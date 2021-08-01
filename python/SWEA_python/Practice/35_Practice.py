player_1 = str(input())
player_2 = str(input())

player_1_pick = str(input())
player_2_pick = str(input())

def play(pick_1, pick_2):
    if pick_1 == pick_2:
        print('비겼습니다.')
    elif pick_1 == '가위' and pick_2 == '바위':
        print('바위가 이겼습니다!')
    elif pick_1 == '가위' and pick_2 == '보':
        print('가위가 이겼습니다!')
    elif pick_1 == '바위' and pick_2 == '가위':
        print('바위가 이겼습니다!')
    elif pick_1 == '바위' and pick_2 == '보':
        print('보가 이겼습니다!')
    elif pick_1 == '보' and pick_2 == '가위':
        print('가위가 이겼습니다!')
    elif pick_1 == '보' and pick_2 == '바위':
        print('보가 이겼습니다!')

play(player_1_pick, player_2_pick)