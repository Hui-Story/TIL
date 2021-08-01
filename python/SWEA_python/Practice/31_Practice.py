space = 4
star = 1

while space >= 0:
    result = ' ' * space + '*' * star
    print(result)
    space -= 1
    star += 1