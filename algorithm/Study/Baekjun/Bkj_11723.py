import sys
input = sys.stdin.readline

M = int(input())
S = [0] * 21

for _ in range(M):
    inp = list(map(str, input().split()))
    if inp[0] == 'add':
        S[int(inp[1])] = 1
    elif inp[0] == 'remove':
        S[int(inp[1])] = 0
    elif inp[0] == 'check':
        if S[int(inp[1])]:
            print(1)
        else:
            print(0)
    elif inp[0] == 'toggle':
        S[int(inp[1])] = 1 - S[int(inp[1])]
    elif inp[0] == 'all':
        S = [1] * 21
    elif inp[0] == 'empty':
        S = [0] * 21