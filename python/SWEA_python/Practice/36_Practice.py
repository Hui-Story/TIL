number = int(input())

def prime(number):
    i = 1
    count = 0
    while i * i < number:
        if number % i == 0:
            count += 2
        i += 1
    if i * i == number:
        count += 1
    if count == 2:
        print('소수입니다.')
    else:
        print('소수가 아닙니다.')

prime(number)