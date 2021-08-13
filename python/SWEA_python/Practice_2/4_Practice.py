string = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
lst = []

for word in string:
    if word not in ['a','e','i','o','u']:
        lst.append(word)

print(''.join(lst))