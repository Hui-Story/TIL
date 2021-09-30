import sys
input = sys.stdin.readline

M = int(input())
S = 1 << 21

for _ in range(M):
    inp = list(map(str, input().split()))
    if len(inp) == 1:
        order = inp[0]
    else:
        order, num = inp[0], int(inp[1])
    if order == 'add':
        S |= (1 << num)
    elif order == 'remove':
        if S & (1 << num):
            S ^= (1 << num)
    elif order == 'check':
        if S & (1 << num):
            print(1)
        else:
            print(0)
    elif order == 'toggle':
        S ^= (1 << num)
    elif order == 'all':
        S = (1 << 22) - 1
    elif order == 'empty':
        S = 1 << 21