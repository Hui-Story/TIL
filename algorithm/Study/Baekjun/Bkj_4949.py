parens = []
while True: 
  n = input()
  if n=='.':
    break
  parens.append(n)

for paren in parens:
    stack = [0]
    for i in paren:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                print('no')
                break
        elif i == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                print('no')
                break
    else:
        if stack == [0]:
            print('yes')
        else:
            print('no')