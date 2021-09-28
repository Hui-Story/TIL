import sys
input = sys.stdin.readline

inp = str(input())

minus = False
num = ''
num_cnt = 0
result = 0

for i in inp:
    if i == '+':
        num_cnt += int(num)
        num = ''
    elif i == '-':
        num_cnt += int(num)
        num = ''
        if minus:
            result -= num_cnt
            num_cnt = 0
        else:
            result += num_cnt
            num_cnt = 0
        minus = True
    else:
        num += i

num_cnt += int(num)

if minus:
    result -= num_cnt
else:
    result += num_cnt

print(result)