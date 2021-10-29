import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    result = 0
    cnt = 0
    inp = str(input().strip())
    for i in inp:
        if i == 'O':
            cnt += 1
        elif i == 'X':
            cnt = 0
        result += cnt
    print(result)