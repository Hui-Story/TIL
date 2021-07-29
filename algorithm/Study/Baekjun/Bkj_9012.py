T = int(input())
parens = list(str(input()) for _ in range(T))

for paren in parens:
    stack = []
    for i in paren:
        if i == '(':
            stack.append('(')
        elif i == ')' and '(' in stack:
            stack.pop()
        else:
            print('NO')
            break
    else:
        if stack == []:
            print('YES')
        else:
            print('NO')