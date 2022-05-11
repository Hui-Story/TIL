string = input()
stack = []

for s in string:
    stack.append(s)
    if ''.join(stack[-4:]) == 'PPAP':
        for _ in range(3):
            stack.pop()

if stack == ['P']:
    print('PPAP')
else:
    print('NP')