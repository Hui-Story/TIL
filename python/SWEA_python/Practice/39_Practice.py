list = [2, 4, 6, 8, 10]

def number(n):
    if n in list:
        print(f'{n} => True')
    else:
        print(f'{n} => False')

print(list)
number(5)
number(10)