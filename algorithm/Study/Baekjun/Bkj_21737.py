N = int(input())
words = str(input())

SMUPC = ''
now_num = ''
result = 0
C_check = False
output = []

for word in words:
    if word in 'SMUPC':
        if SMUPC != 'C':
            num = int(now_num)
        if SMUPC == 'S':
            result -= num
        elif SMUPC == 'M':
            result *= num
        elif SMUPC == 'U':
            if result < 0:
                result = -((-result) // num)
            else:
                result = result // num
        elif SMUPC == 'P':
            result += num
        elif SMUPC == 'C':
            pass
        else:
            result = num
        if word == 'C':
            C_check = True
            output.append(result)
        SMUPC = word
        now_num = ''
    else:
        now_num += word

if not C_check:
    print('NO OUTPUT')
else:
    print(*output)