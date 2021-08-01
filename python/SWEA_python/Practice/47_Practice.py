def multi(list):
    result = 1
    for i in list:
        result *= i
    return result

try:
    list = list(map(int, input().split(', ')))
    print(multi(list))
except:
    print('에러발생')