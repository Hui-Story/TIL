K = int(input())
numbers = list(int(input()) for _ in range(K))

stack = []
for i in numbers:
    if i != 0:
        stack.append(i)
    else:
        stack.pop()

print(sum(stack))