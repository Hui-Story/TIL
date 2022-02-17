import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    order = str(input().strip())
    if order == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif order == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else:
        num = int(order[5:])
        stack.append(num)