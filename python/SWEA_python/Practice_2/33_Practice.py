words = str(input())

upper = 0
lower = 0

for word in words:
    if word.isupper():
        upper += 1
    elif word.islower():
        lower += 1

print('UPPER CASE {}'.format(upper))
print('LOWER CASE {}'.format(lower))