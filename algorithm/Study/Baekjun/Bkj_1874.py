n = int(input())
numbers = list(int(input()) for _ in range(n))

stack = [0]
idx = 0
number = 1
push_pop = []
while idx < n:
    if number == n+1 and stack[-1] != numbers[idx]:
        break
    else:
        if stack[-1] == numbers[idx]:
            stack.pop()
            push_pop.append('-')
            idx += 1
        elif number == numbers[idx]:
            # stack.append(number)
            push_pop.append('+')
            # stack.pop()
            push_pop.append('-')
            idx += 1
            number += 1
        else:
            stack.append(number)
            push_pop.append('+')
            number += 1

if stack == [0]:
    for result in push_pop:
      print(result)
else:
    print('NO')