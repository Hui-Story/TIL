import sys
input = sys.stdin.readline

def card_count():
    global card_check
    for i in range(0, len(S), 3):
        card_shape = S[i]
        card_num = S[i+1:i+3]
        if card_check[shape_dic[card_shape]+int(card_num)] == 1:
            card_check[shape_dic[card_shape]+int(card_num)] = 0
        else:
            print('GRESKA')
            return
    print(f'{sum(card_check[:13])} {sum(card_check[13:26])} {sum(card_check[26:39])} {sum(card_check[39:52])}')
    return
    
S = str(input())

card_check = [1]*52
shape_dic = {'P': -1, 'K': 12, 'H': 25, 'T': 38}

card_count()