import sys
input = sys.stdin.readline

while True:
    num = str(input().strip())
    if num == '0':
        break
    for i in range(len(num) // 2):
        if num[i] != num[len(num) - i - 1]:
            print('no')
            break
    else:
        print('yes')