import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    num = int(input())
    length = len(str(num))
    if str(num * num)[-length:] == str(num):
        print('YES')
    else:
        print('NO')