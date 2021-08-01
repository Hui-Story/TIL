star = 7
space = 0

while star >= 1:
    result = ' ' * space + '*' * star + ' ' * space
    print(result)
    star -= 2
    space += 1