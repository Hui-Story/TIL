words = str(input())

letters = 0
digits = 0

for word in words:
    if word.isalpha():
        letters += 1
    elif word.isdigit():
        digits += 1

print('LETTERS {}'.format(letters))
print('DIGITS {}'.format(digits))